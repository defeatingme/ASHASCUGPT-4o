# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'has_camera_ui_3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QStatusBar, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(1600, 900)
        Camera.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.actionExit = QAction(Camera)
        self.actionExit.setObjectName(u"actionExit")
        self.actionStartCamera = QAction(Camera)
        self.actionStartCamera.setObjectName(u"actionStartCamera")
        self.actionStopCamera = QAction(Camera)
        self.actionStopCamera.setObjectName(u"actionStopCamera")
        self.actionSettings = QAction(Camera)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout_Qt = QAction(Camera)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(Camera)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 40, 820, 710))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        gradient = QLinearGradient(1, 1, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(64, 64, 64, 255))
        gradient.setColorAt(1, QColor(48, 48, 48, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(1, 1, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(64, 64, 64, 255))
        gradient1.setColorAt(1, QColor(48, 48, 48, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(1, 1, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(64, 64, 64, 255))
        gradient2.setColorAt(1, QColor(48, 48, 48, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(1, 1, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(64, 64, 64, 255))
        gradient3.setColorAt(1, QColor(48, 48, 48, 255))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(1, 1, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(64, 64, 64, 255))
        gradient4.setColorAt(1, QColor(48, 48, 48, 255))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(1, 1, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(64, 64, 64, 255))
        gradient5.setColorAt(1, QColor(48, 48, 48, 255))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(1, 1, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(64, 64, 64, 255))
        gradient6.setColorAt(1, QColor(48, 48, 48, 255))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(1, 1, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(64, 64, 64, 255))
        gradient7.setColorAt(1, QColor(48, 48, 48, 255))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(1, 1, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(64, 64, 64, 255))
        gradient8.setColorAt(1, QColor(48, 48, 48, 255))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.viewfinderPage = QWidget()
        self.viewfinderPage.setObjectName(u"viewfinderPage")
        self.gridLayout_5 = QGridLayout(self.viewfinderPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.viewfinder = QVideoWidget(self.viewfinderPage)
        self.viewfinder.setObjectName(u"viewfinder")

        self.gridLayout_5.addWidget(self.viewfinder, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewfinderPage)
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.gridLayout_4 = QGridLayout(self.previewPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lastImagePreviewLabel = QLabel(self.previewPage)
        self.lastImagePreviewLabel.setObjectName(u"lastImagePreviewLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lastImagePreviewLabel.sizePolicy().hasHeightForWidth())
        self.lastImagePreviewLabel.setSizePolicy(sizePolicy1)
        self.lastImagePreviewLabel.setFrameShape(QFrame.Shape.Box)

        self.gridLayout_4.addWidget(self.lastImagePreviewLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.previewPage)
        self.push_back = QPushButton(self.centralwidget)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 820, 121, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.push_back.setFont(font)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(240, 750, 581, 101))
        font1 = QFont()
        font1.setPointSize(11)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.push_recheck = QPushButton(self.frame)
        self.push_recheck.setObjectName(u"push_recheck")
        self.push_recheck.setGeometry(QRect(20, 50, 171, 41))
        self.push_recheck.setFont(font)
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
        self.push_redo = QPushButton(self.frame)
        self.push_redo.setObjectName(u"push_redo")
        self.push_redo.setGeometry(QRect(200, 50, 171, 41))
        self.push_redo.setFont(font)
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
        self.push_size = QPushButton(self.frame)
        self.push_size.setObjectName(u"push_size")
        self.push_size.setGeometry(QRect(390, 60, 171, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.push_size.setFont(font2)
        self.push_size.setStyleSheet(u"QPushButton {\n"
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
        self.push_size.setCheckable(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 181, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: None;\n"
"border: None;\n"
"color: #eee")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeImageButton = QPushButton(self.frame)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(False)
        self.takeImageButton.setGeometry(QRect(390, 10, 171, 41))
        self.takeImageButton.setFont(font3)
        self.takeImageButton.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 2px solid rgb(96, 96, 96);\n"
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
        self.exposureCompensation = QSlider(self.frame)
        self.exposureCompensation.setObjectName(u"exposureCompensation")
        self.exposureCompensation.setGeometry(QRect(210, 10, 161, 31))
        self.exposureCompensation.setStyleSheet(u"background-color: None;\n"
"border: None;")
        self.exposureCompensation.setMinimum(-4)
        self.exposureCompensation.setMaximum(4)
        self.exposureCompensation.setPageStep(2)
        self.exposureCompensation.setOrientation(Qt.Orientation.Horizontal)
        self.exposureCompensation.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.frame_result = QFrame(self.centralwidget)
        self.frame_result.setObjectName(u"frame_result")
        self.frame_result.setGeometry(QRect(1190, 10, 401, 831))
        font4 = QFont()
        self.frame_result.setFont(font4)
        self.frame_result.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_result.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result.setFrameShadow(QFrame.Shadow.Raised)
        self.label_result = QLabel(self.frame_result)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(0, 0, 401, 30))
        self.label_result.setFont(font2)
        self.label_result.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade = QLabel(self.frame_result)
        self.label_sol_grade.setObjectName(u"label_sol_grade")
        self.label_sol_grade.setGeometry(QRect(0, 780, 121, 50))
        self.label_sol_grade.setFont(font2)
        self.label_sol_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade = QLabel(self.frame_result)
        self.label_fa_grade.setObjectName(u"label_fa_grade")
        self.label_fa_grade.setGeometry(QRect(120, 780, 120, 50))
        self.label_fa_grade.setFont(font2)
        self.label_fa_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_fa_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_overall_grade = QLabel(self.frame_result)
        self.label_overall_grade.setObjectName(u"label_overall_grade")
        self.label_overall_grade.setGeometry(QRect(240, 780, 161, 50))
        self.label_overall_grade.setFont(font2)
        self.label_overall_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_overall_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.web_result = QWebEngineView(self.frame_result)
        self.web_result.setObjectName(u"web_result")
        self.web_result.setGeometry(QRect(0, 30, 401, 750))
        self.web_result.setFont(font1)
        self.web_result.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.frame_latex = QFrame(self.centralwidget)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(830, 420, 351, 331))
        self.frame_latex.setFont(font4)
        self.frame_latex.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 30, 351, 300))
        self.web_latex.setFont(font1)
        self.web_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 351, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setUnderline(False)
        self.label_latex.setFont(font5)
        self.label_latex.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_save = QPushButton(self.centralwidget)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(850, 800, 301, 41))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.push_save.setFont(font6)
        self.push_save.setStyleSheet(u"QPushButton {\n"
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
        self.push_save.setCheckable(False)
        self.push_view_ak = QPushButton(self.centralwidget)
        self.push_view_ak.setObjectName(u"push_view_ak")
        self.push_view_ak.setGeometry(QRect(230, 10, 121, 25))
        self.push_view_ak.setFont(font)
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
        self.label_image_2 = QLabel(self.centralwidget)
        self.label_image_2.setObjectName(u"label_image_2")
        self.label_image_2.setGeometry(QRect(830, 110, 351, 301))
        self.label_image_2.setFont(font)
        self.label_image_2.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_ak_count = QLabel(self.centralwidget)
        self.label_ak_count.setObjectName(u"label_ak_count")
        self.label_ak_count.setGeometry(QRect(10, 0, 211, 41))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(True)
        self.label_ak_count.setFont(font7)
        self.label_ak_count.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_ak_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_view_has = QPushButton(self.centralwidget)
        self.push_view_has.setObjectName(u"push_view_has")
        self.push_view_has.setGeometry(QRect(360, 10, 151, 25))
        self.push_view_has.setFont(font)
        self.push_view_has.setStyleSheet(u"QPushButton {\n"
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
        self.push_view_has.setCheckable(False)
        self.label_counter = QLabel(self.centralwidget)
        self.label_counter.setObjectName(u"label_counter")
        self.label_counter.setGeometry(QRect(520, 0, 151, 41))
        self.label_counter.setFont(font7)
        self.label_counter.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"")
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_last_name = QLabel(self.centralwidget)
        self.label_last_name.setObjectName(u"label_last_name")
        self.label_last_name.setGeometry(QRect(670, 0, 151, 41))
        self.label_last_name.setFont(font7)
        self.label_last_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"")
        self.label_last_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.edit_student_name = QLineEdit(self.centralwidget)
        self.edit_student_name.setObjectName(u"edit_student_name")
        self.edit_student_name.setGeometry(QRect(880, 760, 301, 30))
        self.edit_student_name.setFont(font)
        self.edit_student_name.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(224, 224, 224)")
        self.label_student_name = QLabel(self.centralwidget)
        self.label_student_name.setObjectName(u"label_student_name")
        self.label_student_name.setGeometry(QRect(831, 765, 80, 21))
        self.label_student_name.setFont(font5)
        self.label_student_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_student_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame_has_data = QFrame(self.centralwidget)
        self.frame_has_data.setObjectName(u"frame_has_data")
        self.frame_has_data.setGeometry(QRect(830, 10, 351, 91))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(11)
        font8.setItalic(True)
        self.frame_has_data.setFont(font8)
        self.frame_has_data.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_has_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_has_data.setFrameShadow(QFrame.Shadow.Raised)
        self.label_ocr_time = QLabel(self.frame_has_data)
        self.label_ocr_time.setObjectName(u"label_ocr_time")
        self.label_ocr_time.setGeometry(QRect(0, 0, 181, 41))
        self.label_ocr_time.setFont(font7)
        self.label_ocr_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_ocr_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_check_time = QLabel(self.frame_has_data)
        self.label_check_time.setObjectName(u"label_check_time")
        self.label_check_time.setGeometry(QRect(180, 0, 171, 41))
        self.label_check_time.setFont(font7)
        self.label_check_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_check_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_prob_count = QLabel(self.frame_has_data)
        self.label_prob_count.setObjectName(u"label_prob_count")
        self.label_prob_count.setGeometry(QRect(180, 40, 171, 51))
        self.label_prob_count.setFont(font7)
        self.label_prob_count.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_prob_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_total_time = QLabel(self.frame_has_data)
        self.label_total_time.setObjectName(u"label_total_time")
        self.label_total_time.setGeometry(QRect(0, 40, 181, 51))
        self.label_total_time.setFont(font7)
        self.label_total_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_total_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: #eee")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevices = QMenu(self.menubar)
        self.menuDevices.setObjectName(u"menuDevices")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Camera)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"color: #eee; \n"
"background-color: rgb(64,64,64)")
        Camera.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevices.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionStartCamera)
        self.menuFile.addAction(self.actionStopCamera)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(Camera)
        self.actionExit.triggered.connect(Camera.close)
        self.takeImageButton.clicked.connect(Camera.takeImage)
        self.exposureCompensation.valueChanged.connect(Camera.setExposureCompensation)
        self.actionSettings.triggered.connect(Camera.configureCaptureSettings)
        self.actionStartCamera.triggered.connect(Camera.startCamera)
        self.actionStopCamera.triggered.connect(Camera.stopCamera)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Camera", None))
        self.actionExit.setText(QCoreApplication.translate("Camera", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Camera", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionStartCamera.setText(QCoreApplication.translate("Camera", u"Start Camera", None))
        self.actionStopCamera.setText(QCoreApplication.translate("Camera", u"Stop Camera", None))
        self.actionSettings.setText(QCoreApplication.translate("Camera", u"Change Settings", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("Camera", u"About Qt", None))
        self.lastImagePreviewLabel.setText("")
        self.push_back.setText(QCoreApplication.translate("Camera", u"Back", None))
        self.push_recheck.setText(QCoreApplication.translate("Camera", u"Recheck processed\n"
"solution", None))
        self.push_redo.setText(QCoreApplication.translate("Camera", u"Redo from OCR to\n"
"checking", None))
        self.push_size.setText(QCoreApplication.translate("Camera", u"View character sizes", None))
        self.label.setText(QCoreApplication.translate("Camera", u"Exposure Compensation:", None))
        self.takeImageButton.setText(QCoreApplication.translate("Camera", u"Capture image", None))
        self.label_result.setText(QCoreApplication.translate("Camera", u"Step-by-step checking result:", None))
        self.label_sol_grade.setText(QCoreApplication.translate("Camera", u"Solution:", None))
        self.label_fa_grade.setText(QCoreApplication.translate("Camera", u"Final Answer:", None))
        self.label_overall_grade.setText(QCoreApplication.translate("Camera", u"Overall:", None))
        self.label_latex.setText(QCoreApplication.translate("Camera", u"OCR-processed solution in LaTeX: ", None))
        self.push_save.setText(QCoreApplication.translate("Camera", u"Record and check another solution", None))
        self.push_view_ak.setText(QCoreApplication.translate("Camera", u"View AK(s)", None))
        self.label_image_2.setText(QCoreApplication.translate("Camera", u"Source file preview\n"
"360x300", None))
        self.label_ak_count.setText(QCoreApplication.translate("Camera", u"\n"
"AK 1: SOL steps = 0, FA weight: 20", None))
        self.push_view_has.setText(QCoreApplication.translate("Camera", u"View solution(s)", None))
        self.label_counter.setText(QCoreApplication.translate("Camera", u"No. of solutions recorded:\n"
" 0", None))
        self.label_last_name.setText(QCoreApplication.translate("Camera", u"Last checked from:\n"
" None", None))
        self.edit_student_name.setText("")
        self.edit_student_name.setPlaceholderText(QCoreApplication.translate("Camera", u"May auto-fill after scan if none", None))
        self.label_student_name.setText(QCoreApplication.translate("Camera", u"Name:", None))
        self.label_ocr_time.setText(QCoreApplication.translate("Camera", u"OCR processing runtime:\n"
" 0.00s", None))
        self.label_check_time.setText(QCoreApplication.translate("Camera", u"Solution checking runtime:\n"
" 0.00s", None))
        self.label_prob_count.setText(QCoreApplication.translate("Camera", u"No. of problems aimed to\n"
"solve by the solution: 0 ", None))
        self.label_total_time.setText(QCoreApplication.translate("Camera", u"Total runtime from capture\n"
"to result display: 0.00s", None))
        self.menuFile.setTitle(QCoreApplication.translate("Camera", u"File", None))
        self.menuDevices.setTitle(QCoreApplication.translate("Camera", u"Devices", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Camera", u"Help", None))
    # retranslateUi

