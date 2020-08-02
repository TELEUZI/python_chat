import sys

from PySide2.QtWidgets import QWidget
from dialog import Ui_Form
from ui_mainwindow import Ui_MainWindow
from reg_enter import UiForm


class MainWindow(QWidget):
    def __init__(self, ctrl):
        super(MainWindow, self).__init__()
        self.ctrl = ctrl
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class LoginForm(QWidget):
    def __init__(self, ctrl):
        super(LoginForm, self).__init__()
        self.ctrl = ctrl
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.ctrl.ssh)
        self.ui.buttonBox.rejected.connect(sys.exit)
        self.setWindowTitle("Блэт, наконец-то!#2")


class EnterReg(QWidget):
    def __init__(self, ctrl):
        super(EnterReg, self).__init__()
        self.ctrl = ctrl
        self.ui = UiForm()
        self.ui.setupUi(self)
        self.ui.pushButtonEnter.clicked.connect(self.ctrl.n)
        self.ui.pushButtonReg.clicked.connect(self.ctrl.z)
        self.setWindowTitle("Блэт, наконец-то!#3")
