TOKEN = " "
GROUP_ID = " "

INTENTS = [
    {
        "name": "Start",
        "tokens": ("/help", 'помощь', 'привет', 'hi', 'hello', 'здравствуй', '/start', 'заказ',
                   'салют', 'добрый день', 'добрый вечер', 'доброе утро', 'помоги', 'подскажи', 'start', 'старт'),
        "scenario": None,
        "answer": "Добро пожаловать в кондитерскую 'Baked by bots'!"
                  "\nВы можете ознакомиться с нашим ассортиментом!",
        "keyboard": 'starting_kb'
    },
    {
        "name": "Shopping",
        "tokens": ('меню'),
        "scenario": "shopping",
        "answer": None,
        "keyboard": 'categories_kb'
    },
]

SCENARIOS = {
    "shopping": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": 'Выберите категорию',
                "alt_text": None,
                "keyboard": 'categories_kb',
                "template": None,
                "failure_text": "Прошу прощения, не понял вас, используйте кнопки",
                "handler": "handle_categories",
                "finish_scenario": False
            },
            "step2": {
                "text": 'В категории {category} представлены:',
                "alt_text": 'Добавляйте в корзину товары и выбирайте дальнейшие действия',
                "keyboard": 'carousel_kb',
                "template": 'carousel_template',
                "failure_text": "Прошу прощения, не понял вас, используйте кнопки",
                "handler": "handle_carousel",
                "finish_scenario": False
            },
            "step3": {
                "text": 'Корзина: \n{goods_content}',
                "alt_text": None,
                "keyboard": 'cart_kb',
                "template": None,
                "failure_text": "Прошу прощения, не понял вас, используйте кнопки",
                "handler": "handle_cart",
                "finish_scenario": False
            },
            "step4": {
                "text": 'Проверьте и подтвердите заказ'
                        '\n{goods_content}'
                        '\n'
                        '\nСумма: {cart_sum}',
                "alt_text": None,
                "keyboard": 'submit_kb',
                "template": None,
                "failure_text": "Прошу прощения, не понял вас, используйте кнопки",
                "handler": "handle_submit",
                "finish_scenario": False
            },
            "step5": {
                "text": 'Введите номер телефона. Менеджер с вами свяжется и уточнит все нюансы'
                        '\nПример ввода: 8хххххххххх',
                "alt_text": None,
                "keyboard": 'hidden_kb',
                "template": None,
                "failure_text": "Прошу прощения, не понял вас, используйте кнопки",
                "handler": "handle_phone",
                "finish_scenario": True
            },
            "step6": {
                "text": 'Спасибо за заказ, ожидайте звонка',
                "alt_text": None,
                "keyboard": 'hidden_kb',
                "template": None,
                "failure_text": None,
                "handler": None,
            },
        }
    }
}

DEFAULT_ANSWER = " Для информации о работе бота используйте команду /help"
