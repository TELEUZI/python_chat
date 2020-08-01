import sys
import time
import requests
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QColor
from PySide2.QtMultimedia import QSound
from server.models import check_users_password


class ReceivingNewMassagesThread(QThread):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        self.model.receive_new()


class SendingMassageThread(QThread):
    start_sending = Signal()
    end_sending = Signal()

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        self.start_sending.emit()
        self.model.send_new_massage()
        self.end_sending.emit()


class Model:
    def __init__(self, controller):
        self.controller = controller

    def launch_receiving_thread(self):
        self.receiving_messages = ReceivingNewMassagesThread(self)
        self.receiving_messages.start()

    def launch_sending_thread(self):
        self.sending_massages = SendingMassageThread(self)
        self.sending_massages.start_sending.connect(self.start_sending_message)
        self.sending_massages.end_sending.connect(self.end_sending_massage)
        self.sending_massages.start()
        self.controller.view.ui.push_button.setEnabled(False)

    def start_sending_message(self):
        self.controller.view.ui.text_edit.setTextColor(QColor('#808080'))
        self.controller.view.ui.text_edit.setText("Отправка сообщения...")

    def end_sending_massage(self):
        self.controller.view.ui.text_edit.setText("")
        self.controller.view.ui.text_edit.setTextColor(QColor('#000000'))
        self.controller.view.ui.push_button.setEnabled(True)

    def receiver(self):
        self.massages = requests.get("http://127.0.0.1:5000/view").json()["database"]
        for massage in self.massages:
            self.controller.view.ui.massage_box.append(f'{massage["username"]}, {massage["text"]}, {massage["time"]}')

    def receive_new(self):
        self.new_massages = requests.get("http://127.0.0.1:5000/view").json()["database"]
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
        requests.post("http://127.0.0.1:5000/send",
                      json={"username": "username", "text": self.text, "time": time.ctime()})
    def check_password(self):
        username = self.controller.view.ui.username_line_edit.text()
        password = self.controller.view.ui.password_line_edit.text()
        a = requests.post("http://127.0.0.1:5000/checkpass",
                          json={"username": username, "text": password})
        return a.json()['answer']

    def show_main_window(self):
        if self.check_password():
            self.controller.view.hide()
            self.controller.show_main()
        else:
            self.controller.view.ui.message_box.show()

    @staticmethod
    def exit():
        sys.exit()
