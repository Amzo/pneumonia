# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/mainwindow.ui',
# licensing of 'gui/ui/mainwindow.ui' applies.
#
# Created: Wed Mar 31 14:58:12 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(994, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setEnabled(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectTrainFolderButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectTrainFolderButton.setObjectName("selectTrainFolderButton")
        self.horizontalLayout.addWidget(self.selectTrainFolderButton)
        self.selectTestFolderButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectTestFolderButton.setObjectName("selectTestFolderButton")
        self.horizontalLayout.addWidget(self.selectTestFolderButton)
        self.selectValFolderButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectValFolderButton.setEnabled(True)
        self.selectValFolderButton.setObjectName("selectValFolderButton")
        self.horizontalLayout.addWidget(self.selectValFolderButton)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)
        self.trainOutput = QtWidgets.QTextEdit(self.groupBox)
        self.trainOutput.setObjectName("trainOutput")
        self.gridLayout.addWidget(self.trainOutput, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMinimumSize(QtCore.QSize(120, 120))
        self.groupBox_3.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.modelList = QtWidgets.QComboBox(self.groupBox_3)
        self.modelList.setObjectName("modelList")
        self.modelList.addItem("")
        self.modelList.addItem("")
        self.modelList.addItem("")
        self.verticalLayout_2.addWidget(self.modelList)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.optimiserList = QtWidgets.QComboBox(self.groupBox_3)
        self.optimiserList.setObjectName("optimiserList")
        self.verticalLayout_2.addWidget(self.optimiserList)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.useBruteForce = QtWidgets.QRadioButton(self.groupBox_3)
        self.useBruteForce.setObjectName("useBruteForce")
        self.verticalLayout_2.addWidget(self.useBruteForce)
        self.saveModel = QtWidgets.QRadioButton(self.groupBox_3)
        self.saveModel.setObjectName("saveModel")
        self.verticalLayout_2.addWidget(self.saveModel)
        self.trainButton = QtWidgets.QPushButton(self.groupBox_3)
        self.trainButton.setObjectName("trainButton")
        self.verticalLayout_2.addWidget(self.trainButton)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 2, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.browseFilesButton = QtWidgets.QPushButton(self.tab_2)
        self.browseFilesButton.setGeometry(QtCore.QRect(210, 220, 89, 30))
        self.browseFilesButton.setObjectName("browseFilesButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 994, 27))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Folder Select", None, -1))
        self.selectTrainFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Train Folder", None, -1))
        self.selectTestFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Test Folder", None, -1))
        self.selectValFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Validation Folder", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Output:", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Model Options", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Model", None, -1))
        self.modelList.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "CNN", None, -1))
        self.modelList.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "ResNet50", None, -1))
        self.modelList.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "vgg16", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Optimiser", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Epochs", None, -1))
        self.lineEdit_2.setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Batch Size", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "32", None, -1))
        self.useBruteForce.setText(QtWidgets.QApplication.translate("MainWindow", "Bruteforce", None, -1))
        self.saveModel.setText(QtWidgets.QApplication.translate("MainWindow", "Save Model", None, -1))
        self.trainButton.setText(QtWidgets.QApplication.translate("MainWindow", "Train", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Train", None, -1))
        self.browseFilesButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Predict", None, -1))
