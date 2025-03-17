# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ak_dialog_ui_2.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 480)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.frame_latex = QFrame(Dialog)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(480, 10, 361, 460))
        self.frame_latex.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: rgb(96, 96, 96);\n"
"border-radius: 2px\n"
"")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 39, 361, 421))
        self.web_latex.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 361, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.label_latex.setFont(font)
        self.label_latex.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_sol_grade = QLabel(self.frame_latex)
        self.label_sol_grade.setObjectName(u"label_sol_grade")
        self.label_sol_grade.setGeometry(QRect(0, 20, 211, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_sol_grade.setFont(font1)
        self.label_sol_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_sol_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade = QLabel(self.frame_latex)
        self.label_fa_grade.setObjectName(u"label_fa_grade")
        self.label_fa_grade.setGeometry(QRect(210, 20, 151, 21))
        self.label_fa_grade.setFont(font1)
        self.label_fa_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_fa_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_back = QPushButton(Dialog)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(860, 440, 211, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.push_back.setFont(font2)
        self.push_back.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"}\n"
"QPushButton:hover {\n"
"color:  rgb(175, 192, 220);\n"
"border: 1px solid rgb(175, 192, 220);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:  rgb(208, 172, 220);\n"
"color: #eee;\n"
"border: 1px solid #eee;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.push_back.setCheckable(False)
        self.frame_note = QFrame(Dialog)
        self.frame_note.setObjectName(u"frame_note")
        self.frame_note.setGeometry(QRect(850, 30, 221, 381))
        self.frame_note.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 2px")
        self.frame_note.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_note.setFrameShadow(QFrame.Shadow.Raised)
        self.label_note3 = QLabel(self.frame_note)
        self.label_note3.setObjectName(u"label_note3")
        self.label_note3.setGeometry(QRect(0, 160, 221, 161))
        self.label_note3.setFont(font1)
        self.label_note3.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border-radius: 2px\n"
"")
        self.label_note3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_note1 = QLabel(self.frame_note)
        self.label_note1.setObjectName(u"label_note1")
        self.label_note1.setGeometry(QRect(0, 0, 221, 81))
        self.label_note1.setFont(font1)
        self.label_note1.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border-radius: 2px\n"
"")
        self.label_note1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_note2 = QLabel(self.frame_note)
        self.label_note2.setObjectName(u"label_note2")
        self.label_note2.setGeometry(QRect(0, 80, 221, 81))
        self.label_note2.setFont(font1)
        self.label_note2.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border-radius: 2px\n"
"")
        self.label_note2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_note4 = QLabel(self.frame_note)
        self.label_note4.setObjectName(u"label_note4")
        self.label_note4.setGeometry(QRect(0, 320, 221, 61))
        self.label_note4.setFont(font1)
        self.label_note4.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border-radius: 2px\n"
"")
        self.label_note4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_file = QLabel(Dialog)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setGeometry(QRect(10, 10, 461, 461))
        self.label_file.setFont(font2)
        self.label_file.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_file.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_latex.setText(QCoreApplication.translate("Dialog", u"Answer key:", None))
        self.label_sol_grade.setText(QCoreApplication.translate("Dialog", u"Step-by-step solution (SOL):", None))
        self.label_fa_grade.setText(QCoreApplication.translate("Dialog", u"Final answer (FA):", None))
        self.push_back.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.label_note3.setText(QCoreApplication.translate("Dialog", u"SOL grade is calculated as:\n"
"\n"
" (C / T) * W\n"
"\n"
" - C = correct SOL steps aligned\n"
"with answer key counterpart;\n"
" - T = total SOL steps from answer\n"
"key; and\n"
" - W = SOL weight.", None))
        self.label_note1.setText(QCoreApplication.translate("Dialog", u"Step-by-step solution (SOL) weight\n"
"is calculated as:\n"
"\n"
" 100 - Final answer (FA) weight", None))
        self.label_note2.setText(QCoreApplication.translate("Dialog", u"Thus, overall grade of the checked\n"
"solution is calculated as:\n"
"\n"
" (SOL grade + FA grade) %", None))
        self.label_note4.setText(QCoreApplication.translate("Dialog", u"FA is typically the last layer of a\n"
"solution and does not count as a\n"
"SOL step.", None))
        self.label_file.setText(QCoreApplication.translate("Dialog", u"Source file preview\n"
"460x460\n"
"\n"
"No source found", None))
    # retranslateUi

