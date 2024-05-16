from random import randint

print('Здравствуйте меня зовут Генадий сегодня я буду вашим ботом')
print('1 - шутка 2 - рекомендация китайских мультиков')
print('3 - игра угадай число 4 - купить раба')

otvet = input('Что вас интересует?').lower()

while otvet.find('дос') == -1:

    if otvet.find('шут') >= 0 :
        print('Колобок повесился')
    elif otvet.find('ани') >= 0:
        otvet = input('Какой жанр вас интересует?')
        if otvet == 'комедия':
            print('ван панч мен \ ханакун \ волейбол')
        elif otvet == 'исекай':
            print('реинкарнация бомжика \ поднятия уровня \ какая то слизь ')
        else:
            print('Я не знаю такой жанр могу порекомендовать вам Атаку Титаника')
    elif otvet.find('игр') >= 0:
        print('Я загадал число от 1 до 100 посмотрим с какой попытки ты его угадаешь?)')
        rand_num = randint(0,100)
        otvet = int(input('Введите число:'))
        for popytka in range(10): 

            if otvet == rand_num:
                print('Приз пачка сухариков')
                break
            else:
                if otvet > rand_num:
                    print('Загадоное число меньше')
                else:
                    print('Загадоное число больше')

            otvet = int(input('Попробуй еще раз'))
        print('Вы угадали с',popytka + 1,'попытки')
    elif otvet.find('куп') >= 0:
        print('Добро пожаловать в Черно-Шоп')
        print('1 - Аркадий (100$) 2 - Виталя (200$) 3 - Лейкопластырь (1$)')
        money = int(input('Сколько у вас деняк?'))
        tovar = input('Что бы вы хотели приобрести?')
        if tovar == '1' and money >= 100:
            print('Вы купили Аркашу за 100 долларов')
            print('У вас осталось', money - 100)
        elif tovar == '2' and money >= 200:
            print('Вы купили Виталика за 200 долларов')
            print('У вас осталось', money - 200)
        elif tovar == '3':
            print('Вы купили лейкопластырь за бакс')
            print('У вас осталось', money - 1)
        else:
            print('У вас недостаточно деняк')    
    else:
        print('Я тоби не понимаю')

    otvet = input('Что нибудь еще?').lower()

print('Всего хорошего!!!')
















