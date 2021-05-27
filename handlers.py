import re
from assortment.assortment import prices

categories = ['Круассаны', 'Эклеры', 'Торты', ' Сытная выпечка']
clear = 'Очистить карзину'
back = 'К категориям'
to_cart = 'В корзину'
buy = 'Купить'
add = 'Добавить в корзину'
re_phone_number = re.compile(r'89\d{9}|[+]79\d{9}')


def collect_cart_sum(cart):
    total = 0
    for good in cart["goods"]:
        if good in prices:
            total += prices[good]
    return total


def handle_categories(text, context):
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
    next_step = re.search(to_cart, text)
    to_categories = re.search(back, text)
    if continue_shopping:
        item = text[len(continue_shopping[0]) + 1:]
        order = (item, prices[item])
        try:
            context['goods'].append(order)
        except KeyError:
            context['goods'] = [order]
        return 'step2'
    elif next_step:
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
        return 'step4'
    elif clear_cart:
        context['goods'] = []
        return 'step3'
    elif to_categories:
        return 'step1'
    else:
        return False


def handle_submit(text, context):
    clear_cart = re.search(clear, text)
    purchase = re.search(buy, text)
    if purchase:
        context['confirmed'] = True
        context['cart_sum'] = collect_cart_sum(context)
        return 'step5'
    elif clear_cart:
        context['goods'] = []
        return 'step3'
    else:
        return False


def handle_phone(text, context):
    match = re.search(re_phone_number, text)
    if match:
        context['number'] = match[0]
        return True
    else:
        return False
