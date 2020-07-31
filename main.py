# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore
from PySide2.QtCore import QUrl, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QDialogButtonBox
from model import Model
from view import LoginForm, MainWindow
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QWidget
from dialog import Ui_Form
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QSound
import time

class Ctrl():
    def __init__(self):
        self.view = LoginForm(self)
        self.model = Model(self)
        self.view.show()
        self.view.ui.buttonBox.accepted.connect(self.model.show_main_window)
        self.view.ui.buttonBox.rejected.connect(self.model.exit)

    def show_main(self):
        self.view = MainWindow(self)
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.timers)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.send_new_massage)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Ctrl()

    sys.exit(app.exec_())

# a.setMedia(QMediaContent(QUrl.fromLocalFile()))
