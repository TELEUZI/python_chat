# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg_enter.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonEnter = QPushButton(Form)
        self.pushButtonEnter.setObjectName(u"pushButtonEnter")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEnter.sizePolicy().hasHeightForWidth())
        self.pushButtonEnter.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(10)
        self.pushButtonEnter.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonEnter)

        self.pushButtonReg = QPushButton(Form)
        self.pushButtonReg.setObjectName(u"pushButtonReg")
        sizePolicy.setHeightForWidth(self.pushButtonReg.sizePolicy().hasHeightForWidth())
        self.pushButtonReg.setSizePolicy(sizePolicy)
        self.pushButtonReg.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonReg)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c. \u0421\u043d\u043e\u0432\u0430.", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u043e\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435.", None))
        self.pushButtonEnter.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButtonReg.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

