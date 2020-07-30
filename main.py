# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore
from PySide2.QtCore import QUrl, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QDialogButtonBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QWidget
from dialog import Ui_Form
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QSound
import time


class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.show_main_window)
        self.ui.buttonBox.rejected.connect(self.exit)
        self.setWindowTitle("Блэт, наконец-то!#2")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timers)
        self.timer.start(5000)

    def show_main_window(self):
        self.new_win = MainWindow()
        self.new_win.show()
        self.hide()


    def timers(self):
        self.new_win.ui.receive_new()



    def exit(self):
        sys.exit()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Блэт, наконец-то запустилось!")
        self.ui.receiver()




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()

    sys.exit(app.exec_())

# a.setMedia(QMediaContent(QUrl.fromLocalFile()))
