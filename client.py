import sys
import time

import requests
from PySide2 import QtCore
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import QWidget

from dialog import Ui_Form
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.push_button.clicked.connect(self.send_new_massage)
        self.setWindowTitle("Блэт, наконец-то запустилось!")
        self.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timers)
        self.timer.start(5000)

    def receiver(self):
        self.massages = requests.get("HTTP://127.0.0.1:5000/send").json()["massages_for_receiving"]
        for massage in self.massages:
            self.ui.massage_box.append(f'{massage["username"]}, {massage["text"]}, {massage["time"]}')

    def receive_new(self):
        self.new_massages = requests.get("HTTP://127.0.0.1:5000/send").json()["massages_for_receiving"]
        for i in range(-len(self.new_massages)+len(self.massages), 0):
            self.ui.massage_box.append(f'{self.new_massages[i]["username"]}, {self.new_massages[i]["text"]}, {self.new_massages[i]["time"]}')
            if self.text != self.new_massages[i]["text"]:
                self.qq = QSound("youGotmail.wav")
                self.qq.play()
            self.massages.append([{self.new_massages[i]["username"]}, {self.new_massages[i]["text"]}, {self.new_massages[i]["time"]}])

    def send_new_massage(self):
        self.text = self.ui.text_edit.toPlainText()
        requests.post("http://127.0.0.1:5000/send", json={"username": "username", "text": self.text, "time": time.ctime()})
        self.ui.text_edit.setText("")
    def timers(self):
        self.receive_new()


class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Блэт, наконец-то!#2")






