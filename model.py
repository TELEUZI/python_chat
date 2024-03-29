import locale
from datetime import datetime

import requests
from PySide2.QtMultimedia import QSound

locale.setlocale(locale.LC_TIME, "ru")


class Model:
    def __init__(self):
        self.messages = requests.get("http://127.0.0.1:5000/view").json()["database"]

    def get_messages(self):
        return [f'{a["username"]}, {a["time"]}:\n{a["text"]}' for a in self.messages[-20:]]

    def receive_new(self):
        new = []
        self.new_messages = requests.get("http://127.0.0.1:5000/view").json()["database"]
        for i in range(-len(self.new_messages) + len(self.messages), 0):
            new.append(
                f'{self.new_messages[i]["username"]}, {self.new_messages[i]["time"]}:\n{self.new_messages[i]["text"]}')
            self.messages.extend(new)
            if self.username != self.new_messages[-1]["username"]:
                self.qq = QSound("youGotmail.wav")
                self.qq.play()

        return new

    def send_new_massage(self, text):
        requests.post("http://127.0.0.1:5000/send",
                      json={"username": self.username, "text": text, "time": datetime.now().strftime("%d %B %Y, %H:%M")})

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
            answer = a.json()['answer']
            return answer[0], answer[1]
        else:
            return False, 'Пароли не совпадают!'
