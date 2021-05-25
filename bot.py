#!/usr/bin/env python3.9
import logging

try:
    from settings import settings
except ImportError:
    exit('Do cp settings_default.py settings.py and set token')
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

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


# todo  начать писать логику бота
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

    def run(self):
        """Starting bot"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event=event)
            except Exception as exc:
                log.exception(f"Exception in handling event {exc}")

    def on_event(self, event):
        pass
