from io import BytesIO
from models import Product, Categories


def get_photo(image):
    temp_file = BytesIO(image)
    temp_file.seek(0)
    return temp_file


def create_elements(category):
    elements = []
    category = Categories.get(category=category)
    products = [cat for cat in Product.select().where(Product.category == category)]
    for product in products:
        photo = get_photo(product.photo)
        template = {
            'photo_id': photo,
            'title': product.title,
            'description': product.description,
            'action': {
                'type': 'open_photo'
            },
            'buttons': [
                {
                    'action': {
                        'type': 'text',
                        'label': f"Добавить в корзину {product.title}"
                    },
                    "color": "primary"
                }]
        }
        elements.append(template)
    return elements


def carousel_template(category):
    carousel = {
        'type': 'carousel',
        'elements': create_elements(category),
    }
    return carousel
