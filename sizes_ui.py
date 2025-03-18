# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sizes_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Size(object):
    def setupUi(self, Size):
        if not Size.objectName():
            Size.setObjectName(u"Size")
        Size.resize(840, 700)
        Size.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.push_prev = QPushButton(Size)
        self.push_prev.setObjectName(u"push_prev")
        self.push_prev.setGeometry(QRect(290, 650, 121, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.push_prev.setFont(font)
        self.push_prev.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_prev.setCheckable(False)
        self.push_next = QPushButton(Size)
        self.push_next.setObjectName(u"push_next")
        self.push_next.setGeometry(QRect(430, 650, 121, 21))
        self.push_next.setFont(font)
        self.push_next.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_next.setCheckable(False)
        self.push_back = QPushButton(Size)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 670, 121, 21))
        self.push_back.setFont(font)
        self.push_back.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_back.setCheckable(False)
        self.widget = QWidget(Size)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 820, 630))
        self.widget.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px\n"
"")

        self.retranslateUi(Size)

        QMetaObject.connectSlotsByName(Size)
    # setupUi

    def retranslateUi(self, Size):
        Size.setWindowTitle(QCoreApplication.translate("Size", u"Form", None))
        self.push_prev.setText(QCoreApplication.translate("Size", u"Previous page", None))
        self.push_next.setText(QCoreApplication.translate("Size", u"Next page", None))
        self.push_back.setText(QCoreApplication.translate("Size", u"Close", None))
    # retranslateUi

