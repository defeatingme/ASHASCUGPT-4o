# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grading_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_Session(object):
    def setupUi(self, Session):
        if not Session.objectName():
            Session.setObjectName(u"Session")
        Session.resize(720, 540)
        Session.setStyleSheet(u"background-color:qconicalgradient(cx:0, cy:1, angle:159.4, stop:0 rgba(212, 161, 205, 255), stop:1 rgba(71, 71, 71, 255))")
        self.label_session = QLabel(Session)
        self.label_session.setObjectName(u"label_session")
        self.label_session.setGeometry(QRect(0, 20, 721, 45))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_session.setFont(font)
        self.label_session.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"color: #eee;\n"
"border: 1px solid #eee;\n"
"padding: 8px")
        self.label_instructor = QLabel(Session)
        self.label_instructor.setObjectName(u"label_instructor")
        self.label_instructor.setGeometry(QRect(0, 64, 240, 35))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_instructor.setFont(font1)
        self.label_instructor.setStyleSheet(u"background-color: #eee;\n"
"color: #333;\n"
"border: 1px solid rgb(71, 71, 71);\n"
"padding: 8px")
        self.label_instructor.setOpenExternalLinks(True)
        self.label_submit = QLabel(Session)
        self.label_submit.setObjectName(u"label_submit")
        self.label_submit.setGeometry(QRect(160, 120, 180, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_submit.setFont(font2)
        self.label_submit.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_submit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_camera = QPushButton(Session)
        self.push_camera.setObjectName(u"push_camera")
        self.push_camera.setGeometry(QRect(160, 160, 121, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.push_camera.setFont(font3)
        self.push_camera.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_camera.setCheckable(False)
        self.push_computer = QPushButton(Session)
        self.push_computer.setObjectName(u"push_computer")
        self.push_computer.setGeometry(QRect(160, 190, 121, 21))
        self.push_computer.setFont(font3)
        self.push_computer.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_computer.setCheckable(False)
        self.label_fa_weight = QLabel(Session)
        self.label_fa_weight.setObjectName(u"label_fa_weight")
        self.label_fa_weight.setGeometry(QRect(210, 270, 180, 21))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label_fa_weight.setFont(font4)
        self.label_fa_weight.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_fa_weight.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_default = QLabel(Session)
        self.label_default.setObjectName(u"label_default")
        self.label_default.setGeometry(QRect(210, 290, 91, 21))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setUnderline(False)
        self.label_default.setFont(font5)
        self.label_default.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_default.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_fa_weight = QLineEdit(Session)
        self.edit_fa_weight.setObjectName(u"edit_fa_weight")
        self.edit_fa_weight.setGeometry(QRect(210, 320, 41, 30))
        self.edit_fa_weight.setStyleSheet(u"padding: 8px; \n"
"border-radius: 5px; \n"
"border: 1px solid rgb(81, 139, 132);\n"
"background-color: white")
        self.edit_fa_weight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_percent = QLabel(Session)
        self.label_percent.setObjectName(u"label_percent")
        self.label_percent.setGeometry(QRect(260, 320, 41, 31))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setUnderline(False)
        self.label_percent.setFont(font6)
        self.label_percent.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_percent.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_image = QLabel(Session)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(20, 120, 120, 120))
        self.label_image.setStyleSheet(u"border: 1px solid  #eee;\n"
"background-color: rgb(71, 71, 71);\n"
"color: #eee")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_latex = QLabel(Session)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(20, 250, 181, 241))
        self.label_latex.setStyleSheet(u"border: 1px solid  rgb(71, 71, 71);\n"
"background-color: #eee;\n"
"color: #333")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_save = QPushButton(Session)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(210, 400, 121, 21))
        self.push_save.setFont(font3)
        self.push_save.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_save.setCheckable(False)
        self.table_list = QTableView(Session)
        self.table_list.setObjectName(u"table_list")
        self.table_list.setGeometry(QRect(460, 150, 240, 300))
        self.table_list.setStyleSheet(u"border: 1px solid rgb(71, 71, 71);\n"
"background-color: #eee;\n"
"color: #333")
        self.label_list = QLabel(Session)
        self.label_list.setObjectName(u"label_list")
        self.label_list.setGeometry(QRect(460, 130, 241, 21))
        self.label_list.setFont(font4)
        self.label_list.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_list.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_start = QPushButton(Session)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setGeometry(QRect(520, 470, 181, 25))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.push_start.setFont(font7)
        self.push_start.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_start.setCheckable(False)
        self.push_back = QPushButton(Session)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(20, 510, 121, 21))
        self.push_back.setFont(font3)
        self.push_back.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_back.setCheckable(False)

        self.retranslateUi(Session)

        QMetaObject.connectSlotsByName(Session)
    # setupUi

    def retranslateUi(self, Session):
        Session.setWindowTitle(QCoreApplication.translate("Session", u"Session - Algeval", None))
        self.label_session.setText(QCoreApplication.translate("Session", u"Session: {session_id}", None))
        self.label_instructor.setText(QCoreApplication.translate("Session", u"by: {instructor_name}", None))
        self.label_submit.setText(QCoreApplication.translate("Session", u"Submit Answer Key File", None))
        self.push_camera.setText(QCoreApplication.translate("Session", u"Open Camera", None))
        self.push_computer.setText(QCoreApplication.translate("Session", u"From Computer", None))
        self.label_fa_weight.setText(QCoreApplication.translate("Session", u"Final Answer Weight", None))
        self.label_default.setText(QCoreApplication.translate("Session", u"Default: 20", None))
        self.edit_fa_weight.setText("")
        self.edit_fa_weight.setPlaceholderText(QCoreApplication.translate("Session", u"20", None))
        self.label_percent.setText(QCoreApplication.translate("Session", u"%", None))
        self.label_image.setText(QCoreApplication.translate("Session", u"Image Preview\n"
"120x120", None))
        self.label_latex.setText(QCoreApplication.translate("Session", u"Rendered LaTeX Preview\n"
"180 \u00d7 240", None))
        self.push_save.setText(QCoreApplication.translate("Session", u"Save Changes", None))
        self.label_list.setText(QCoreApplication.translate("Session", u"List of checked solutions", None))
        self.push_start.setText(QCoreApplication.translate("Session", u"Start Checking", None))
        self.push_back.setText(QCoreApplication.translate("Session", u"Back to Home", None))
    # retranslateUi

