import json

starting_kb = {
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "Меню",
                },
                "color": "primary"
            },
        ],
    ]
}
starting_kb = json.dumps(starting_kb, ensure_ascii=False).encode('utf-8')
starting_kb = str(starting_kb.decode('utf-8'))

hidden_kb = {"buttons": [],
             "one_time": True}
hidden_kb = json.dumps(hidden_kb, ensure_ascii=False).encode('utf-8')
hidden_kb = str(hidden_kb.decode('utf-8'))

categories_kb = {
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "Круассаны",
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Эклеры",
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Торты",
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Сытная выпечка",
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": "В корзину",
                },
                "color": "primary"

            }
        ]
    ],
    "inline": True
}
categories_kb = json.dumps(categories_kb, ensure_ascii=False).encode('utf-8')
categories_kb = str(categories_kb.decode('utf-8'))

carousel_kb = {
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "К категориям",
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "В корзину",
                },
                "color": "primary"
            }
        ],
    ]
}
carousel_kb = json.dumps(carousel_kb, ensure_ascii=False).encode('utf-8')
carousel_kb = str(carousel_kb.decode('utf-8'))

cart_kb = {
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "К категориям",
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Очистить корзину",
                },
                "color": "negative"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": "Купить",
                },
                "color": "positive"
            }
        ],
    ]
}
cart_kb = json.dumps(cart_kb, ensure_ascii=False).encode('utf-8')
cart_kb = str(cart_kb.decode('utf-8'))

submit_kb = {
    'buttons': [
        [
            {
                'action': {
                    'type': 'text',
                    'label': 'Купить'
                },
                'color': 'positive'
            },
            {
                'action': {
                    'type': 'text',
                    'label': 'Очистить корзину'
                },
                'color': 'negative'
            }
        ]
    ],
}
submit_kb = json.dumps(submit_kb, ensure_ascii=False).encode('utf-8')
submit_kb = str(submit_kb.decode('utf-8'))
