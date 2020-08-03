import sys

from PySide2.QtGui import QColor

from PySide2.QtWidgets import QWidget
from dialog import Ui_Form
from ui_mainwindow import Ui_MainWindow
from reg_enter import UiForm
from reg import Ui_RegForm


class MainWindow(QWidget):
    def __init__(self, ctrl):
        super(MainWindow, self).__init__()
        self.ctrl = ctrl
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def get_text(self):
        return self.ui.text_edit.toPlainText()

    def start_sending_message(self):
        self.ui.push_button.setEnabled(False)
        self.ui.text_edit.setTextColor(QColor('#808080'))
        self.ui.text_edit.setText("Отправка сообщения...")

    def end_sending_massage(self):
        self.ui.text_edit.setText("")
        self.ui.text_edit.setTextColor(QColor('#000000'))
        self.ui.push_button.setEnabled(True)

    def show_messages(self, text):
        for massage in text:
            self.ui.massage_box.append(f'{massage["username"]}, {massage["text"]}, {massage["time"]}')


class LoginForm(QWidget):
    def __init__(self, ctrl):
        super(LoginForm, self).__init__()
        self.ctrl = ctrl
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Блэт, наконец-то!#2")

    def get_username_password(self):
        return self.ui.username_line_edit.text(), self.ui.password_line_edit.text()

    def show_message_box(self):
        self.ui.message_box.show()


class EnterReg(QWidget):
    def __init__(self, ctrl):
        super(EnterReg, self).__init__()
        self.ctrl = ctrl
        self.ui = UiForm()
        self.ui.setupUi(self)

        self.setWindowTitle("Блэт, наконец-то!#3")

    def enterchoise(self):
        return True


class Reg(QWidget):
    def __init__(self, ctrl):
        super(Reg, self).__init__()
        self.ctrl = ctrl
        self.ui = Ui_RegForm()
        self.ui.setupUi(self)

    def get_username_password(self):
        return self.ui.username_line_edit.text(), self.ui.password_line_edit.text()
