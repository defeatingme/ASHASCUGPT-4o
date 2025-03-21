# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ak_camera_ui_2.ui'
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QStatusBar,
    QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(1280, 800)
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
        self.stackedWidget.setGeometry(QRect(10, 0, 820, 710))
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
        self.push_save.setGeometry(QRect(960, 720, 301, 25))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(False)
        self.push_save.setFont(font)
        self.push_save.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
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
        self.push_back = QPushButton(self.centralwidget)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 720, 121, 25))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.push_back.setFont(font1)
        self.push_back.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
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
        self.push_back.setCheckable(False)
        self.frame_latex = QFrame(self.centralwidget)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(839, 10, 431, 411))
        font2 = QFont()
        font2.setPointSize(11)
        self.frame_latex.setFont(font2)
        self.frame_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 30, 431, 360))
        self.web_latex.setFont(font2)
        self.web_latex.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 431, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setUnderline(False)
        self.label_latex.setFont(font3)
        self.label_latex.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"border: 1px solid  rgb(208, 172, 220);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(850, 400, 411, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(True)
        self.label_time.setFont(font4)
        self.label_time.setStyleSheet(u"background-color: None;\n"
"color: rgb(224, 224, 224);")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(950, 430, 321, 281))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeImageButton = QPushButton(self.centralwidget)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(False)
        self.takeImageButton.setGeometry(QRect(650, 720, 180, 25))
        self.takeImageButton.setFont(font)
        self.takeImageButton.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
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
        self.push_redo = QPushButton(self.centralwidget)
        self.push_redo.setObjectName(u"push_redo")
        self.push_redo.setGeometry(QRect(470, 720, 151, 25))
        self.push_redo.setFont(font)
        self.push_redo.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
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
        self.push_redo.setCheckable(False)
        self.push_size = QPushButton(self.centralwidget)
        self.push_size.setObjectName(u"push_size")
        self.push_size.setGeometry(QRect(280, 720, 181, 25))
        self.push_size.setFont(font)
        self.push_size.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
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
        self.push_size.setCheckable(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(840, 430, 101, 311))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 101, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: None;\n"
"border: None;\n"
"color:  rgb(224, 224, 224)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exposureCompensation = QSlider(self.frame)
        self.exposureCompensation.setObjectName(u"exposureCompensation")
        self.exposureCompensation.setGeometry(QRect(30, 60, 31, 241))
        self.exposureCompensation.setStyleSheet(u"background-color: None;\n"
"border: None;")
        self.exposureCompensation.setMinimum(-4)
        self.exposureCompensation.setMaximum(4)
        self.exposureCompensation.setPageStep(2)
        self.exposureCompensation.setOrientation(Qt.Orientation.Vertical)
        self.exposureCompensation.setTickPosition(QSlider.TickPosition.TicksAbove)
        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224)")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevices = QMenu(self.menubar)
        self.menuDevices.setObjectName(u"menuDevices")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Camera)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(64, 64, 64)")
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
        self.push_save.setText(QCoreApplication.translate("Camera", u"Submit and close", None))
        self.push_back.setText(QCoreApplication.translate("Camera", u"Back", None))
        self.label_latex.setText(QCoreApplication.translate("Camera", u"OCR-processed solution in LaTeX:", None))
        self.label_time.setText(QCoreApplication.translate("Camera", u"Runtime: 0.00s", None))
        self.label_2.setText(QCoreApplication.translate("Camera", u"Image preview\n"
"320x280p", None))
        self.takeImageButton.setText(QCoreApplication.translate("Camera", u"Capture image", None))
        self.push_redo.setText(QCoreApplication.translate("Camera", u"Redo OCR", None))
        self.push_size.setText(QCoreApplication.translate("Camera", u"View character sizes", None))
        self.label.setText(QCoreApplication.translate("Camera", u"Exposure\n"
"compensation", None))
        self.menuFile.setTitle(QCoreApplication.translate("Camera", u"File", None))
        self.menuDevices.setTitle(QCoreApplication.translate("Camera", u"Devices", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Camera", u"Help", None))
    # retranslateUi

