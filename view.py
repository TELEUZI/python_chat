from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget

from dialog import Ui_Form
from reg import Ui_RegForm
from reg_enter import UiForm
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
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
        for message in text:
            self.ui.massage_box.append(message)

    def show_new(self, text):
        for massage in text:
            self.ui.massage_box.append(massage)


class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Блэт, наконец-то!#2")

    def get_username_password(self):
        return self.ui.username_line_edit.text(), self.ui.password_line_edit.text()

    def show_unsuccessful_sign_in_message(self):
        self.message_box.setWindowTitle("Ошибка!")
        self.message_box.setText('Неправильный логин или пароль!')
        self.ui.message_box.show()


class EnterReg(QWidget):
    def __init__(self):
        super(EnterReg, self).__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Блэт, наконец-то!#3")


class Reg(QWidget):
    def __init__(self):
        super(Reg, self).__init__()
        self.ui = Ui_RegForm()
        self.ui.setupUi(self)

    def get_username_password(self):
        return self.ui.username_line_edit.text(), self.ui.password_line_edit.text(), self.ui.password_line_edit_2.text()

    def show_unsuccessful_sign_up_message(self, text):
        self.ui.message_box.setText(text)
        self.ui.message_box.setWindowTitle("Ошибка!")
        self.ui.message_box.show()

    def successful_sign_up_message(self, text):
        self.ui.message_box.setText(text)
        self.ui.message_box.setWindowTitle("Добро пожаловать в чат!")
        self.ui.message_box.show()
