def get_course(wish):
    if wish.find('спорт') != -1:
        course = 'волейбол'
    elif wish.find('наука') != -1:
        course = 'астрономия'
    elif wish.find('комиксы') != -1:
        course = 'скетчинг'
    else:
        course = 'история Древнего Рима'
    return course

amount = int(input('Число учеников:'))
for i in range(amount):
    wish = input('Введите предпочтение:')
    res = get_course(wish) 
    print('Рекомендация:', res)
    if res == 'астрономия':
        print('Будьте внимательны! Занятия проходят ночью!')







def check_test(score):
    if score > 50:
        return True
    else:
        return False

amount = int(input('Число учеников:'))
for i in range(amount):
    score = int(input('Введите балл:'))
    res = check_test(score) 
    print('Допуск:', res)
    if res == False:
        print('Займитесь чтением! Отличные книги: Три толстяка, Дон Кихот и Робинзон Крузо')
