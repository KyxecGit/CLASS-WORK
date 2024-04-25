total = int(input('Сумма:'))
time = int(input('Текущее время (час):'))
if time >= 20 and time <= 22:
    print('Акция! Итого к оплате:', total/2)
elif time >= 8 and time <= 19:
    print('Итого к оплате:', total)
else:
    print('Магазин не работает!')


category = input('Введите подкатегорию:')
if category == 'еда':
    print('Вам пригодятся: торт, чипсы, газировка')
elif category == 'оформление':
    print('Вам пригодятся: свечи, шары')
else:
    print('Загляните в хиты продаж!')
