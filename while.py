
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



number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')
while number != 'off':
   if number == '1':
       preference = input('Введите предпочтение:')
       if preference == 'спорт':
           print('Подкаст Убойный спорт')
       else:
           print('Новый альбом Канье Уэста')
   elif number == '2':
       for i in range(1, 4):
           if input('Введите название группы') == 'Queen':
               print('Вы выиграли билет на концерт!')
               break
   number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')
