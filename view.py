import sys
import time

import requests
from PySide2 import QtCore
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import QWidget

from dialog import Ui_Form
from ui_mainwindow import Ui_MainWindow


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
        self.setWindowTitle("Блэт, наконец-то!#2")






