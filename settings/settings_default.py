TOKEN = " "
GROUP_ID = " "

INTENTS = [
    {
        "name": "Start",
        "tokens": ("/help", 'помощь', 'привет', 'hi', 'hello', 'здравствуй', '/start', 'заказ',
                   'салют', 'добрый день', 'добрый вечер', 'доброе утро', 'помоги', 'подскажи', 'start', 'старт'),
        "scenario": "shopping",
        "answer": "Добро пожаловать в кондитерскую 'Baked by bots'!"
                  "\nВы можете ознакомиться с нашим ассортиментом!"
    },
]

SCENARIOS = {
    "shopping": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": 'Выберите категорию',
                "keyboard": 'categories_kb',
                "template": None,
                "handler": "handle_categories",
            },
            "step2": {
                "text": 'Сейчас доступны:',
                "keyboard": 'carousel_kb',
                "template": 'carousel_template',
                "handler": "handle_carousel",
            },
            "step3": {
                "text": 'Вы заказали: ',
                "keyboard": 'cart_kb',
                "template": None,
                "handler": "handle_cart",
            },
            "step4": {
                "text": 'Подтвердите заказ',
                "keyboard": 'submit_kb',
                "template": None,
                "handler": "handle_submit",
            },
            "step5": {
                "text": 'Введите номер телефона. Менеджер с вами свяжется и уточнит все нюансы'
                        '\nПример ввода: 8хххххххххх',
                "keyboard": None,
                "template": None,
                "handler": "handle_phone",
            },
        }
    }
}

DEFAULT_ANSWER = " Для информации о работе бота используйте команду /help"
