import sqlite3

question = [
('2 + 2 = 4 ?', 'Может быть', 'Однозачно', 'Для гениев'),
('Любишь маму ?', 'Да', 'Нет', 'Для гениев'),
('Кто ты из Гарри потера ?', 'Я не смотрю аниме', 'Хагрид', 'Для дотеров'),
('Можешь посмотреть в завтрашний день ?', 'Не только лишь каждый', 'Нет', 'Для дотеров'),
]
conn = sqlite3.connect('quiz.sqlite')
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE quiz_info (
                question VARCHAR,
                answer VARCHAR,
                wrong VARCHAR,
                quiz VARCHAR )       ''')
conn.commit()
