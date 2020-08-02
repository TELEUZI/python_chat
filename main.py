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
        self.view.ui.buttonBox.rejected.connect(self.model.exit)

    def show_main(self):
        self.view = MainWindow(self)
        self.view.show()
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.launch_receiving_thread)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.launch_sending_thread)
class Ctrl1:
    def __init__(self):
        self.view = EnterReg(self)
        self.model = Model(self)
        self.view.show()
        self.view.ui.pushButtonEnter.clicked.connect(self.n)
        self.view.ui.pushButtonReg.clicked.connect(self.z)

    def n(self):
        self.a = Ctrl()
        self.view.hide()

    def z(self):
        self.view = LoginForm(self)
        self.model = Model(self)
        self.view.show()
        self.view.ui.buttonBox.accepted.connect(self.model.sh)
        self.view.ui.buttonBox.rejected.connect(self.model.exit)
    def show_main(self):
        self.view = MainWindow(self)
        self.view.show()
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.launch_receiving_thread)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.launch_sending_thread)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = Ctrl1()
    sys.exit(app.exec_())
