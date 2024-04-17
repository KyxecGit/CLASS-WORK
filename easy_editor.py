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
#РАСПОЛОЖЕНИЕ
main_layout = QHBoxLayout()
line_files = QVBoxLayout()
line_image = QVBoxLayout()
line_files.addWidget(btn_folder)
line_files.addWidget(list_files)
line_image.addWidget(image)
main_layout.addLayout(line_files)
main_layout.addLayout(line_image)
#ЗАПУСК ПРИЛОЖЕНИЯ
win.setLayout(main_layout)
win.show()
app.exec()
