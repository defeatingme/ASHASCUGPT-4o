# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ak_camera_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QStatusBar,
    QWidget)

class Ui_AK_Camera(object):
    def setupUi(self, AK_Camera):
        if not AK_Camera.objectName():
            AK_Camera.setObjectName(u"AK_Camera")
        AK_Camera.resize(1080, 720)
        AK_Camera.setStyleSheet(u"background-color:qconicalgradient(cx:0, cy:1, angle:159.4, stop:0 rgba(212, 161, 205, 255), stop:1 rgba(71, 71, 71, 255))")
        self.actionExit = QAction(AK_Camera)
        self.actionExit.setObjectName(u"actionExit")
        self.actionStartCamera = QAction(AK_Camera)
        self.actionStartCamera.setObjectName(u"actionStartCamera")
        self.actionStopCamera = QAction(AK_Camera)
        self.actionStopCamera.setObjectName(u"actionStopCamera")
        self.actionSettings = QAction(AK_Camera)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout_Qt = QAction(AK_Camera)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(AK_Camera)
        self.centralwidget.setObjectName(u"centralwidget")
        self.captureFrame = QFrame(self.centralwidget)
        self.captureFrame.setObjectName(u"captureFrame")
        self.captureFrame.setGeometry(QRect(110, 560, 611, 71))
        self.exposureCompensation = QSlider(self.captureFrame)
        self.exposureCompensation.setObjectName(u"exposureCompensation")
        self.exposureCompensation.setGeometry(QRect(40, 40, 141, 21))
        self.exposureCompensation.setStyleSheet(u"background-color: None;\n"
"border: None\n"
"")
        self.exposureCompensation.setMinimum(-4)
        self.exposureCompensation.setMaximum(4)
        self.exposureCompensation.setPageStep(2)
        self.exposureCompensation.setOrientation(Qt.Orientation.Horizontal)
        self.exposureCompensation.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.label_exposure = QLabel(self.captureFrame)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(40, 0, 141, 41))
        font = QFont()
        font.setBold(True)
        self.label_exposure.setFont(font)
        self.label_exposure.setStyleSheet(u"background-color: None;\n"
"border: None;\n"
"color: #eee;")
        self.label_exposure.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeImageButton = QPushButton(self.captureFrame)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(False)
        self.takeImageButton.setGeometry(QRect(240, 10, 141, 24))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.takeImageButton.setFont(font1)
        self.takeImageButton.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_retake = QPushButton(self.captureFrame)
        self.push_retake.setObjectName(u"push_retake")
        self.push_retake.setGeometry(QRect(240, 40, 141, 21))
        self.push_retake.setFont(font1)
        self.push_retake.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_retake.setCheckable(False)
        self.push_start = QPushButton(self.captureFrame)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setGeometry(QRect(410, 30, 181, 25))
        self.push_start.setFont(font1)
        self.push_start.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_start.setCheckable(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 10, 720, 540))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(71, 71, 71, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
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
        self.push_back.setGeometry(QRect(20, 650, 121, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.push_back.setFont(font2)
        self.push_back.setStyleSheet(u"background-color: #333;\n"
"color: rgb(208, 172, 220)\n"
"")
        self.push_back.setCheckable(False)
        self.label_latex = QLabel(self.centralwidget)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(750, 20, 300, 400))
        self.label_latex.setFont(font2)
        self.label_latex.setStyleSheet(u"background-color: #eee;\n"
"color: #333")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_ak = QLabel(self.centralwidget)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(750, 0, 241, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_ak.setFont(font3)
        self.label_ak.setStyleSheet(u"background-color: None;\n"
"color: #eee")
        self.label_ak.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(780, 430, 240, 240))
        self.label_image.setStyleSheet(u"border: 1px solid  #eee;\n"
"background-color: rgb(71, 71, 71);\n"
"color: #eee")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        AK_Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AK_Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 21))
        self.menubar.setStyleSheet(u"background-color: #eee; \n"
"color: #333")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevices = QMenu(self.menubar)
        self.menuDevices.setObjectName(u"menuDevices")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        AK_Camera.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AK_Camera)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: #eee")
        AK_Camera.setStatusBar(self.statusbar)

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

        self.retranslateUi(AK_Camera)
        self.takeImageButton.clicked.connect(AK_Camera.takeImage)
        self.exposureCompensation.valueChanged.connect(AK_Camera.setExposureCompensation)
        self.actionExit.triggered.connect(AK_Camera.close)
        self.actionSettings.triggered.connect(AK_Camera.configureCaptureSettings)
        self.actionStartCamera.triggered.connect(AK_Camera.startCamera)
        self.actionStopCamera.triggered.connect(AK_Camera.stopCamera)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AK_Camera)
    # setupUi

    def retranslateUi(self, AK_Camera):
        AK_Camera.setWindowTitle(QCoreApplication.translate("AK_Camera", u"Camera", None))
        self.actionExit.setText(QCoreApplication.translate("AK_Camera", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("AK_Camera", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionStartCamera.setText(QCoreApplication.translate("AK_Camera", u"Start Camera", None))
        self.actionStopCamera.setText(QCoreApplication.translate("AK_Camera", u"Stop Camera", None))
        self.actionSettings.setText(QCoreApplication.translate("AK_Camera", u"Change Settings", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("AK_Camera", u"About Qt", None))
        self.label_exposure.setText(QCoreApplication.translate("AK_Camera", u"Exposure Compensation:", None))
        self.takeImageButton.setText(QCoreApplication.translate("AK_Camera", u"Capture", None))
        self.push_retake.setText(QCoreApplication.translate("AK_Camera", u"Retake", None))
        self.push_start.setText(QCoreApplication.translate("AK_Camera", u"Submit Answer Key", None))
        self.lastImagePreviewLabel.setText("")
        self.push_back.setText(QCoreApplication.translate("AK_Camera", u"Back to Home", None))
        self.label_latex.setText(QCoreApplication.translate("AK_Camera", u"Rendered LaTeX\n"
"300x400px", None))
        self.label_ak.setText(QCoreApplication.translate("AK_Camera", u"Answer Key in LaTeX", None))
        self.label_image.setText(QCoreApplication.translate("AK_Camera", u"Image Preview\n"
"240x240", None))
        self.menuFile.setTitle(QCoreApplication.translate("AK_Camera", u"File", None))
        self.menuDevices.setTitle(QCoreApplication.translate("AK_Camera", u"Devices", None))
        self.menuHelp.setTitle(QCoreApplication.translate("AK_Camera", u"Help", None))
    # retranslateUi

