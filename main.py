# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore
from model import Model
from view import LoginForm, MainWindow, EnterReg
from PySide2.QtWidgets import QApplication


class Ctrl:
    def __init__(self):
        self.view = LoginForm(self)
        self.model = Model(self)
        self.view.show()
        self.view.ui.buttonBox.accepted.connect(self.model.show_main_window)
        self.view.ui.buttonBox.rejected.connect(sys.exit)

    def ssh(self):
        self.model.show_main_window()
    def show_main(self):
        self.view = MainWindow(self)
        self.view.show()
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.launch_receiving_thread)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.launch_sending_thread)
class Ctrl1:
    def __init__(self, view, model):
        self.view = view(self)
        self.model = model(self)
        self.view.show()
    def change_window(self, view):
        self.view = view

    def ssh(self):
        self.model.show_main_window()

    def n(self):
        self.a = Ctrl()
        self.view.hide()

    def z(self):
        self.view = LoginForm(self)
        self.model = Model(self)
        self.view.show()
    def show_main(self):
        self.view = MainWindow(self)
        self.view.show()
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.launch_receiving_thread)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.launch_sending_thread)
    def sh(self):
        self.view.hide()
        self.model.reg_new_user()
        self.show_main()
    @staticmethod
    def exit():
        sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Ctrl1(EnterReg, Model)
    sys.exit(app.exec_())
