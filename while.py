
#Первые 3 покупателя получают скидку
count = 0
while count < 3:
    card = input('Введите номер карты:')
    print('Поздравляем! Вы получили скидку 10%.')
    count +=  1

print('Скидки закончились.')


#Подсчёт категорий товаров
category = input('Категория (end - завершить):')
count = 0
while category != 'end':
    category = input('Категория (end - завершить):')
    count += 1

print('Всего категорий товаров:', count)
