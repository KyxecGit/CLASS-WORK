#поиск наибольшей цены из трёх
tovar1 = int(input('Цена первого товара:'))
tovar2 = int(input('Цена второго товара:'))
tovar3 = int(input('Цена третьего товара:'))
max_price = 0
if tovar1 >= tovar2:
    max_price = tovar1
    if tovar1 >= tovar3:
        max_price = tovar1
    else:
        max_price = tovar3
else:
    if tovar2 >= tovar3:
        max_price = tovar2
    else:
        max_price = tovar3

print('Акция! К оплате за три товара:',max_price)
