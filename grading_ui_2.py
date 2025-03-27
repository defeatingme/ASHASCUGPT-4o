# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grading_ui_2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Session(object):
    def setupUi(self, Session):
        if not Session.objectName():
            Session.setObjectName(u"Session")
        Session.resize(1140, 840)
        Session.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.label_session = QLabel(Session)
        self.label_session.setObjectName(u"label_session")
        self.label_session.setGeometry(QRect(0, 20, 1141, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_session.setFont(font)
        self.label_session.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 4px")
        self.label_instructor = QLabel(Session)
        self.label_instructor.setObjectName(u"label_instructor")
        self.label_instructor.setGeometry(QRect(0, 50, 211, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_instructor.setFont(font1)
        self.label_instructor.setStyleSheet(u"background-color: rgb(208, 172, 220);\n"
"color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_instructor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_instructor.setOpenExternalLinks(True)
        self.label_ak = QLabel(Session)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(0, 80, 281, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setUnderline(False)
        self.label_ak.setFont(font2)
        self.label_ak.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image = QLabel(Session)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(280, 60, 360, 301))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        self.label_image.setFont(font3)
        self.label_image.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_start = QPushButton(Session)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setGeometry(QRect(280, 770, 361, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.push_start.setFont(font4)
        self.push_start.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"    border: 1px solid rgb(208, 172, 220);\n"
"    border-bottom: 2px solid rgb(121, 100, 128);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(160, 160, 160);\n"
"    border: 1px solid rgb(192, 192, 192);\n"
"    border-radius: 4px\n"
"    }")
        self.push_start.setCheckable(False)
        self.push_back = QPushButton(Session)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 800, 121, 25))
        self.push_back.setFont(font3)
        self.push_back.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_back.setCheckable(False)
        self.frame_latex = QFrame(Session)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(280, 370, 361, 391))
        self.frame_latex.setFont(font3)
        self.frame_latex.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 30, 361, 360))
        self.web_latex.setFont(font3)
        self.web_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 361, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setUnderline(False)
        self.label_latex.setFont(font5)
        self.label_latex.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_name = QLabel(Session)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(780, 0, 351, 21))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(False)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.label_name.setFont(font6)
        self.label_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_checked = QFrame(Session)
        self.frame_checked.setObjectName(u"frame_checked")
        self.frame_checked.setGeometry(QRect(679, 60, 451, 771))
        self.frame_checked.setFont(font3)
        self.frame_checked.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_checked.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_checked.setFrameShadow(QFrame.Shadow.Raised)
        self.label_checked = QLabel(self.frame_checked)
        self.label_checked.setObjectName(u"label_checked")
        self.label_checked.setGeometry(QRect(0, 0, 451, 31))
        self.label_checked.setFont(font5)
        self.label_checked.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_checked.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_table_note = QLabel(self.frame_checked)
        self.label_table_note.setObjectName(u"label_table_note")
        self.label_table_note.setGeometry(QRect(10, 630, 441, 21))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(True)
        font7.setUnderline(False)
        self.label_table_note.setFont(font7)
        self.label_table_note.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_table_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.table_checked = QTableWidget(self.frame_checked)
        self.table_checked.setObjectName(u"table_checked")
        self.table_checked.setGeometry(QRect(0, 30, 451, 601))
        self.table_checked.setFont(font3)
        self.table_checked.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px")
        self.frame_buttons = QFrame(self.frame_checked)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(0, 650, 451, 121))
        self.frame_buttons.setFont(font3)
        self.frame_buttons.setStyleSheet(u"background-color: rgb(48, 48, 48)")
        self.frame_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.push_list = QPushButton(self.frame_buttons)
        self.push_list.setObjectName(u"push_list")
        self.push_list.setGeometry(QRect(10, 80, 431, 25))
        self.push_list.setFont(font3)
        self.push_list.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_list.setCheckable(False)
        self.push_export = QPushButton(self.frame_buttons)
        self.push_export.setObjectName(u"push_export")
        self.push_export.setGeometry(QRect(230, 10, 211, 25))
        self.push_export.setFont(font3)
        self.push_export.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_export.setCheckable(False)
        self.push_delete = QPushButton(self.frame_buttons)
        self.push_delete.setObjectName(u"push_delete")
        self.push_delete.setGeometry(QRect(10, 40, 211, 25))
        self.push_delete.setFont(font3)
        self.push_delete.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_delete.setCheckable(False)
        self.push_reload = QPushButton(self.frame_buttons)
        self.push_reload.setObjectName(u"push_reload")
        self.push_reload.setGeometry(QRect(10, 10, 211, 25))
        self.push_reload.setFont(font3)
        self.push_reload.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_reload.setCheckable(False)
        self.push_recheck = QPushButton(self.frame_buttons)
        self.push_recheck.setObjectName(u"push_recheck")
        self.push_recheck.setGeometry(QRect(230, 40, 211, 25))
        self.push_recheck.setFont(font3)
        self.push_recheck.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_recheck.setCheckable(False)
        self.frame_ak_data = QFrame(Session)
        self.frame_ak_data.setObjectName(u"frame_ak_data")
        self.frame_ak_data.setGeometry(QRect(10, 120, 261, 641))
        self.frame_ak_data.setFont(font3)
        self.frame_ak_data.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_ak_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ak_data.setFrameShadow(QFrame.Shadow.Raised)
        self.edit_fa_weight = QLineEdit(self.frame_ak_data)
        self.edit_fa_weight.setObjectName(u"edit_fa_weight")
        self.edit_fa_weight.setGeometry(QRect(30, 370, 181, 25))
        self.edit_fa_weight.setFont(font3)
        self.edit_fa_weight.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.edit_fa_weight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_grading = QLabel(self.frame_ak_data)
        self.label_grading.setObjectName(u"label_grading")
        self.label_grading.setGeometry(QRect(0, 170, 261, 31))
        self.label_grading.setFont(font5)
        self.label_grading.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_grading.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_computer = QPushButton(self.frame_ak_data)
        self.push_computer.setObjectName(u"push_computer")
        self.push_computer.setGeometry(QRect(10, 90, 240, 25))
        self.push_computer.setFont(font3)
        self.push_computer.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_computer.setCheckable(False)
        self.push_camera = QPushButton(self.frame_ak_data)
        self.push_camera.setObjectName(u"push_camera")
        self.push_camera.setGeometry(QRect(10, 60, 240, 25))
        self.push_camera.setFont(font3)
        self.push_camera.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_camera.setCheckable(False)
        self.label_submit = QLabel(self.frame_ak_data)
        self.label_submit.setObjectName(u"label_submit")
        self.label_submit.setGeometry(QRect(0, 0, 261, 31))
        self.label_submit.setFont(font5)
        self.label_submit.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_submit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_settings = QLabel(self.frame_ak_data)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setGeometry(QRect(0, 410, 261, 31))
        self.label_settings.setFont(font5)
        self.label_settings.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_settings.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_redo = QPushButton(self.frame_ak_data)
        self.push_redo.setObjectName(u"push_redo")
        self.push_redo.setGeometry(QRect(10, 130, 240, 25))
        self.push_redo.setFont(font3)
        self.push_redo.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_redo.setCheckable(False)
        self.label_save_note = QLabel(self.frame_ak_data)
        self.label_save_note.setObjectName(u"label_save_note")
        self.label_save_note.setGeometry(QRect(10, 440, 251, 21))
        self.label_save_note.setFont(font7)
        self.label_save_note.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_save_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_fa_weight = QLabel(self.frame_ak_data)
        self.label_fa_weight.setObjectName(u"label_fa_weight")
        self.label_fa_weight.setGeometry(QRect(0, 310, 261, 31))
        self.label_fa_weight.setFont(font5)
        self.label_fa_weight.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None;\n"
"border-top: 1px solid rgb(175, 192, 220);\n"
"")
        self.label_fa_weight.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_sol_layers = QLineEdit(self.frame_ak_data)
        self.edit_sol_layers.setObjectName(u"edit_sol_layers")
        self.edit_sol_layers.setGeometry(QRect(40, 270, 181, 25))
        self.edit_sol_layers.setFont(font3)
        self.edit_sol_layers.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.edit_sol_layers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_sol_autofill = QLabel(self.frame_ak_data)
        self.label_sol_autofill.setObjectName(u"label_sol_autofill")
        self.label_sol_autofill.setGeometry(QRect(10, 230, 251, 31))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(True)
        font8.setUnderline(False)
        self.label_sol_autofill.setFont(font8)
        self.label_sol_autofill.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_sol_autofill.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_sol_note = QLabel(self.frame_ak_data)
        self.label_sol_note.setObjectName(u"label_sol_note")
        self.label_sol_note.setGeometry(QRect(10, 200, 251, 31))
        self.label_sol_note.setFont(font5)
        self.label_sol_note.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_sol_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_save = QPushButton(self.frame_ak_data)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(10, 470, 241, 41))
        self.push_save.setFont(font4)
        self.push_save.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"    border: 1px solid rgb(208, 172, 220);\n"
"    border-bottom: 2px solid rgb(121, 100, 128);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(160, 160, 160);\n"
"    border: 1px solid rgb(192, 192, 192);\n"
"    border-radius: 4px\n"
"    }")
        self.push_save.setCheckable(False)
        self.push_add = QPushButton(self.frame_ak_data)
        self.push_add.setObjectName(u"push_add")
        self.push_add.setGeometry(QRect(10, 520, 241, 31))
        self.push_add.setFont(font4)
        self.push_add.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_add.setCheckable(False)
        self.label_sol_autofill_2 = QLabel(self.frame_ak_data)
        self.label_sol_autofill_2.setObjectName(u"label_sol_autofill_2")
        self.label_sol_autofill_2.setGeometry(QRect(10, 30, 241, 21))
        self.label_sol_autofill_2.setFont(font7)
        self.label_sol_autofill_2.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_sol_autofill_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_sol_autofill_3 = QLabel(self.frame_ak_data)
        self.label_sol_autofill_3.setObjectName(u"label_sol_autofill_3")
        self.label_sol_autofill_3.setGeometry(QRect(10, 340, 251, 21))
        self.label_sol_autofill_3.setFont(font7)
        self.label_sol_autofill_3.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_sol_autofill_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_view_ak_2 = QPushButton(self.frame_ak_data)
        self.push_view_ak_2.setObjectName(u"push_view_ak_2")
        self.push_view_ak_2.setGeometry(QRect(10, 605, 241, 25))
        self.push_view_ak_2.setFont(font4)
        self.push_view_ak_2.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_view_ak_2.setCheckable(False)
        self.push_view_ak = QPushButton(self.frame_ak_data)
        self.push_view_ak.setObjectName(u"push_view_ak")
        self.push_view_ak.setGeometry(QRect(10, 560, 241, 25))
        self.push_view_ak.setFont(font4)
        self.push_view_ak.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_view_ak.setCheckable(False)
        self.frame = QFrame(Session)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(650, 60, 21, 771))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border-radius: 2px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(Session)

        QMetaObject.connectSlotsByName(Session)
    # setupUi

    def retranslateUi(self, Session):
        Session.setWindowTitle(QCoreApplication.translate("Session", u"Form", None))
        self.label_session.setText(QCoreApplication.translate("Session", u"Session:", None))
        self.label_instructor.setText(QCoreApplication.translate("Session", u"by: Anonymous", None))
        self.label_ak.setText(QCoreApplication.translate("Session", u"Answer Key (AK)", None))
        self.label_image.setText(QCoreApplication.translate("Session", u"Source file preview\n"
"360x300", None))
        self.push_start.setText(QCoreApplication.translate("Session", u"Start checking solutions", None))
        self.push_back.setText(QCoreApplication.translate("Session", u"Back", None))
        self.label_latex.setText(QCoreApplication.translate("Session", u"AK in LaTeX: ", None))
        self.label_name.setText(QCoreApplication.translate("Session", u"Algeval", None))
        self.label_checked.setText(QCoreApplication.translate("Session", u"List of checked solutions: ", None))
        self.label_table_note.setText(QCoreApplication.translate("Session", u"*No recorded solutions", None))
        self.push_list.setText(QCoreApplication.translate("Session", u"View full table", None))
        self.push_export.setText(QCoreApplication.translate("Session", u"Export table as...", None))
        self.push_delete.setText(QCoreApplication.translate("Session", u"Delete solution", None))
        self.push_reload.setText(QCoreApplication.translate("Session", u"Reload table", None))
        self.push_recheck.setText(QCoreApplication.translate("Session", u"Recheck solution", None))
        self.edit_fa_weight.setText("")
        self.edit_fa_weight.setPlaceholderText(QCoreApplication.translate("Session", u"[Autofill if none]", None))
        self.label_grading.setText(QCoreApplication.translate("Session", u"Grading mechanics:", None))
        self.push_computer.setText(QCoreApplication.translate("Session", u"From computer", None))
        self.push_camera.setText(QCoreApplication.translate("Session", u"Open camera", None))
        self.label_submit.setText(QCoreApplication.translate("Session", u"Submit file:", None))
        self.label_settings.setText(QCoreApplication.translate("Session", u"Settings:", None))
        self.push_redo.setText(QCoreApplication.translate("Session", u"Redo OCR", None))
        self.label_save_note.setText(QCoreApplication.translate("Session", u"*No. of AKs saved: 0/2", None))
        self.label_fa_weight.setText(QCoreApplication.translate("Session", u" Input final answer weight (%): ", None))
        self.edit_sol_layers.setText("")
        self.edit_sol_layers.setPlaceholderText(QCoreApplication.translate("Session", u"0 - 10 [Autofill if none]", None))
        self.label_sol_autofill.setText(QCoreApplication.translate("Session", u"*Does not include the problem setup\n"
"and final answer", None))
        self.label_sol_note.setText(QCoreApplication.translate("Session", u"Input no. of steps in the solution: ", None))
        self.push_save.setText(QCoreApplication.translate("Session", u"Save data", None))
        self.push_add.setText(QCoreApplication.translate("Session", u"Add AK for another problem", None))
        self.label_sol_autofill_2.setText(QCoreApplication.translate("Session", u"*Must be one problem solved step-by-step", None))
        self.label_sol_autofill_3.setText(QCoreApplication.translate("Session", u"*Same weight as solution steps by default", None))
        self.push_view_ak_2.setText(QCoreApplication.translate("Session", u"Delete AK", None))
        self.push_view_ak.setText(QCoreApplication.translate("Session", u"View saved", None))
    # retranslateUi

