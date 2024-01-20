import sys
from datetime import date

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow, \
    QPlainTextEdit
# from PyQt5.QtGui import QIcon
# from PyQt5.uic.properties import QtWidgets, QtCore, QtGui
from pathlib import Path

#from notes import Note_Window


class Add_Note_Windowww(QMainWindow):
    def __init__(self, email, name):
        super().__init__()
        self.email = email
        self.name = name
        self.today = date.today()
        self.date_format = self.today.strftime("%B %d, %Y")
        # window properties
        self.note_window = None

        self.setWindowTitle("Прибыль")
        self.resize(1000, 500)
        self.setStyleSheet("background-color: #ffffff;")


        self.add_label = QLabel(self)
        self.add_label.move(100, 30)
        self.add_label.setText("Прибыль")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(100, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Прибыль")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()


        self.add_label = QLabel(self)
        self.add_label.move(250, 30)
        self.add_label.setText("Промежуток времени")
        self.add_label.setStyleSheet("font-size:24px")

        self.text_input = QPlainTextEdit(self)
        self.text_input.move(250, 80)
        self.text_input.resize(100, 300)
        self.text_input.setPlaceholderText("Промежуток времени")
        self.text_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:16px;")
        self.text_input.setFocus()


        self.button_1 = QPushButton("Назззад", self) #действует как add пока что
        self.button_1.move(100, 400)
        self.button_1.resize(190, 40)
        self.button_1.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_1.clicked.connect(self.close)

        self.alert_message = QMessageBox()

    def create_note_action(self):
        if Path("notes.txt").exists():
            self.note_value = self.text_input.toPlainText()
            self.note_value = self.note_value.strip()
            if self.note_value == "":
                self.alert_message.setText("Please enter something")
                self.alert_message.setWindowTitle("Error")
                self.alert_message.exec()
            else:
                self.append_file = open('notes.txt', 'a')
                self.append_file.write(
                    self.note_value + ',,,,' + self.date_format + ';;;;')
                self.append_file.close()
                self.alert_message.setText("Your note has been added. Please click the refresh button.")
                self.alert_message.setWindowTitle("Success")
                self.alert_message.exec()
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Add_Note_Windowww("f", "g")
    app.exec_()
