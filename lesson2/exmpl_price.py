phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount > 99:
        raise  ValueError('Слишком большая максимальная скидка')
    elif discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)

dis_iphone = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
dis_android = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
dis_noname = discounted(100, 10, name='')

print(dis_iphone)
print(dis_android)
print(dis_noname)