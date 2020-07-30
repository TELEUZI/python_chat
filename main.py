# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore
from PySide2.QtCore import QUrl, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QDialogButtonBox

from client import LoginForm, MainWindow
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QWidget
from dialog import Ui_Form
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QSound
import time

class Ctrl():
    def show_main_window(self):
        self.new_win = MainWindow()
        self.new_win.show()
        window.hide()
    def exit(self):
        sys.exit()
a = Ctrl()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.ui.buttonBox.accepted.connect(a.show_main_window)
    window.ui.buttonBox.rejected.connect(a.exit)
    window.show()

    sys.exit(app.exec_())

# a.setMedia(QMediaContent(QUrl.fromLocalFile()))
