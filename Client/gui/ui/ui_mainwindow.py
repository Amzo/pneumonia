# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/mainwindow.ui',
# licensing of 'gui/ui/mainwindow.ui' applies.
#
# Created: Thu May  6 15:17:56 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(903, 647)
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
        self.Predict = QtWidgets.QWidget()
        self.Predict.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Predict.sizePolicy().hasHeightForWidth())
        self.Predict.setSizePolicy(sizePolicy)
        self.Predict.setObjectName("Predict")
        self.gridLayout = QtWidgets.QGridLayout(self.Predict)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFilename = QtWidgets.QLabel(self.Predict)
        self.lblFilename.setMinimumSize(QtCore.QSize(0, 0))
        self.lblFilename.setMaximumSize(QtCore.QSize(16777215, 18))
        self.lblFilename.setObjectName("lblFilename")
        self.gridLayout.addWidget(self.lblFilename, 0, 0, 1, 1)
        self.picView = QtWidgets.QLabel(self.Predict)
        self.picView.setAutoFillBackground(True)
        self.picView.setText("")
        self.picView.setObjectName("picView")
        self.gridLayout.addWidget(self.picView, 1, 0, 1, 1)
        self.browseFilesButton = QtWidgets.QPushButton(self.Predict)
        self.browseFilesButton.setObjectName("browseFilesButton")
        self.gridLayout.addWidget(self.browseFilesButton, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.Predict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(850, 120))
        self.groupBox_3.setMaximumSize(QtCore.QSize(0, 120))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.modelList = QtWidgets.QComboBox(self.groupBox_3)
        self.modelList.setMaximumSize(QtCore.QSize(75, 25))
        self.modelList.setObjectName("modelList")
        self.modelList.addItem("")
        self.modelList.addItem("")
        self.modelList.addItem("")
        self.horizontalLayout.addWidget(self.modelList)
        self.useBruteForce = QtWidgets.QRadioButton(self.groupBox_3)
        self.useBruteForce.setMaximumSize(QtCore.QSize(75, 25))
        self.useBruteForce.setObjectName("useBruteForce")
        self.horizontalLayout.addWidget(self.useBruteForce)
        self.saveModel = QtWidgets.QRadioButton(self.groupBox_3)
        self.saveModel.setMaximumSize(QtCore.QSize(75, 25))
        self.saveModel.setObjectName("saveModel")
        self.horizontalLayout.addWidget(self.saveModel)
        self.predictButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictButton.sizePolicy().hasHeightForWidth())
        self.predictButton.setSizePolicy(sizePolicy)
        self.predictButton.setObjectName("predictButton")
        self.horizontalLayout.addWidget(self.predictButton)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.Predict)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.lblPredict = QtWidgets.QLabel(self.groupBox)
        self.lblPredict.setText("")
        self.lblPredict.setObjectName("lblPredict")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblPredict)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.Predict, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 27))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lblFilename.setText(QtWidgets.QApplication.translate("MainWindow", "Selected Image: ", None, -1))
        self.browseFilesButton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse Files", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Model Options", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Model", None, -1))
        self.modelList.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "CNN", None, -1))
        self.modelList.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "ResNet50", None, -1))
        self.modelList.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "vgg16", None, -1))
        self.useBruteForce.setText(QtWidgets.QApplication.translate("MainWindow", "Remote", None, -1))
        self.saveModel.setText(QtWidgets.QApplication.translate("MainWindow", "Local", None, -1))
        self.predictButton.setText(QtWidgets.QApplication.translate("MainWindow", "Predict", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Prediction", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Predict), QtWidgets.QApplication.translate("MainWindow", "Train", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))

