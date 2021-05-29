import re
from models import Categories, Product

clear = 'Очистить корзину'
back = 'К категориям'
to_cart = 'В корзину'
buy = 'Купить'
add = 'Добавить в корзину'
re_phone_number = re.compile(r'89\d{9}|[+]79\d{9}')


def collect_cart_sum(cart):
    total = 0
    for idx, good, price in cart["goods"]:
        total += price
    return total


def handle_categories(text, context):
    categories = [cat.category for cat in Categories.select()]
    for category in categories:
        chosen_category = re.search(category, text)
        chosen_cart = re.search(to_cart, text)
        if chosen_category:
            context['category'] = text
            return 'step2'
        elif chosen_cart:
            return 'step3'
    else:
        return False


def handle_carousel(text, context):
    continue_shopping = re.search(add, text)
    chosen_cart = re.search(to_cart, text)
    to_categories = re.search(back, text)
    if continue_shopping:
        idx = context['goods_idx']
        item = text[len(continue_shopping[0]) + 1:]
        price = Product.get(Product.title == item).price
        order = (idx, item, price)
        if order not in context['goods']:
            context['goods'].append(order)
            goods_content = []
            for good in context['goods']:
                formed = f'\n-{good[1]}.....{good[2]}р'
                goods_content.append(formed)
            if goods_content:
                context['goods_content'] = '\n'.join(goods_content)
            else:
                context['goods_content'] = 'Корзина пуста'
        else:
            pass
        return 'step2'
    elif chosen_cart:
        return 'step3'
    elif to_categories:
        return 'step1'
    else:
        return False


def handle_cart(text, context):
    to_categories = re.search(back, text)
    clear_cart = re.search(clear, text)
    purchase = re.search(buy, text)
    if purchase:
        context['cart_sum'] = collect_cart_sum(context)
        return 'step4'
    elif clear_cart:
        context['goods'] = []
        context['goods_content'] = 'Корзина пуста'
        return 'step1'
    elif to_categories:
        return 'step1'
    else:
        return False


def handle_submit(text, context):
    clear_cart = re.search(clear, text)
    purchase = re.search(buy, text)
    if purchase:
        context['confirmed'] = True
        return 'step5'
    elif clear_cart:
        context['goods'] = []
        context['goods_content'] = 'Корзина пуста'
        return 'step1'
    else:
        return False


def handle_phone(text, context):
    match = re.search(re_phone_number, text)
    if match:
        context['phone_number'] = match[0]
        return 'step6'
    else:
        return False
