# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import *
import requests
import time




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(829, 562)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(23, 27, 23, 25)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(25, -1, 25, -1)
        self.massage_box = QTextBrowser(MainWindow)
        self.massage_box.setObjectName(u"massage_box")
        sizePolicy.setHeightForWidth(self.massage_box.sizePolicy().hasHeightForWidth())
        self.massage_box.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.massage_box)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.text_edit = QTextEdit(MainWindow)
        self.text_edit.setObjectName(u"text_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_edit.sizePolicy().hasHeightForWidth())
        self.text_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.text_edit)

        self.push_button = QPushButton(MainWindow)
        self.push_button.setObjectName(u"push_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
        self.push_button.setSizePolicy(sizePolicy2)
        self.push_button.setFlat(False)





        self.horizontalLayout.addWidget(self.push_button)

        self.horizontalLayout.setStretch(0, 10)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.massage_box.setMarkdown("")
        self.text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u0442\u0435\u043a\u0441\u0442...", None))
        self.push_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.push_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        pass
    # retranslateUi