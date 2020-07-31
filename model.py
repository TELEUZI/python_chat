import sys
import time

import requests
from PySide2.QtMultimedia import QSound


class Model():
    def __init__(self, controller):
        self.controller = controller
    def receiver(self):
        self.massages = requests.get("https://a4d46fceca38.ngrok.io/send").json()["massages_for_receiving"]
        for massage in self.massages:
            self.controller.view.ui.massage_box.append(f'{massage["username"]}, {massage["text"]}, {massage["time"]}')


    def receive_new(self):
        self.new_massages = requests.get("https://a4d46fceca38.ngrok.io/send").json()["massages_for_receiving"]
        for i in range(-len(self.new_massages) + len(self.massages), 0):
            self.controller.view.ui.massage_box.append(
                f'{self.new_massages[i]["username"]}, {self.new_massages[i]["text"]}, {self.new_massages[i]["time"]}')
            if self.text != self.new_massages[i]["text"]:
                self.qq = QSound("youGotmail.wav")
                self.qq.play()
            self.massages.append(
                [{self.new_massages[i]["username"]}, {self.new_massages[i]["text"]}, {self.new_massages[i]["time"]}])


    def send_new_massage(self):
        self.text = self.controller.view.ui.text_edit.toPlainText()
        requests.post("https://a4d46fceca38.ngrok.io/send", json={"username": "username", "text": self.text, "time": time.ctime()})
        self.controller.view.ui.text_edit.setText("")


    def timers(self):
        self.receive_new()

    def show_main_window(self):
        self.controller.view.hide()
        self.controller.show_main()
        self.controller.view.show()

    def exit(self):
        sys.exit()