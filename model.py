import locale
import sys
import time

import requests
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QColor
from PySide2.QtMultimedia import QSound
from datetime import datetime
locale.setlocale(locale.LC_TIME, "ru")


class Model:
    def __init__(self):
        self.massages = requests.get("http://127.0.0.1:5000/view").json()["database"]

    def receiver(self):
        return self.massages

    def receive_new(self):
        new = []
        self.new_massages = requests.get("http://127.0.0.1:5000/view").json()["database"]
        for i in range(-len(self.new_massages) + len(self.massages), 0):
            new.append(
                f'{self.new_massages[i]["username"]}, {self.new_massages[i]["time"]}:\n{self.new_massages[i]["text"]}')
            if self.username != self.new_massages[i]["username"]:
                self.qq = QSound("youGotmail.wav")
                self.qq.play()
            self.massages.extend(new)
        return new

    def send_new_massage(self, text):
        requests.post("http://127.0.0.1:5000/send",
                      json={"username": self.username, "text": text, "time": datetime.now().strftime("%d_%B_%Y_%H.%M")})

    def check_password(self, username_password):
        self.username = username_password[0]
        a = requests.post("http://127.0.0.1:5000/checkpass",
                          json={"username": self.username, "text": username_password[1]})
        return a.json()['answer']

    def reg_new_user(self, username_password):
        if username_password[1] == username_password[2]:
            self.username = username_password[0]
            a = requests.post("http://127.0.0.1:5000/reg_user",
                              json={"username": self.username, "text": username_password[1]})
            return a.json()['answer'],
        else:
            return False, 'Пароли не совпадают!'
