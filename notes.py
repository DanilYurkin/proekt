import os
from pathlib import Path

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QPlainTextEdit)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


from add_note import Add_Note_Window
from Klient import Add_Note_Windoww
from pribil import Add_Note_Windowww
from stoinki import Add_Note_Windowwww

class Note_Window(QMainWindow):
    def __init__(self, email, name):
        super().__init__()
        self.email = email
        self.name = name
        self.notes_text = ""
        self.add_note_window = None
        #get notes
        #if Path("notes.txt").exists():
            #with open(Path("notes.txt"), 'r') as self.read_file:
                #self.read_file_data = self.read_file.read().replace('\n', '')
                #self.file_data = self.read_file_data.split(';;;;')
                #self.file_data = self.file_data[:-1]
                #self.length = len(self.file_data)
                #for self.counter_one in self.file_data:
                    #self.data_line_split = self.file_data[self.length-1].split(',,,,')
                        #self.counter_one.split(',,,,')
                    #self.notes_text = self.notes_text + self.data_line_split[0] + '\n' + self.data_line_split[1] + '\n\n\n'
                    #self.length = self.length - 1
                #if self.read_file_data.strip() == "":
                    #self.notes_text = "You have not created any notes"

        #else:
            #self.create_file = open("notes.txt", "w")
            #self.create_file.write("")
            #self.notes_text = "You have not created any notes"
        self.initUI()

    #set ui
    def initUI(self):
        self.setWindowTitle(self.name + "Главная страница")
        self.resize(1000, 500)
        self.setStyleSheet("background-color:#ffffff;")

        self.label = QLabel(self)
        self.label.setGeometry(30, 30, 500, 30)
        self.label.setText(self.name + "Главная страница")
        self.label.setStyleSheet("font-size:20px;")

        self.scroll = QScrollArea(self)
        self.scroll.setGeometry(16, 60, 530, 560)
        self.scroll.setStyleSheet("border: 0.5px solid #ffffff;")
        self.widget = QWidget(self)
        self.vbox = QVBoxLayout()
        # self.vbox.setGeometry(550, 500)



        object =  QtWidgets.QTextBrowser(self)
        object.setStyleSheet("background:#ffffff; border: 0px solid #fffff;font-size:16px; line-height:19px;")
        object.setStyleSheet("margin-right:25px;font-size:15px;")
        object.setText(self.notes_text)
        self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #scroll area properties
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)


        self.button_add = QPushButton("История", self)
        self.button_add.move(30, 100)
        self.button_add.resize(190, 40)
        self.button_add.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_add.clicked.connect(self.add_note_action)


        self.button_refresh = QPushButton("Клиент", self)
        self.button_refresh.move(30, 150)
        self.button_refresh.resize(190, 40)
        self.button_refresh.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_refresh.clicked.connect(self.ref_window)


        self.button_refresh = QPushButton("Прибыль", self)
        self.button_refresh.move(30, 200)
        self.button_refresh.resize(190, 40)
        self.button_refresh.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_refresh.clicked.connect(self.pribill)

        self.button_refresh = QPushButton("Стоянки", self)
        self.button_refresh.move(30, 250)
        self.button_refresh.resize(190, 40)
        self.button_refresh.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_refresh.clicked.connect(self.stoinkii)


#--------------------------------------------------------------------------------------------------Это были кнопки

        self.add_label = QLabel(self)
        self.add_label.move(250, 30)
        self.add_label.setText("Самокат")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(250, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Номер самоката")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()


        self.add_label = QLabel(self)
        self.add_label.move(400, 30)
        self.add_label.setText("Состояние")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(400, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Прокат/Стоянка")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()

        self.add_label = QLabel(self)
        self.add_label.move(550, 30)
        self.add_label.setText("Нахождение")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(550, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Клиент/Номер стоянки")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()

        self.add_label = QLabel(self)
        self.add_label.move(700, 30)
        self.add_label.setText("Тариф")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(700, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Тариф")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()

        self.add_label = QLabel(self)
        self.add_label.move(850, 30)
        self.add_label.setText("Заряд")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(850, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Заряд")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()


        self.show()

    def add_note_action(self):
        self.add_note_window = Add_Note_Window(self.email, self.name)
        self.add_note_window.show()


    def ref_window(self):
        #close old window and open a new window
        self.Klient = Add_Note_Windoww(self.email, self.name)
        #self.ref_window = Note_Window(self.email, self.name)
        self.Klient.show()


    def pribill(self):
        self.pribil = Add_Note_Windowww(self.email, self.name)
        self.pribil.show()


    def stoinkii(self):
        self.stoinki = Add_Note_Windowwww(self.email, self.name)
        self.stoinki.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Note_Window("","")
    window.show()
    app.exec_()


# This project was developed by Safat Jamil, email : safaetxamil@yahoo.com