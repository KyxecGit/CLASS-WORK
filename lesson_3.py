Ответы на задания

Задание 1. «Подсолнухи: обратная связь»
1.1. Правильные варианты ответов:


1.4. Программа после исправления ошибок:
feedback = input('Оставьте отзыв о путешествии:')
length = len(feedback)
print('Спасибо за подробный отзыв! В нём целых', length, 'символов!')

1.5. Программа после исправления ошибок:
feedback = 'Корпуcа 2, 7 и 9 - самые уютные! Если выберете этот отель, то останавливайтесь в них'
building1 = feedback[8]
building2 = feedback[11]
building3 = feedback[15]
print('Клиенты выбирают корпуса:', building1, building2, building3)

1.6. Программа после исправления ошибок:
feedback = 'Вид на море - это фишка отеля!'
feedback_advert = feedback[0:11]
print('Нашим клиентам нравится:', feedback_advert)


1.7. Текст программы для поиска любимых блюд:
dishes = input('Введите любимые блюда ресторана "Подсолнух":')
searching1 = 'шоколадный торт'
searching2 = 'шашлык'
result1 = dishes.find(searching1)
result2 = dishes.find(searching2)
print(searching1, result1)
print(searching2, result2)

1.8. Текст программы для поиска слов:
feedback = 'Волшебный Отель с супер ресторанами. Лучший на Кипре. Качественная еда, большое разнообразие. Прекрасный пляж и сервис. Чистые и просторные номера! Всё на пять! Японская кухня оставляет приятное впечатление. Всегда, приезжая в Лимассол, заказываем суши и роллы. Мимо витрины со сладким очень сложно пройти не остановившись, хотя бы посмотреть. Тихий район - это круто!'
searching1 = 'тихий район'
searching2 = 'вкусно'
feedback = feedback.lower()
result1 = feedback.find(searching1)
result2 = feedback.find(searching2)
print(searching1, result1)
print(searching2, result2)

Доп задание 1.1. Правильное соответветствие:
	

Доп задание 1.2
feedback = 'В Подсолнухах мне больше всего понравился заботливый персонал'
end = len(feedback)
start = end - len('заботливый персонал')
service = feedback[start:end]
print(service)


Доп задание 1.4



Задание 2. «Подсолнухи: обратная связь 2»

2.1. Верны следующие варианты ответов:


2.2. Варианты соответствуют категориям:
	


2.5. Программа после исправления ошибок:
city = input('Введите город:')
district = input('Введите район:')
rating = input('Введите рейтинг:')
searching = city + '/' + district + '/' + rating
print('Запрос',  searching,'сформирован')

2.6. Программа после исправления ошибок:
id_number = 12451512
surname = 'Степашин'
tour = 'Занзибар'
client_data = str(id_number) + '/' + surname + '/' + tour
print('Информация о клиенте:',client_data)


2.7. Программа для назначения премии:
feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
worker1 = feedback[0:5]
worker2 = feedback[8:12]
workers = worker1 + '/' + worker2
print('Назначить премию:', workers)


2.8. Программа для сбора обратной связи:
rating = input('На сколько вы оцениваете отдых от 1 до 5:')
feedback = input('Что вам не понравилось?')
total = rating + '-' + feedback
print(total)


Доп задание. 2.1:

Доп задание 2.2:
	


Доп задание 2.3:
feedback1 = input('Напишите подробный отзыв:')
feedback2 = input('Что вам понравилось:')
feedback3 = input('Что вам НЕ понравилось:')
length1 = len(feedback1)
length2 = len(feedback2)
length3 = len(feedback3)
sale = (length1 + length2 + length3)*0.1
print('Спасибо! Ваша скидка:', sale)


Дополнительное задание. «Подсолнухи: доп задание»
1.1. Верные варианты ответов:



1.2. Верный порядок команд:
	


1.5. Код программы:
searching1 = 'весело'
searching2 = 'увлекательно'
searching3 = 'развлечения'
feedback = input('Оцените развлекательный комплекс:')
feedback = feedback.lower()
result1 = feedback.find('весело')
result2 = feedback.find('увлекательно')
result3 = feedback.find('развлечения')
print('Результат анализа:', result1, result2, result3)
