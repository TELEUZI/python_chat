# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QColor

from model import Model
from view import LoginForm, MainWindow, EnterReg, Reg
from PySide2.QtWidgets import QApplication


class ReceivingNewMassagesThread(QThread):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view

    def run(self):
        self.view.show_new(self.model.receive_new())


class SendingMassageThread(QThread):
    start_sending = Signal()
    end_sending = Signal()

    def __init__(self, model, text):
        super().__init__()
        self.model = model
        self.text = text

    def run(self):
        self.start_sending.emit()
        self.model.send_new_massage(self.text)
        self.end_sending.emit()


class Ctrl1:
    def __init__(self, view, model):
        self.view = view()
        self.model = model()
        self.view.show()

    def change_window(self, view):
        self.view.hide()
        self.view = view()
        self.view.show()

    def launch_receiving_thread(self):
        self.receiving_messages = ReceivingNewMassagesThread(self.model, self.view)
        self.receiving_messages.start()

    def launch_sending_thread(self):
        self.sending_massages = SendingMassageThread(self.model, self.view.get_text())
        self.sending_massages.start_sending.connect(self.view.start_sending_message)
        self.sending_massages.end_sending.connect(self.view.end_sending_massage)
        self.sending_massages.start()

    def create_main(self):
        self.change_window(MainWindow)
        self.view.ui.push_button.clicked.connect(self.launch_sending_thread)
        self.view.show_messages(self.model.receiver())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.launch_receiving_thread)
        self.timer.start(5000)

    def create_login_form(self):
        self.change_window(LoginForm)
        self.view.ui.buttonBox.accepted.connect(self.try_to_login)
        self.view.ui.buttonBox.rejected.connect(sys.exit)

    def create_reg_form(self):
        self.change_window(Reg)
        self.view.ui.buttonBox.accepted.connect(self.try_to_reg)
        self.view.ui.buttonBox.rejected.connect(sys.exit)

    def try_to_reg(self):
        z = self.model.reg_new_user(self.view.get_username_password())
        if z[0]:
            self.create_main()
        else:
            self.view.show_message_box(z[1])

    def try_to_login(self):
        if self.model.check_password(self.view.get_username_password()):
            self.create_main()
        else:
            self.view.show_message_box()

    @staticmethod
    def exit():
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Ctrl1(EnterReg, Model)
    r.view.ui.pushButtonEnter.clicked.connect(r.create_login_form)
    r.view.ui.pushButtonReg.clicked.connect(r.create_reg_form)

    sys.exit(app.exec_())
