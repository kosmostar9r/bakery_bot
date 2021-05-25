from assortment.assortment import elements_by_category


# todo  разобраться как получать id фото
def create_elements(category):
    elements = []
    for elem in category:
        template = {
            'photo_id': elem['image'],
            'title': elem['title'],
            'description': elem['description'],
            'action': {
                'type': 'open_photo'
            },
            'buttons': [{
                'action': {
                    'type': 'text',
                    'label': f"Добавить в корзину {elem['title']}"
                }
            }]
        }
        elements.append(template)
    return elements


def carousel_template(category):
    carousel = {
        'type': 'carousel',
        'elements': create_elements(elements_by_category[category]),
    }
    return carousel


