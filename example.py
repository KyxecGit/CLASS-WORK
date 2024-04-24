from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLineEdit, QPushButton,
    QLabel, QVBoxLayout)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Калькулятор ИМТ')
window.resize(400,200)

result = QLabel('Введите ваши данные: ')
weight = QLineEdit()
weight.setPlaceholderText('Введите ваш вес: ')
height = QLineEdit()
height.setPlaceholderText('Введите ваш рост: ')
button = QPushButton('Расчитать')

layout = QVBoxLayout()
layout.addWidget(result)
layout.addWidget(weight)
layout.addWidget(height)
layout.addWidget(button)

def show_result():
    ves = weight.text()
    rost = height.text()
    try:
        res = int(ves) / float(rost)**2
        if res < 25:
            result.setText('Ваш вес в пределах нормы')
        else:
            result.setText('У вас избыточный вес')
    except:
        result.setText('Вам нужно ввести цифры!')

button.clicked.connect(show_result)

window.setLayout(layout)
window.show()
app.exec()
