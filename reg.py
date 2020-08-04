# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_RegForm(object):
    def setupUi(self, RegForm):
        if not RegForm.objectName():
            RegForm.setObjectName(u"RegForm")
        RegForm.resize(491, 290)
        self.verticalLayout_2 = QVBoxLayout(RegForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username_label = QLabel(RegForm)
        self.username_label.setObjectName(u"username_label")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(9)
        self.username_label.setFont(font)
        self.username_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.username_label)

        self.username_line_edit = QLineEdit(RegForm)
        self.username_line_edit.setObjectName(u"username_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_line_edit.sizePolicy().hasHeightForWidth())
        self.username_line_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.username_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 12, -1, 0)
        self.password_label = QLabel(RegForm)
        self.password_label.setObjectName(u"password_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy1)
        self.password_label.setFont(font)
        self.password_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.password_label)

        self.password_line_edit_2 = QLineEdit(RegForm)
        self.password_line_edit_2.setObjectName(u"password_line_edit_2")
        sizePolicy.setHeightForWidth(self.password_line_edit_2.sizePolicy().hasHeightForWidth())
        self.password_line_edit_2.setSizePolicy(sizePolicy)
        self.password_line_edit_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.password_line_edit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 12, -1, -1)
        self.password_label_2 = QLabel(RegForm)
        self.password_label_2.setObjectName(u"password_label_2")
        sizePolicy1.setHeightForWidth(self.password_label_2.sizePolicy().hasHeightForWidth())
        self.password_label_2.setSizePolicy(sizePolicy1)
        self.password_label_2.setFont(font)
        self.password_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.password_label_2)

        self.password_line_edit = QLineEdit(RegForm)
        self.password_line_edit.setObjectName(u"password_line_edit")
        sizePolicy.setHeightForWidth(self.password_line_edit.sizePolicy().hasHeightForWidth())
        self.password_line_edit.setSizePolicy(sizePolicy)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.password_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(RegForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(RegForm)

        QMetaObject.connectSlotsByName(RegForm)
    # setupUi

    def retranslateUi(self, RegForm):
        RegForm.setWindowTitle(QCoreApplication.translate("RegForm", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("RegForm", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_label.setText(QCoreApplication.translate("RegForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_label_2.setText(QCoreApplication.translate("RegForm", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

