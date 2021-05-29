from assortment.assortment import elements_by_category


def format_img_binary(img_path):
    img = open(img_path, 'rb')
    binary_img = img.read()
    return binary_img


def update_categories(cats, prods):
    for product in elements_by_category:
        product_category, created = cats.get_or_create(category=product['category'])
        if not created:
            cats.update(category=product['category']).where(cats.category == product_category.category).execute()
        binary_img = format_img_binary(product['image'])
        prod, created = prods.get_or_create(title=product['title'],
                                            description=product['description'],
                                            price=product['price'],
                                            photo=binary_img,
                                            category=product_category)
        if not created:
            prods.update(title=product['title'],
                         description=product['description'],
                         price=product['price'],
                         photo=binary_img,
                         category=product_category).where(prods.title == prod.title).execute()

