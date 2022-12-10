# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import resource_rc

class MainwindowUi(object):
    def setupUi(self, MainwindowUi):
        if not MainwindowUi.objectName():
            MainwindowUi.setObjectName(u"MainwindowUi")
        MainwindowUi.resize(900, 630)
        MainwindowUi.setMaximumSize(QSize(900, 630))
        self.centralwidget = QWidget(MainwindowUi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 881, 611))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.vloToolbar = QVBoxLayout()
        self.vloToolbar.setSpacing(0)
        self.vloToolbar.setObjectName(u"vloToolbar")
        self.vloToolbar.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gpbBodies = QGroupBox(self.horizontalLayoutWidget)
        self.gpbBodies.setObjectName(u"gpbBodies")
        self.gpbBodies.setMaximumSize(QSize(255, 150))
        self.lstBodies = QListWidget(self.gpbBodies)
        self.lstBodies.setObjectName(u"lstBodies")
        self.lstBodies.setGeometry(QRect(5, 21, 241, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstBodies.sizePolicy().hasHeightForWidth())
        self.lstBodies.setSizePolicy(sizePolicy)

        self.vloToolbar.addWidget(self.gpbBodies)

        self.gpbEdit = QGroupBox(self.horizontalLayoutWidget)
        self.gpbEdit.setObjectName(u"gpbEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gpbEdit.sizePolicy().hasHeightForWidth())
        self.gpbEdit.setSizePolicy(sizePolicy1)
        self.gpbEdit.setMaximumSize(QSize(255, 250))
        self.verticalLayoutWidget = QWidget(self.gpbEdit)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 241, 221))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gloPosSpd = QGridLayout()
        self.gloPosSpd.setObjectName(u"gloPosSpd")
        self.lblPos = QLabel(self.verticalLayoutWidget)
        self.lblPos.setObjectName(u"lblPos")

        self.gloPosSpd.addWidget(self.lblPos, 0, 0, 1, 1)

        self.lblSpdY = QLabel(self.verticalLayoutWidget)
        self.lblSpdY.setObjectName(u"lblSpdY")
        self.lblSpdY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gloPosSpd.addWidget(self.lblSpdY, 1, 3, 1, 1)

        self.lblSpdX = QLabel(self.verticalLayoutWidget)
        self.lblSpdX.setObjectName(u"lblSpdX")
        self.lblSpdX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gloPosSpd.addWidget(self.lblSpdX, 1, 1, 1, 1)

        self.lblSpd = QLabel(self.verticalLayoutWidget)
        self.lblSpd.setObjectName(u"lblSpd")

        self.gloPosSpd.addWidget(self.lblSpd, 1, 0, 1, 1)

        self.lblPosY = QLabel(self.verticalLayoutWidget)
        self.lblPosY.setObjectName(u"lblPosY")
        self.lblPosY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gloPosSpd.addWidget(self.lblPosY, 0, 3, 1, 1)

        self.spbPosY = QSpinBox(self.verticalLayoutWidget)
        self.spbPosY.setObjectName(u"spbPosY")
        self.spbPosY.setEnabled(True)
        self.spbPosY.setMinimum(-310)
        self.spbPosY.setMaximum(310)

        self.gloPosSpd.addWidget(self.spbPosY, 0, 4, 1, 1)

        self.lblPosX = QLabel(self.verticalLayoutWidget)
        self.lblPosX.setObjectName(u"lblPosX")
        self.lblPosX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gloPosSpd.addWidget(self.lblPosX, 0, 1, 1, 1)

        self.spbPosX = QSpinBox(self.verticalLayoutWidget)
        self.spbPosX.setObjectName(u"spbPosX")
        self.spbPosX.setEnabled(True)
        self.spbPosX.setMinimum(-310)
        self.spbPosX.setMaximum(310)

        self.gloPosSpd.addWidget(self.spbPosX, 0, 2, 1, 1)

        self.spbSpdY = QSpinBox(self.verticalLayoutWidget)
        self.spbSpdY.setObjectName(u"spbSpdY")
        self.spbSpdY.setEnabled(True)
        self.spbSpdY.setMinimum(-500)
        self.spbSpdY.setMaximum(500)

        self.gloPosSpd.addWidget(self.spbSpdY, 1, 4, 1, 1)

        self.spbSpdX = QSpinBox(self.verticalLayoutWidget)
        self.spbSpdX.setObjectName(u"spbSpdX")
        self.spbSpdX.setEnabled(True)
        self.spbSpdX.setMinimum(-500)
        self.spbSpdX.setMaximum(500)

        self.gloPosSpd.addWidget(self.spbSpdX, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gloPosSpd)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spbMass = QSpinBox(self.verticalLayoutWidget)
        self.spbMass.setObjectName(u"spbMass")
        self.spbMass.setEnabled(True)
        self.spbMass.setMinimum(1)
        self.spbMass.setMaximum(1000000)
        self.spbMass.setValue(1)

        self.gridLayout.addWidget(self.spbMass, 0, 1, 1, 1)

        self.spbRadius = QSpinBox(self.verticalLayoutWidget)
        self.spbRadius.setObjectName(u"spbRadius")
        self.spbRadius.setEnabled(True)
        self.spbRadius.setMinimum(1)
        self.spbRadius.setMaximum(100)
        self.spbRadius.setValue(10)

        self.gridLayout.addWidget(self.spbRadius, 1, 1, 1, 1)

        self.lblRadius = QLabel(self.verticalLayoutWidget)
        self.lblRadius.setObjectName(u"lblRadius")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblRadius.sizePolicy().hasHeightForWidth())
        self.lblRadius.setSizePolicy(sizePolicy2)
        self.lblRadius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblRadius, 1, 0, 1, 1)

        self.lblMass = QLabel(self.verticalLayoutWidget)
        self.lblMass.setObjectName(u"lblMass")
        sizePolicy2.setHeightForWidth(self.lblMass.sizePolicy().hasHeightForWidth())
        self.lblMass.setSizePolicy(sizePolicy2)
        self.lblMass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblMass, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.btnAdd = QPushButton(self.verticalLayoutWidget)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(26)
        sizePolicy3.setVerticalStretch(26)
        sizePolicy3.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy3)
        self.btnAdd.setMinimumSize(QSize(0, 0))
        self.btnAdd.setMaximumSize(QSize(26, 26))
        self.btnAdd.setToolTipDuration(2)
        icon = QIcon()
        icon.addFile(u":/icon/icons/free-icon-font-plus-3917757.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAdd.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(self.verticalLayoutWidget)
        self.btnEdit.setObjectName(u"btnEdit")
        sizePolicy3.setHeightForWidth(self.btnEdit.sizePolicy().hasHeightForWidth())
        self.btnEdit.setSizePolicy(sizePolicy3)
        self.btnEdit.setMaximumSize(QSize(26, 26))
        self.btnEdit.setToolTipDuration(2)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/free-icon-font-pencil-3917651.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEdit.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setObjectName(u"btnDelete")
        sizePolicy3.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy3)
        self.btnDelete.setMaximumSize(QSize(26, 26))
        self.btnDelete.setToolTipDuration(2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/free-icon-font-trash-3917772.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDelete.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btnDelete)

        self.btnSave = QPushButton(self.verticalLayoutWidget)
        self.btnSave.setObjectName(u"btnSave")
        sizePolicy3.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy3)
        self.btnSave.setMaximumSize(QSize(26, 26))
        self.btnSave.setToolTipDuration(2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/free-icon-font-download-3917768.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.btnSave)

        self.btnLoad = QPushButton(self.verticalLayoutWidget)
        self.btnLoad.setObjectName(u"btnLoad")
        sizePolicy3.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy3)
        self.btnLoad.setMaximumSize(QSize(26, 26))
        self.btnLoad.setToolTipDuration(2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/free-icon-font-upload-3917769.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoad.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btnLoad)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.vloToolbar.addWidget(self.gpbEdit)

        self.gpbSettings = QGroupBox(self.horizontalLayoutWidget)
        self.gpbSettings.setObjectName(u"gpbSettings")
        sizePolicy1.setHeightForWidth(self.gpbSettings.sizePolicy().hasHeightForWidth())
        self.gpbSettings.setSizePolicy(sizePolicy1)
        self.gpbSettings.setMaximumSize(QSize(255, 150))
        self.verticalLayoutWidget_3 = QWidget(self.gpbSettings)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 15, 241, 131))
        self.vloSimSettings = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vloSimSettings.setObjectName(u"vloSimSettings")
        self.vloSimSettings.setContentsMargins(0, 0, 0, 0)
        self.cbxDrawTrails = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawTrails.setObjectName(u"cbxDrawTrails")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbxDrawTrails.sizePolicy().hasHeightForWidth())
        self.cbxDrawTrails.setSizePolicy(sizePolicy4)

        self.vloSimSettings.addWidget(self.cbxDrawTrails)

        self.cbxDrawSpdVects = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawSpdVects.setObjectName(u"cbxDrawSpdVects")
        sizePolicy4.setHeightForWidth(self.cbxDrawSpdVects.sizePolicy().hasHeightForWidth())
        self.cbxDrawSpdVects.setSizePolicy(sizePolicy4)

        self.vloSimSettings.addWidget(self.cbxDrawSpdVects)

        self.cbxDrawMassCenter = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawMassCenter.setObjectName(u"cbxDrawMassCenter")
        sizePolicy4.setHeightForWidth(self.cbxDrawMassCenter.sizePolicy().hasHeightForWidth())
        self.cbxDrawMassCenter.setSizePolicy(sizePolicy4)

        self.vloSimSettings.addWidget(self.cbxDrawMassCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cbxColorDependent = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxColorDependent.setObjectName(u"cbxColorDependent")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cbxColorDependent.sizePolicy().hasHeightForWidth())
        self.cbxColorDependent.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.cbxColorDependent)

        self.cbbColorDependsOn = QComboBox(self.verticalLayoutWidget_3)
        self.cbbColorDependsOn.addItem("")
        self.cbbColorDependsOn.addItem("")
        self.cbbColorDependsOn.setObjectName(u"cbbColorDependsOn")
        sizePolicy5.setHeightForWidth(self.cbbColorDependsOn.sizePolicy().hasHeightForWidth())
        self.cbbColorDependsOn.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.cbbColorDependsOn)


        self.vloSimSettings.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSimStart = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStart.setObjectName(u"btnSimStart")
        self.btnSimStart.setMaximumSize(QSize(23, 23))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStart.setIcon(icon5)
        self.btnSimStart.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStart)

        self.btnSimStep = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStep.setObjectName(u"btnSimStep")
        self.btnSimStep.setMaximumSize(QSize(23, 23))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/step.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStep.setIcon(icon6)
        self.btnSimStep.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStep)

        self.btnSimStop = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStop.setObjectName(u"btnSimStop")
        self.btnSimStop.setMaximumSize(QSize(23, 23))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStop.setIcon(icon7)
        self.btnSimStop.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStop)

        self.btnShowHeatMap = QPushButton(self.verticalLayoutWidget_3)
        self.btnShowHeatMap.setObjectName(u"btnShowHeatMap")
        sizePolicy5.setHeightForWidth(self.btnShowHeatMap.sizePolicy().hasHeightForWidth())
        self.btnShowHeatMap.setSizePolicy(sizePolicy5)
        self.btnShowHeatMap.setMinimumSize(QSize(23, 23))
        self.btnShowHeatMap.setMaximumSize(QSize(23, 23))
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/free-icon-font-layers-3917233.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnShowHeatMap.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.btnShowHeatMap)


        self.vloSimSettings.addLayout(self.horizontalLayout_2)


        self.vloToolbar.addWidget(self.gpbSettings)

        self.lblCreator = QLabel(self.horizontalLayoutWidget)
        self.lblCreator.setObjectName(u"lblCreator")
        self.lblCreator.setMaximumSize(QSize(16777215, 20))
        self.lblCreator.setAlignment(Qt.AlignCenter)

        self.vloToolbar.addWidget(self.lblCreator)


        self.horizontalLayout.addLayout(self.vloToolbar)

        self.lblSimulationDisplay = QLabel(self.horizontalLayoutWidget)
        self.lblSimulationDisplay.setObjectName(u"lblSimulationDisplay")
        sizePolicy.setHeightForWidth(self.lblSimulationDisplay.sizePolicy().hasHeightForWidth())
        self.lblSimulationDisplay.setSizePolicy(sizePolicy)
        self.lblSimulationDisplay.setMaximumSize(QSize(610, 610))
        self.lblSimulationDisplay.setFrameShape(QFrame.Panel)
        self.lblSimulationDisplay.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.lblSimulationDisplay)

        MainwindowUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainwindowUi)
        self.cbxColorDependent.clicked["bool"].connect(self.cbbColorDependsOn.setEnabled)

        QMetaObject.connectSlotsByName(MainwindowUi)
    # setupUi

    def retranslateUi(self, MainwindowUi):
        MainwindowUi.setWindowTitle(QCoreApplication.translate("MainwindowUi", u"PyGravSim", None))
        self.gpbBodies.setTitle(QCoreApplication.translate("MainwindowUi", u"\u0422\u0435\u043b\u0430", None))
        self.gpbEdit.setTitle(QCoreApplication.translate("MainwindowUi", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lblPos.setText(QCoreApplication.translate("MainwindowUi", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435:", None))
        self.lblSpdY.setText(QCoreApplication.translate("MainwindowUi", u"Y:", None))
        self.lblSpdX.setText(QCoreApplication.translate("MainwindowUi", u"X:", None))
        self.lblSpd.setText(QCoreApplication.translate("MainwindowUi", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.lblPosY.setText(QCoreApplication.translate("MainwindowUi", u"Y:", None))
        self.lblPosX.setText(QCoreApplication.translate("MainwindowUi", u"X:", None))
        self.lblRadius.setText(QCoreApplication.translate("MainwindowUi", u"\u0420\u0430\u0434\u0438\u0443\u0441:", None))
        self.lblMass.setText(QCoreApplication.translate("MainwindowUi", u"\u041c\u0430\u0441\u0441\u0430:", None))
#if QT_CONFIG(tooltip)
        self.btnAdd.setToolTip(QCoreApplication.translate("MainwindowUi", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u043b\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.btnAdd.setText("")
#if QT_CONFIG(tooltip)
        self.btnEdit.setToolTip(QCoreApplication.translate("MainwindowUi", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u043b\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.btnEdit.setText("")
#if QT_CONFIG(tooltip)
        self.btnDelete.setToolTip(QCoreApplication.translate("MainwindowUi", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0435\u043b\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.btnDelete.setText("")
#if QT_CONFIG(tooltip)
        self.btnSave.setToolTip(QCoreApplication.translate("MainwindowUi", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.btnSave.setText("")
#if QT_CONFIG(tooltip)
        self.btnLoad.setToolTip(QCoreApplication.translate("MainwindowUi", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.btnLoad.setText("")
        self.gpbSettings.setTitle(QCoreApplication.translate("MainwindowUi", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.cbxDrawTrails.setText(QCoreApplication.translate("MainwindowUi", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0442\u0440\u0430\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
        self.cbxDrawSpdVects.setText(QCoreApplication.translate("MainwindowUi", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0432\u0435\u043a\u0442\u043e\u0440\u044b \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0435\u0439", None))
        self.cbxDrawMassCenter.setText(QCoreApplication.translate("MainwindowUi", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0431\u0430\u0440\u0438\u0446\u0435\u043d\u0442\u0440", None))
        self.cbxColorDependent.setText(QCoreApplication.translate("MainwindowUi", u"\u0426\u0432\u0435\u0442 \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442", None))
        self.cbbColorDependsOn.setItemText(0, QCoreApplication.translate("MainwindowUi", u"\u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438", None))
        self.cbbColorDependsOn.setItemText(1, QCoreApplication.translate("MainwindowUi", u"\u0443\u0441\u043a\u043e\u0440\u0435\u043d\u0438\u044f", None))

        self.btnSimStart.setText("")
        self.btnSimStep.setText("")
        self.btnSimStop.setText("")
        self.btnShowHeatMap.setText("")
        self.lblCreator.setText(QCoreApplication.translate("MainwindowUi", u"by Egor Kosachev | Distributed via MIT Liscence", None))
        self.lblSimulationDisplay.setText("")
    # retranslateUi

