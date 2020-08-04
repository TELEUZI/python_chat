# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QApplication

from model import Model
from view import LoginForm, MainWindow, EnterReg, Reg


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


class Controller:
    def __init__(self, view, model):
        self.model = model()
        self.view = view()
        self.view.show()

    def change_window(self, view):
        self.view.hide()
        self.view = view()
        self.view.show()

    def create_main(self):
        def launch_receiving_thread():
            nonlocal self
            self.receiving_messages = ReceivingNewMassagesThread(self.model, self.view)
            self.receiving_messages.start()

        def launch_sending_thread():
            nonlocal self
            self.sending_massages = SendingMassageThread(self.model, self.view.get_text())
            self.sending_massages.start_sending.connect(self.view.start_sending_message)
            self.sending_massages.end_sending.connect(self.view.end_sending_massage)
            self.sending_massages.start()

        self.change_window(MainWindow)
        self.view.ui.push_button.clicked.connect(launch_sending_thread)
        self.view.show_messages(self.model.get_messages())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(launch_receiving_thread)
        self.timer.start(5000)

    def create_login_form(self):
        def try_to_login():
            nonlocal self
            if self.model.check_password(self.view.get_username_password()):
                self.create_main()
            else:
                self.view.show_message_box()

        self.change_window(LoginForm)
        self.view.ui.buttonBox.accepted.connect(try_to_login)
        self.view.ui.buttonBox.rejected.connect(sys.exit)

    def create_reg_form(self):
        def try_to_reg():
            nonlocal self
            z = self.model.reg_new_user(self.view.get_username_password())
            if z[0]:
                self.create_main()
                self.view.good_reg("Благодарим за регистрацию!")
            else:
                self.view.show_message_box(z[1])

        self.change_window(Reg)
        self.view.ui.buttonBox.accepted.connect(try_to_reg)
        self.view.ui.buttonBox.rejected.connect(sys.exit)

    def create_reg_enter(self):
        self.view.ui.pushButtonEnter.clicked.connect(self.create_login_form)
        self.view.ui.pushButtonReg.clicked.connect(self.create_reg_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller(EnterReg, Model)
    controller.create_reg_enter()

    sys.exit(app.exec_())
