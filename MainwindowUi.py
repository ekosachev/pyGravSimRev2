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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)
import resource_rc

class MainwindowUi(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 630)
        MainWindow.setMaximumSize(QSize(900, 630))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 9, 891, 611))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.sim_tab = QWidget()
        self.sim_tab.setObjectName(u"sim_tab")
        self.horizontalLayoutWidget = QWidget(self.sim_tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 881, 581))
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
        self.gpbEdit.setMaximumSize(QSize(255, 250))
        self.verticalLayoutWidget = QWidget(self.gpbEdit)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 231, 201))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblRadius.sizePolicy().hasHeightForWidth())
        self.lblRadius.setSizePolicy(sizePolicy1)
        self.lblRadius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblRadius, 1, 0, 1, 1)

        self.lblMass = QLabel(self.verticalLayoutWidget)
        self.lblMass.setObjectName(u"lblMass")
        sizePolicy1.setHeightForWidth(self.lblMass.sizePolicy().hasHeightForWidth())
        self.lblMass.setSizePolicy(sizePolicy1)
        self.lblMass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblMass, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnDelete = QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.btnDelete, 1, 0, 1, 1)

        self.btnCopy = QPushButton(self.verticalLayoutWidget)
        self.btnCopy.setObjectName(u"btnCopy")
        self.btnCopy.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btnCopy.sizePolicy().hasHeightForWidth())
        self.btnCopy.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.btnCopy, 1, 1, 1, 1)

        self.btnNew = QPushButton(self.verticalLayoutWidget)
        self.btnNew.setObjectName(u"btnNew")

        self.gridLayout_2.addWidget(self.btnNew, 0, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.vloToolbar.addWidget(self.gpbEdit)

        self.gpbSettings = QGroupBox(self.horizontalLayoutWidget)
        self.gpbSettings.setObjectName(u"gpbSettings")
        self.gpbSettings.setMaximumSize(QSize(255, 150))
        self.verticalLayoutWidget_3 = QWidget(self.gpbSettings)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 19, 231, 127))
        self.vloSimSettings = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vloSimSettings.setObjectName(u"vloSimSettings")
        self.vloSimSettings.setContentsMargins(0, 0, 0, 0)
        self.cbxDrawTrails = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawTrails.setObjectName(u"cbxDrawTrails")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cbxDrawTrails.sizePolicy().hasHeightForWidth())
        self.cbxDrawTrails.setSizePolicy(sizePolicy3)

        self.vloSimSettings.addWidget(self.cbxDrawTrails)

        self.cbxDrawSpdVects = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawSpdVects.setObjectName(u"cbxDrawSpdVects")
        sizePolicy3.setHeightForWidth(self.cbxDrawSpdVects.sizePolicy().hasHeightForWidth())
        self.cbxDrawSpdVects.setSizePolicy(sizePolicy3)

        self.vloSimSettings.addWidget(self.cbxDrawSpdVects)

        self.cbxDrawMassCenter = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawMassCenter.setObjectName(u"cbxDrawMassCenter")
        sizePolicy3.setHeightForWidth(self.cbxDrawMassCenter.sizePolicy().hasHeightForWidth())
        self.cbxDrawMassCenter.setSizePolicy(sizePolicy3)

        self.vloSimSettings.addWidget(self.cbxDrawMassCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSimStart = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStart.setObjectName(u"btnSimStart")
        self.btnSimStart.setMaximumSize(QSize(23, 23))
        icon = QIcon()
        icon.addFile(u":/icon/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStart.setIcon(icon)
        self.btnSimStart.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStart)

        self.btnSimStep = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStep.setObjectName(u"btnSimStep")
        self.btnSimStep.setMaximumSize(QSize(23, 23))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/step.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStep.setIcon(icon1)
        self.btnSimStep.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStep)

        self.btnSimStop = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStop.setObjectName(u"btnSimStop")
        self.btnSimStop.setMaximumSize(QSize(23, 23))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStop.setIcon(icon2)
        self.btnSimStop.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStop)


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

        self.tabWidget.addTab(self.sim_tab, "")
        self.graphs_tab = QWidget()
        self.graphs_tab.setObjectName(u"graphs_tab")
        self.verticalLayoutWidget_4 = QWidget(self.graphs_tab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(9, 9, 871, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_position_graph = QLabel(self.verticalLayoutWidget_4)
        self.lbl_position_graph.setObjectName(u"lbl_position_graph")
        sizePolicy.setHeightForWidth(self.lbl_position_graph.sizePolicy().hasHeightForWidth())
        self.lbl_position_graph.setSizePolicy(sizePolicy)
        self.lbl_position_graph.setFrameShape(QFrame.Panel)
        self.lbl_position_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.lbl_position_graph)

        self.lbl_speed_graph = QLabel(self.verticalLayoutWidget_4)
        self.lbl_speed_graph.setObjectName(u"lbl_speed_graph")
        sizePolicy.setHeightForWidth(self.lbl_speed_graph.sizePolicy().hasHeightForWidth())
        self.lbl_speed_graph.setSizePolicy(sizePolicy)
        self.lbl_speed_graph.setFrameShape(QFrame.Panel)
        self.lbl_speed_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.lbl_speed_graph)

        self.tabWidget.addTab(self.graphs_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyGravSim", None))
        self.gpbBodies.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0430", None))
        self.gpbEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lblPos.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435:", None))
        self.lblSpdY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lblSpdX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lblSpd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.lblPosY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lblPosX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lblRadius.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441:", None))
        self.lblMass.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0441\u0430:", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnCopy.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.gpbSettings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.cbxDrawTrails.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0441\u043b\u0435\u0434", None))
        self.cbxDrawSpdVects.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0432\u0435\u043a\u0442\u043e\u0440\u044b \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0435\u0439", None))
        self.cbxDrawMassCenter.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0446\u0435\u043d\u0442\u0440 \u043c\u0430\u0441\u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.btnSimStart.setText("")
        self.btnSimStep.setText("")
        self.btnSimStop.setText("")
        self.lblCreator.setText(QCoreApplication.translate("MainWindow", u"by Egor Kosachev | Distributed via MIT License", None))
        self.lblSimulationDisplay.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sim_tab), QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lbl_position_graph.setText("")
        self.lbl_speed_graph.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphs_tab), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

