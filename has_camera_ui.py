# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'has_camera_ui_2.ui'
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
    QStatusBar, QTabWidget, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(1350, 760)
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
        self.captureWidget = QTabWidget(self.centralwidget)
        self.captureWidget.setObjectName(u"captureWidget")
        self.captureWidget.setGeometry(QRect(750, 280, 180, 360))
        self.captureWidget.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 2px;\n"
"color: rgb(224, 224, 224);\n"
"")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.takeImageButton = QPushButton(self.tab_2)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(False)
        self.takeImageButton.setGeometry(QRect(10, 290, 151, 24))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        self.takeImageButton.setFont(font)
        self.takeImageButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(48, 48, 48);\n"
"color:  rgb(128, 128, 128);\n"
"border: 1px solid rgb(128, 128, 128);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.exposureCompensation = QSlider(self.tab_2)
        self.exposureCompensation.setObjectName(u"exposureCompensation")
        self.exposureCompensation.setGeometry(QRect(10, 60, 151, 41))
        self.exposureCompensation.setStyleSheet(u"background-color: None;\n"
"border: None;")
        self.exposureCompensation.setMinimum(-4)
        self.exposureCompensation.setMaximum(4)
        self.exposureCompensation.setPageStep(2)
        self.exposureCompensation.setOrientation(Qt.Orientation.Horizontal)
        self.exposureCompensation.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 161, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: None;\n"
"border: None;\n"
"color: rgb(224, 224, 224);\n"
"")
        self.captureWidget.addTab(self.tab_2, "")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 740, 680))
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
        self.push_save = QPushButton(self.centralwidget)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(960, 680, 361, 25))
        self.push_save.setFont(font)
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
        self.push_back = QPushButton(self.centralwidget)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 690, 121, 21))
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
"border-radius: 4px\n"
"}\n"
"")
        self.push_back.setCheckable(False)
        self.frame_result = QFrame(self.centralwidget)
        self.frame_result.setObjectName(u"frame_result")
        self.frame_result.setGeometry(QRect(940, 330, 401, 340))
        self.frame_result.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_result.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result.setFrameShadow(QFrame.Shadow.Raised)
        self.label_result = QLabel(self.frame_result)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(0, 0, 401, 21))
        self.label_result.setFont(font1)
        self.label_result.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade = QLabel(self.frame_result)
        self.label_sol_grade.setObjectName(u"label_sol_grade")
        self.label_sol_grade.setGeometry(QRect(0, 300, 121, 40))
        self.label_sol_grade.setFont(font)
        self.label_sol_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade = QLabel(self.frame_result)
        self.label_fa_grade.setObjectName(u"label_fa_grade")
        self.label_fa_grade.setGeometry(QRect(120, 300, 120, 40))
        self.label_fa_grade.setFont(font)
        self.label_fa_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_fa_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_overall_grade = QLabel(self.frame_result)
        self.label_overall_grade.setObjectName(u"label_overall_grade")
        self.label_overall_grade.setGeometry(QRect(240, 300, 161, 40))
        self.label_overall_grade.setFont(font)
        self.label_overall_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_overall_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.web_result = QWebEngineView(self.frame_result)
        self.web_result.setObjectName(u"web_result")
        self.web_result.setGeometry(QRect(0, 20, 401, 281))
        self.web_result.setStyleSheet(u"background-color: rgb(64, 64, 64);")
        self.label_counter = QLabel(self.centralwidget)
        self.label_counter.setObjectName(u"label_counter")
        self.label_counter.setGeometry(QRect(750, 10, 181, 31))
        self.label_counter.setFont(font1)
        self.label_counter.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_last_name = QLabel(self.centralwidget)
        self.label_last_name.setObjectName(u"label_last_name")
        self.label_last_name.setGeometry(QRect(750, 50, 181, 31))
        self.label_last_name.setFont(font1)
        self.label_last_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_last_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.edit_student_name = QLineEdit(self.centralwidget)
        self.edit_student_name.setObjectName(u"edit_student_name")
        self.edit_student_name.setGeometry(QRect(500, 685, 240, 25))
        self.edit_student_name.setFont(font2)
        self.edit_student_name.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.label_student_name = QLabel(self.centralwidget)
        self.label_student_name.setObjectName(u"label_student_name")
        self.label_student_name.setGeometry(QRect(440, 690, 61, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setUnderline(False)
        self.label_student_name.setFont(font3)
        self.label_student_name.setStyleSheet(u"background-color: None;\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_student_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_note_autofill = QLabel(self.centralwidget)
        self.label_note_autofill.setObjectName(u"label_note_autofill")
        self.label_note_autofill.setGeometry(QRect(740, 690, 151, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setUnderline(False)
        self.label_note_autofill.setFont(font4)
        self.label_note_autofill.setStyleSheet(u"background-color: None;\n"
"color: rgb(208, 172, 220)")
        self.label_note_autofill.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_size = QPushButton(self.centralwidget)
        self.push_size.setObjectName(u"push_size")
        self.push_size.setGeometry(QRect(760, 650, 161, 21))
        self.push_size.setFont(font1)
        self.push_size.setStyleSheet(u"QPushButton {\n"
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
        self.push_size.setCheckable(False)
        self.frame_latex = QFrame(self.centralwidget)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(940, 10, 401, 311))
        self.frame_latex.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 19, 401, 291))
        self.web_latex.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 401, 21))
        self.label_latex.setFont(font3)
        self.label_latex.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_ocr_time = QLabel(self.centralwidget)
        self.label_ocr_time.setObjectName(u"label_ocr_time")
        self.label_ocr_time.setGeometry(QRect(750, 100, 181, 31))
        self.label_ocr_time.setFont(font1)
        self.label_ocr_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_ocr_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_check_time = QLabel(self.centralwidget)
        self.label_check_time.setObjectName(u"label_check_time")
        self.label_check_time.setGeometry(QRect(750, 140, 181, 31))
        self.label_check_time.setFont(font1)
        self.label_check_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_check_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_total_time = QLabel(self.centralwidget)
        self.label_total_time.setObjectName(u"label_total_time")
        self.label_total_time.setGeometry(QRect(750, 180, 181, 51))
        self.label_total_time.setFont(font1)
        self.label_total_time.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_total_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_view_ak = QPushButton(self.centralwidget)
        self.push_view_ak.setObjectName(u"push_view_ak")
        self.push_view_ak.setGeometry(QRect(140, 690, 121, 21))
        self.push_view_ak.setFont(font2)
        self.push_view_ak.setStyleSheet(u"QPushButton {\n"
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
        self.push_view_ak.setCheckable(False)
        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 21))
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

        self.captureWidget.setCurrentIndex(0)
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
        self.takeImageButton.setText(QCoreApplication.translate("Camera", u"Capture image", None))
        self.label.setText(QCoreApplication.translate("Camera", u"Exposure Compensation:", None))
        self.captureWidget.setTabText(self.captureWidget.indexOf(self.tab_2), QCoreApplication.translate("Camera", u"Image", None))
        self.lastImagePreviewLabel.setText("")
        self.push_save.setText(QCoreApplication.translate("Camera", u"Save and check another solution", None))
        self.push_back.setText(QCoreApplication.translate("Camera", u"Back to Session", None))
        self.label_result.setText(QCoreApplication.translate("Camera", u"Result:", None))
        self.label_sol_grade.setText(QCoreApplication.translate("Camera", u"Solution:", None))
        self.label_fa_grade.setText(QCoreApplication.translate("Camera", u"Final Answer:", None))
        self.label_overall_grade.setText(QCoreApplication.translate("Camera", u"Overall:", None))
        self.label_counter.setText(QCoreApplication.translate("Camera", u"No. of solutions checked:\n"
" 0", None))
        self.label_last_name.setText(QCoreApplication.translate("Camera", u"Last checked from:\n"
" None", None))
        self.edit_student_name.setText("")
        self.edit_student_name.setPlaceholderText(QCoreApplication.translate("Camera", u"Optional/Auto-fill", None))
        self.label_student_name.setText(QCoreApplication.translate("Camera", u"Name/ID:", None))
        self.label_note_autofill.setText(QCoreApplication.translate("Camera", u"*May auto-fill after scan if none", None))
        self.push_size.setText(QCoreApplication.translate("Camera", u"View character sizes", None))
        self.label_latex.setText(QCoreApplication.translate("Camera", u"Solution in LaTeX", None))
        self.label_ocr_time.setText(QCoreApplication.translate("Camera", u"OCR processing runtime:\n"
" 0.00s", None))
        self.label_check_time.setText(QCoreApplication.translate("Camera", u"Solution checking runtime:\n"
" 0.00s", None))
        self.label_total_time.setText(QCoreApplication.translate("Camera", u"Total runtime from capture to\n"
"result display:\n"
" 0.00s", None))
        self.push_view_ak.setText(QCoreApplication.translate("Camera", u"View answer key", None))
        self.menuFile.setTitle(QCoreApplication.translate("Camera", u"File", None))
        self.menuDevices.setTitle(QCoreApplication.translate("Camera", u"Devices", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Camera", u"Help", None))
    # retranslateUi

