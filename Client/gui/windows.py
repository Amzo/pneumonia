from PySide2.QtWidgets import  QMainWindow
from PySide2.QtCore import QProcess
from PySide2.QtGui import QImage, QPixmap

#Import our generated class to create a child class
from gui.ui.ui_mainwindow import Ui_MainWindow

from lib import file
from lib import errors
from client import connect as server

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connectSignalsSlots()
		self.model = ''
		self.imageFile = ''

	def connectSignalsSlots(self):
		imageFile = self.ui.browseFilesButton.clicked.connect(self.bbrowseFiles)
		self.ui.predictButton.clicked.connect(self.getPrediction)

	def bbrowseFiles(self):
		fileName = file.browseFiles()
		pixmap = QPixmap(fileName[0])
		self.ui.lblFilename.setText("Selected Image: " + fileName[0]);
		self.ui.picView.setPixmap(pixmap.scaled(self.ui.picView.width(),self.ui.picView.height()))
		self.imageFile = fileName[0]

	def sendModels(self):
		self.model = str(self.ui.modelList.currentText())
		server.sendModel(self.model)

	def getPrediction(self):
		self.ui.lblPredict.setText("Sending image file")
		server.sendImage(self.imageFile)

		self.sendModels()

		pred = server.receivePred()
		self.ui.lblPredict.setText(pred)
