Ответы на задания

Задание 1. «Турфирма: вычисления»
1.1. Правильные варианты ответов:


1.4. Программа после исправления ошибок:
surname = 'Иванов'
people_amount = 24
ticket_price = 2450
total = people_amount*ticket_price
print('Экскурсовод -', surname)
print('Стоимость пакета:', total)

1.5. Программа после исправления ошибок:
adults = 2
children = 31
adult_price = 3699
child_price = 1100
total = adults*adult_price + children*child_price
print('Полная стоимость:', total)

1.6. Текст программы для подсчёта страховых услуг:
luggage = 890
transport = 875
health = 1345
passport = 2199
total = (luggage+transport+health+passport)*3
print('Стоимость страхования семьи:', total)

1.7. Текст программы стоимости горящего тура:
price = 56720
new_price = price*0.65
print('Стоимость горящего тура:', new_price)

Доп задание 1.1.
 

Доп задание 1.2
price1 = 2100
price2 = 2850
total = price1*4 + price2*5
print(total)


Доп задание 1.4



Задание 2. «Турфирма: оптимизация»

2.1. Верны следующие варианты ответов:


2.4. Программа после исправления ошибок:
surname = input('Введите фамилию:')
country = input('Введите страну отдыха:')
season = input('Введите время года: ')
print('Запрос -', surname, country, season, '- отправлен')

2.5. Программа после исправления ошибок:
price_hotel = input('Введите стоимость одной ночи в отеле:')
price_hotel = int(price_hotel)
days = input('Введите количество дней отдыха:')
days = int(days)
total = price_hotel*days
print('Стоимость отдыха:', total)


2.6. Программа для списания бонусов:
price = input('Введите цену билета:')
price = int(price)
bonus = input('Введите бонусы для списания:')
bonus = int(bonus)
price = price-bonus
print('Цена со скидкой:', price)

2.7. Программа для автоматической рассылки:
name = input('Имя клиента:')
tours = input('Количество купленных путёвок:')
sale = input('Предлагаемая путёвка:')
print('Здравствуйте,', name)
print('Вы путешествовали с нами уже', tours, 'раз(а)! Хотите снова?')
print('Наша турфирма проводит распродажу. Тур в', sale, 'со скидкой 50%!')


Доп задание. 2.1:

Доп задание 2.2:
price = input('Введите стоимость путёвки')
price = int(price)
cash = price*0.05
print('Вам начислен кэшбек в размере', cash)


Доп задание 2.4:



Дополнительное задание. «Турфирма: доп задание»
1.1. Верные варианты ответов:

1.4. Код программы без ошибок:
surname = input('Имя')
date = input('Дата рождения')
index = input('Персональный номер')
index = int(index)
print('Клиент добавлен в базу')


1.5. Код программы:
mass1 = input('Вес чемодана')
mass1 = int(mass1)
mass2 = input('Вес ручной клади')
mass2 = int(mass2)
mass3 = input('Вес доп. предметов ручной клади')
mass3 = int(mass3)
total = mass1 + mass2 + mass3
print('Общий вес багажа:', total)


1.6. Код программы:
change = input('Введите сумму:')
change = int(change)
rub1 = change%10
change = change//10
rub10 = change%10
change = change//10
rub100 = change%10




change = change//10
rub1000 = change
print(rub1, '- по 1р')
print(rub10, '- по 10р')
print(rub100, '- по 100р')
print(rub1000, '- по 1000р')
