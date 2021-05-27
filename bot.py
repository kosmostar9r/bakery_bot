#!/usr/bin/env python3.9
import json
import logging
import random

from playhouse.db_url import connect

import handlers
import keyboards
import templates
from models import Client, ShoppingProgress

try:
    from settings import settings
except ImportError:
    exit('Do cp settings_default.py settings.py and set token')
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload

log = logging.getLogger("Bot")


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt='%d-%m-%Y %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:

    def __init__(self, group_id, token):
        """
        :param group_id: group id from vk group
        :param token: secret token from the same vk group
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()
        self.upload = VkUpload(self.vk)
        self.db = connect('sqlite:///bakery_bot.db')

    def connect_db(self):
        if not self.db.table_exists(Client):
            self.db.create_tables([Client])
        if not self.db.table_exists([ShoppingProgress]):
            self.db.create_tables([ShoppingProgress])

    def run(self):
        """Starting bot"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event=event)
            except Exception as exc:
                log.exception(f"Exception in handling event {exc}")

    def on_event(self, event):
        """
        Sending back text message

        :param event: VkBotMessageEvent object
        :return None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info("Can't handle this type of message %s", event.type)
            return

        user_id = event.obj['message']['peer_id']
        text = event.obj['message']['text']
        self.connect_db()

        state = Client.get_or_none(Client.user_id == str(user_id))

        if state is not None:
            self.continue_scenario(text, state, user_id)
        else:
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent["tokens"]):
                    if intent["answer"]:
                        keyboard = getattr(keyboards, intent['keyboard'])
                        self.send_text(intent["answer"], user_id, context=None, keyboard=keyboard)
                    else:
                        self.start_scenario(user_id, intent["scenario"])
                    break
            else:
                self.send_text(settings.DEFAULT_ANSWER, user_id, context=None)

    def send_text(self, text_to_send, user_id, context, keyboard=keyboards.hidden_kb, template=None):
        if template:
            template = self.format_image(template, context)
            self.api.messages.send(message=text_to_send,
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=user_id,
                                   template=template
                                   )
        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id,
                               keyboard=keyboard,
                               )

    def format_image(self, template, context):
        template = getattr(templates, template)(context['category'])

        for element in template['elements']:
            image = element['photo_id']
            upload_image = self.upload.photo_messages(photos=image)[0]
            owner_id = upload_image['owner_id']
            media_id = upload_image['id']
            attachment = f'{owner_id}_{media_id}'
            element['photo_id'] = attachment
        template = json.dumps(template, ensure_ascii=False).encode('utf-8')
        template = str(template.decode('utf-8'))
        return template

    def send_step(self, step, user_id, keyboard, template, context):
        self.send_text(step["text"].format(**context), user_id, context, keyboard, template)

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario["first_step"]
        step = scenario["steps"][first_step]
        keyboard = getattr(keyboards, step["keyboard"]) if step["keyboard"] else None
        template = getattr(templates, step["template"]) if step["template"] else None
        self.send_step(step, user_id, keyboard=keyboard, template=template, context={})

        Client.create(user_id=str(user_id),
                      scenario_name=scenario_name,
                      step_name=first_step,
                      context={})

    def continue_scenario(self, text, state, user_id):
        steps = settings.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]
        handler = getattr(handlers, step["handler"])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[handler(text=text, context=state.context)]
            next_step_name = handler(text=text, context=state.context)

            keyboard = getattr(keyboards, step["keyboard"]) if step["keyboard"] else None
            if step["template"]:
                template = getattr(templates, step["template"])
            else:
                template = None
            self.send_step(next_step, user_id, keyboard, template, context=state.context)
            if next_step:
                # switch to next step

                print(f'{next_step_name} ns')
                state.step_name = next_step_name

                print(f"{state.step_name} ns updated")
                # state.step_name = next_step_name

            else:
                # finish scenario
                log.info(state.context)
                ShoppingProgress.create(phone_number=state.context['phone_number'],
                                        cart_sum=state.context['cart_sum'],
                                        confirmed=state.context['confirmed'])
                Client.delete().where(Client.user_id == user_id).execute()
        else:
            # print('out of scenario')
            # # retry current step
            text_to_send = step["failure_text"].format(**state.context)
            self.send_text(text_to_send, user_id, context=state.context, keyboard=keyboards.categories_kb)
            Client.delete().where(Client.user_id == user_id).execute()


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
