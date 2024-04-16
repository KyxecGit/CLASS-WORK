Ответы на задания

Задание 1. «Вложенность: задачи»
1.1. Правильные варианты ответов:


1.4. Программа после исправления ошибок:
feedback = input('Оставьте отзыв о путешествии:')
feedback = feedback.lower()
print('Длина отзыва:', len(feedback))
print('Поиск негатива:', feedback.find('ужасно'))

1.5. Программа после оптимизации:
price_human = int(input('Цена билета на самолёт:'))
price_luggage = int(input('Цена провоза багажа:'))
price_meal = int(input('Цена питания на борту:'))
total = price_human + price_luggage + price_meal
print('К оплате:', total)

1.6. Текст программы для оценки эффективности:
name = input('Имя стажёра')
tasks_main = int(input('Количество обязательных задач:'))
tasks_add = int(input('Количество дополнительных задач:'))
efficiency =  tasks_main*15 + tasks_add*20
print(name, '- эффективность', efficiency)

1.7. Текст программы для анализа отзывов:
feedback = input('Как тебе стажировка?')
feedback = feedback.lower()
print('Длина отзыва:', len(feedback))
print('Поиск недостатков:', feedback.find('скучно'))
print('Поиск достоинств:', feedback.find('круто'))






Доп задание 1.1. Правильное соответветствие:
	



Задание 2. «Отборочное задание»

2.1. Верно соответствие:


2.2. Заполненные пропуски:
	

2.5. Программа после исправления ошибок:
#Программа для печати стажёров, с которыми будет заключён договор
note = 'Варя, Миша и Стас отлично проявили себя на стажировке'
offer = note[0:4] + '/' + note[6:10] + '/' + note[13:17]
print('Выслать предложение о работе:', offer)

2.6. Программа после оптимизации (возможны другие варианты, при которых программа занимает столько же строк или меньше):
month_salary = int(input('Введите зарплату за месяц:'))
vacation = int(input('Введите количество дней отпуска:'))
daily_salary = month_salary/29.3 #среднее количество дней в месяце
vacation_pay = daily_salary*vacation
print('Примерные отпускные:', vacation_pay)


2.7. Программа для назначения премии:
salary = int(input('Зарплата за месяц:'))
extra_time = int(input('Количество отработанных в выходные часов:'))
bonus = salary*0.01*extra_time
print('Размер премии:', bonus)


Доп задание. 2.1:



Доп задание 2.2:
weekly_hours = int(input('Количество рабочих часов в неделю:'))
hour_salary = int(input('Желаемая зарплата за час:'))
month_salary = hour_salary * weekly_hours * 4
print('Выделить из бюджета:', month_salary)


Доп задание 2.4:
	
Дополнительное задание. «Стажировка: доп. задание»
1.1. Верные варианты ответов:
	


1.4. Код программы без ошибок:
#вычет государственного налога на доход
salary = int(input('Полная зарплата сотрудника:'))
tax = 0.13
tax = salary*tax
salary = salary - tax
print('Вычтено из зарплаты:', tax)
print('Сотрудник получит:', salary)


1.5. Возможное решение задачи:
#калькулятор трат
income = int(input('Введите доход за неделю:'))
expense_food = int(input('Потрачено на еду:'))
expense_clothes = int(input('Потрачено на одежду:'))
expense_other = int(input('Прочие траты:'))
rest = income - expense_clothes - expense_food - expense_other
print('У вас осталось:', rest)


