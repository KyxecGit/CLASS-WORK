from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

app = QApplication([])
#НАСТРОЙКИ ОКНА
win = QWidget()
win.setWindowTitle('Фотошоп на минималках')
win.resize(700,500)
#ИНТЕРФЕЙС
btn_folder = QPushButton('ПАПКА')
list_files = QListWidget()
image = QLabel('Картинка')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Отзеркалить')
btn_rezcost = QPushButton('Резкость')
btn_gray = QPushButton('Ч\Б')
#РАСПОЛОЖЕНИЕ
main_layout = QHBoxLayout()
line_files = QVBoxLayout()
line_image = QVBoxLayout()
line_editor = QHBoxLayout()
line_files.addWidget(btn_folder)
line_files.addWidget(list_files)
line_image.addWidget(image)
line_editor.addWidget(btn_left)
line_editor.addWidget(btn_right)
line_editor.addWidget(btn_mirror)
line_editor.addWidget(btn_rezcost)
line_editor.addWidget(btn_gray)
main_layout.addLayout(line_files)
main_layout.addLayout(line_image)
line_image.addLayout(line_editor)
#ЗАПУСК ПРИЛОЖЕНИЯ
win.setLayout(main_layout)
win.show()
app.exec()
