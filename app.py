import sqlite3
db_name = 'quiz.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do_query(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    open()
    do_query('DROP TABLE IF EXISTS question')
    close()

def create_db():
    open()
    do_query("""
                CREATE TABLE question (
                question VARCHAR,
                answer VARCHAR,
                wrong1 VARCHAR,
                wrong2 VARCHAR,
                wrong3 VARCHAR,
                point INTEGER,
                quiz VARCHAR)
            """)
    close()

def add_question():
    questions = [
        ("Какой самый высокий горный пик в мире?", "Эверест", "Килиманджаро", "К2", "Аконкагуа", 5, "Горы мира"),
        ("Какое химическое обозначение у воды?", "H2O", "CO2", "NaCl", "HCl", 3, "Химия в повседневной жизни"),
        ("Какой год считается началом Великой Отечественной войны?", "1941", "1939", "1942", "1945", 10, "История России"),
        ("Кто написал произведение 'Преступление и наказание'?", "Федор Достоевский", "Лев Толстой", "Иван Тургенев", "Александр Пушкин", 7, "Русская литература"),
        ("Какой самый крупный океан на Земле?", "Тихий", "Атлантический", "Индийский", "Северный Ледовитый", 4, "Моря и океаны"),
        ("Сколько планет в Солнечной системе?", "8", "7", "9", "10", 6, "Космос и звезды")]

    open()
    cursor.executemany('''
    INSERT INTO question (question, answer, wrong1, wrong2,wrong3, point, quiz)
    VALUES ( ?,?,?,?,?,?,? )''', questions)
    conn.commit()
    close()
    
clear_db()
create_db()
add_question()










from flask import Flask, url_for, redirect
import sqlite3

def index():
    conn = sqlite3.connect('quiz.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT quiz FROM question')
    data = cursor.fetchall()
    result = '<h1> Список викторин </h1> <ol>'
    for quiz in data:
        result += '<li>' + quiz[0] + '</li>'
    result += '</ol>'
    return result

app = Flask(__name__)
app.add_url_rule('/','index', index)

app.run()
