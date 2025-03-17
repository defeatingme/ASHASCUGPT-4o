# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(720, 480)
        Home.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.label_instructor = QLabel(Home)
        self.label_instructor.setObjectName(u"label_instructor")
        self.label_instructor.setGeometry(QRect(0, 20, 721, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_instructor.setFont(font)
        self.label_instructor.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 8px")
        self.label_department = QLabel(Home)
        self.label_department.setObjectName(u"label_department")
        self.label_department.setGeometry(QRect(0, 60, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_department.setFont(font1)
        self.label_department.setStyleSheet(u"background-color: rgb(160, 160, 160);\n"
"color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 4px;\n"
"")
        self.label_department.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_department.setOpenExternalLinks(True)
        self.push_exit = QPushButton(Home)
        self.push_exit.setObjectName(u"push_exit")
        self.push_exit.setGeometry(QRect(10, 450, 121, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.push_exit.setFont(font2)
        self.push_exit.setStyleSheet(u"QPushButton {\n"
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
        self.push_exit.setCheckable(False)
        self.push_logout = QPushButton(Home)
        self.push_logout.setObjectName(u"push_logout")
        self.push_logout.setGeometry(QRect(140, 450, 121, 21))
        self.push_logout.setFont(font2)
        self.push_logout.setStyleSheet(u"QPushButton {\n"
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
        self.push_logout.setCheckable(False)
        self.label_name = QLabel(Home)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(360, 0, 351, 21))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label_name.setFont(font3)
        self.label_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_sessions = QFrame(Home)
        self.frame_sessions.setObjectName(u"frame_sessions")
        self.frame_sessions.setGeometry(QRect(10, 100, 701, 321))
        self.frame_sessions.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 2px")
        self.frame_sessions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sessions.setFrameShadow(QFrame.Shadow.Raised)
        self.table_sessions = QTableWidget(self.frame_sessions)
        self.table_sessions.setObjectName(u"table_sessions")
        self.table_sessions.setGeometry(QRect(0, 20, 701, 241))
        self.table_sessions.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 2px")
        self.frame_buttons = QFrame(self.frame_sessions)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(0, 280, 701, 41))
        self.frame_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.push_reload = QPushButton(self.frame_buttons)
        self.push_reload.setObjectName(u"push_reload")
        self.push_reload.setGeometry(QRect(190, 10, 121, 21))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.push_reload.setFont(font4)
        self.push_reload.setStyleSheet(u"QPushButton {\n"
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
        self.push_reload.setCheckable(False)
        self.push_continue = QPushButton(self.frame_buttons)
        self.push_continue.setObjectName(u"push_continue")
        self.push_continue.setGeometry(QRect(320, 10, 121, 21))
        self.push_continue.setFont(font4)
        self.push_continue.setStyleSheet(u"QPushButton {\n"
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
        self.push_continue.setCheckable(False)
        self.push_delete = QPushButton(self.frame_buttons)
        self.push_delete.setObjectName(u"push_delete")
        self.push_delete.setGeometry(QRect(10, 10, 121, 21))
        self.push_delete.setFont(font4)
        self.push_delete.setStyleSheet(u"QPushButton {\n"
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
        self.push_delete.setCheckable(False)
        self.push_create = QPushButton(self.frame_buttons)
        self.push_create.setObjectName(u"push_create")
        self.push_create.setGeometry(QRect(450, 10, 241, 21))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.push_create.setFont(font5)
        self.push_create.setStyleSheet(u"QPushButton {\n"
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
        self.push_create.setCheckable(False)
        self.label_submit = QLabel(self.frame_sessions)
        self.label_submit.setObjectName(u"label_submit")
        self.label_submit.setGeometry(QRect(0, 0, 701, 21))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setUnderline(False)
        self.label_submit.setFont(font6)
        self.label_submit.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_submit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_note = QLabel(self.frame_sessions)
        self.label_note.setObjectName(u"label_note")
        self.label_note.setGeometry(QRect(10, 260, 681, 21))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setUnderline(False)
        self.label_note.setFont(font7)
        self.label_note.setStyleSheet(u"background-color: None;\n"
"color: rgb(208, 172, 220);\n"
"border: None;")
        self.label_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.label_instructor.setText(QCoreApplication.translate("Home", u"Welcome, Anonymous!", None))
        self.label_department.setText(QCoreApplication.translate("Home", u"no department", None))
        self.push_exit.setText(QCoreApplication.translate("Home", u"Exit", None))
        self.push_logout.setText(QCoreApplication.translate("Home", u"Log out", None))
        self.label_name.setText(QCoreApplication.translate("Home", u"Algeval", None))
        self.push_reload.setText(QCoreApplication.translate("Home", u"Reload sessions", None))
        self.push_continue.setText(QCoreApplication.translate("Home", u"Continue session", None))
        self.push_delete.setText(QCoreApplication.translate("Home", u"Delete session", None))
        self.push_create.setText(QCoreApplication.translate("Home", u"Create a new grading session", None))
        self.label_submit.setText(QCoreApplication.translate("Home", u"Sessions: ", None))
        self.label_note.setText(QCoreApplication.translate("Home", u"*Last saved session:", None))
    # retranslateUi

