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
        Session.resize(960, 720)
        Session.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.label_session = QLabel(Session)
        self.label_session.setObjectName(u"label_session")
        self.label_session.setGeometry(QRect(0, 20, 960, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_session.setFont(font)
        self.label_session.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 8px;\n"
"")
        self.label_instructor = QLabel(Session)
        self.label_instructor.setObjectName(u"label_instructor")
        self.label_instructor.setGeometry(QRect(0, 60, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_instructor.setFont(font1)
        self.label_instructor.setStyleSheet(u"background-color: rgb(160, 160, 160);\n"
"color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 4px;\n"
"")
        self.label_instructor.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_instructor.setOpenExternalLinks(True)
        self.label_ak = QLabel(Session)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(0, 100, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
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
        self.label_image.setGeometry(QRect(220, 70, 360, 271))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.label_image.setFont(font3)
        self.label_image.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_start = QPushButton(Session)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setGeometry(QRect(590, 680, 361, 25))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.push_start.setFont(font4)
        self.push_start.setStyleSheet(u"QPushButton {\n"
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
        self.push_start.setCheckable(False)
        self.push_back = QPushButton(Session)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 690, 121, 21))
        self.push_back.setFont(font3)
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
        self.frame_latex = QFrame(Session)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(220, 350, 361, 361))
        self.frame_latex.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 20, 361, 341))
        self.web_latex.setStyleSheet(u"background-color:  rgb(64, 64, 64);")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 361, 21))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setUnderline(False)
        self.label_latex.setFont(font5)
        self.label_latex.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_name = QLabel(Session)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(600, 0, 351, 21))
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
        self.frame_checked.setGeometry(QRect(590, 70, 360, 601))
        self.frame_checked.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 2px")
        self.frame_checked.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_checked.setFrameShadow(QFrame.Shadow.Raised)
        self.label_checked = QLabel(self.frame_checked)
        self.label_checked.setObjectName(u"label_checked")
        self.label_checked.setGeometry(QRect(0, 0, 360, 21))
        self.label_checked.setFont(font5)
        self.label_checked.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_checked.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.table_checked = QTableWidget(self.frame_checked)
        self.table_checked.setObjectName(u"table_checked")
        self.table_checked.setGeometry(QRect(0, 20, 360, 480))
        self.table_checked.setStyleSheet(u"background-color:  rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px")
        self.push_list = QPushButton(self.frame_checked)
        self.push_list.setObjectName(u"push_list")
        self.push_list.setGeometry(QRect(10, 570, 341, 21))
        self.push_list.setFont(font3)
        self.push_list.setStyleSheet(u"QPushButton {\n"
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
        self.push_list.setCheckable(False)
        self.push_export = QPushButton(self.frame_checked)
        self.push_export.setObjectName(u"push_export")
        self.push_export.setGeometry(QRect(170, 540, 181, 21))
        self.push_export.setFont(font3)
        self.push_export.setStyleSheet(u"QPushButton {\n"
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
        self.push_export.setCheckable(False)
        self.label_table_note = QLabel(self.frame_checked)
        self.label_table_note.setObjectName(u"label_table_note")
        self.label_table_note.setGeometry(QRect(0, 500, 161, 31))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setUnderline(False)
        self.label_table_note.setFont(font7)
        self.label_table_note.setStyleSheet(u"color: rgb(208, 172, 220);\n"
"background-color: rgb(56, 56, 56);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 2px")
        self.label_table_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_reload = QPushButton(self.frame_checked)
        self.push_reload.setObjectName(u"push_reload")
        self.push_reload.setGeometry(QRect(170, 510, 181, 21))
        self.push_reload.setFont(font3)
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
        self.push_delete = QPushButton(self.frame_checked)
        self.push_delete.setObjectName(u"push_delete")
        self.push_delete.setGeometry(QRect(10, 540, 121, 21))
        self.push_delete.setFont(font3)
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
        self.frame_ak_data = QFrame(Session)
        self.frame_ak_data.setObjectName(u"frame_ak_data")
        self.frame_ak_data.setGeometry(QRect(10, 140, 201, 381))
        self.frame_ak_data.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 2px")
        self.frame_ak_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ak_data.setFrameShadow(QFrame.Shadow.Raised)
        self.edit_fa_weight = QLineEdit(self.frame_ak_data)
        self.edit_fa_weight.setObjectName(u"edit_fa_weight")
        self.edit_fa_weight.setGeometry(QRect(20, 170, 161, 25))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        self.edit_fa_weight.setFont(font8)
        self.edit_fa_weight.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.edit_fa_weight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_fa_weight = QLabel(self.frame_ak_data)
        self.label_fa_weight.setObjectName(u"label_fa_weight")
        self.label_fa_weight.setGeometry(QRect(0, 140, 201, 21))
        self.label_fa_weight.setFont(font5)
        self.label_fa_weight.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_fa_weight.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_fa_note = QLabel(self.frame_ak_data)
        self.label_fa_note.setObjectName(u"label_fa_note")
        self.label_fa_note.setGeometry(QRect(20, 200, 161, 51))
        self.label_fa_note.setFont(font7)
        self.label_fa_note.setStyleSheet(u"background-color: None;\n"
"color: rgb(208, 172, 220);\n"
"border: None")
        self.label_fa_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_computer = QPushButton(self.frame_ak_data)
        self.push_computer.setObjectName(u"push_computer")
        self.push_computer.setGeometry(QRect(10, 60, 181, 21))
        self.push_computer.setFont(font3)
        self.push_computer.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
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
        self.push_computer.setCheckable(False)
        self.push_camera = QPushButton(self.frame_ak_data)
        self.push_camera.setObjectName(u"push_camera")
        self.push_camera.setGeometry(QRect(10, 30, 181, 21))
        self.push_camera.setFont(font3)
        self.push_camera.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
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
        self.push_camera.setCheckable(False)
        self.label_submit = QLabel(self.frame_ak_data)
        self.label_submit.setObjectName(u"label_submit")
        self.label_submit.setGeometry(QRect(0, 0, 201, 21))
        self.label_submit.setFont(font5)
        self.label_submit.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_submit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_save = QPushButton(self.frame_ak_data)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(10, 300, 181, 21))
        self.push_save.setFont(font4)
        self.push_save.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
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
        self.push_save.setCheckable(False)
        self.label_save_note = QLabel(self.frame_ak_data)
        self.label_save_note.setObjectName(u"label_save_note")
        self.label_save_note.setGeometry(QRect(10, 320, 181, 21))
        self.label_save_note.setFont(font7)
        self.label_save_note.setStyleSheet(u"background-color: None;\n"
"color: rgb(208, 172, 220);\n"
"border: None;")
        self.label_save_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_settings = QLabel(self.frame_ak_data)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setGeometry(QRect(0, 270, 201, 21))
        self.label_settings.setFont(font5)
        self.label_settings.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_settings.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_reset = QPushButton(self.frame_ak_data)
        self.push_reset.setObjectName(u"push_reset")
        self.push_reset.setGeometry(QRect(10, 350, 181, 21))
        self.push_reset.setFont(font3)
        self.push_reset.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
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
        self.push_reset.setCheckable(False)
        self.push_redo = QPushButton(self.frame_ak_data)
        self.push_redo.setObjectName(u"push_redo")
        self.push_redo.setGeometry(QRect(10, 100, 181, 21))
        self.push_redo.setFont(font3)
        self.push_redo.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
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
        self.push_redo.setCheckable(False)

        self.retranslateUi(Session)

        QMetaObject.connectSlotsByName(Session)
    # setupUi

    def retranslateUi(self, Session):
        Session.setWindowTitle(QCoreApplication.translate("Session", u"Form", None))
        self.label_session.setText(QCoreApplication.translate("Session", u"Session:", None))
        self.label_instructor.setText(QCoreApplication.translate("Session", u"by:", None))
        self.label_ak.setText(QCoreApplication.translate("Session", u"Answer key", None))
        self.label_image.setText(QCoreApplication.translate("Session", u"Source file preview\n"
"360x270", None))
        self.push_start.setText(QCoreApplication.translate("Session", u"Start checking", None))
        self.push_back.setText(QCoreApplication.translate("Session", u"Back to home", None))
        self.label_latex.setText(QCoreApplication.translate("Session", u"Answer key in LaTeX", None))
        self.label_name.setText(QCoreApplication.translate("Session", u"Algeval", None))
        self.label_checked.setText(QCoreApplication.translate("Session", u"List of checked solutions: ", None))
        self.push_list.setText(QCoreApplication.translate("Session", u"View full list details", None))
        self.push_export.setText(QCoreApplication.translate("Session", u"Export", None))
        self.label_table_note.setText(QCoreApplication.translate("Session", u" *No recorded solutions", None))
        self.push_reload.setText(QCoreApplication.translate("Session", u"Reload", None))
        self.push_delete.setText(QCoreApplication.translate("Session", u"Delete record", None))
        self.edit_fa_weight.setText("")
        self.edit_fa_weight.setPlaceholderText(QCoreApplication.translate("Session", u"20", None))
        self.label_fa_weight.setText(QCoreApplication.translate("Session", u"Final answer weight (%): ", None))
        self.label_fa_note.setText(QCoreApplication.translate("Session", u"*Default: 20\n"
"\n"
"*Final answer percetage against\n"
"step-by-step solution", None))
        self.push_computer.setText(QCoreApplication.translate("Session", u"From computer", None))
        self.push_camera.setText(QCoreApplication.translate("Session", u"Open camera", None))
        self.label_submit.setText(QCoreApplication.translate("Session", u"Submit file: ", None))
        self.push_save.setText(QCoreApplication.translate("Session", u"Save answer key data", None))
        self.label_save_note.setText(QCoreApplication.translate("Session", u"*No data is saved", None))
        self.label_settings.setText(QCoreApplication.translate("Session", u"Save and reset:", None))
        self.push_reset.setText(QCoreApplication.translate("Session", u"Reset all", None))
        self.push_redo.setText(QCoreApplication.translate("Session", u"Redo OCR", None))
    # retranslateUi

