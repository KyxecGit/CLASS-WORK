import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout,
    QFileDialog
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
#ФУНКЦИОНАЛ
class Editor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None

    def load_image(self,filename):
        self.filename = filename
        fullname = os.path.join(workdir,filename)
        self.image = Image.open(fullname)

    def show_image(self,dir):
        pixmap = QPixmap(dir)
        pixmap = pixmap.scaled(image.width(), image.height(), Qt.KeepAspectRatio)
        image.setPixmap(pixmap)
  
def show_file():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)
    list_files.clear()
    for file in files:
        for ext in ['.jpg','.png']:
            if file.endswith(ext):
                list_files.addItem(file)

def show_chosen_image():
    filename = list_files.currentItem().text()
    work_image.load_image(filename)
    work_image.show_image(os.path.join(workdir, work_image.filename))

work_image = Editor()
#ПОДПИСКИ
btn_folder.clicked.connect(show_file)
list_files.currentRowChanged.connect(show_chosen_image)
#ЗАПУСК ПРИЛОЖЕНИЯ
win.setLayout(main_layout)
win.show()
app.exec()
