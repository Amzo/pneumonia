from PySide2.QtWidgets import  QMainWindow
from PySide2.QtCore import QProcess
from PySide2.QtGui import QImage, QPixmap

#Import our generated class to create a child class
from gui.ui.ui_mainwindow import Ui_MainWindow

from lib import file
from lib import errors
from client import connect as server

class MainWindow(QMainWindow):
    # default arguements
    arguments = ['--train', '-i', 'data/ct/train', '-c', 'data/ct/test', '--inputValidate', 'data/ct/validate']
    
    # folder location
    trainImageFolder = ''
    testImageFolder = ''
    valImageFolder = ''

    # if running out of memory try a lower batch size
    batchSize = 64

    allOptimiser = ['adam', 'adadelta', 'adagrad', 'adamax', 'ftrl', 'nadam', 'rmsprop']
 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.p = None
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

    def getPrediction(self):
        self.ui.lblPredict.setText("Sending image file")
        server.sendImage(self.imageFile)

        pred = server.receivePred()
        self.ui.lblPredict.setText(pred)

    def startProcess(self):
        if self.p is None:  # No process running.
            self.message("Executing process", "green")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            print(self.arguments)
            self.p.start("./models/cnn.py", self.arguments)

    def handle_stderr(self):
        output = str(self.p.readAllStandardError(), 'utf-8')
        self.message(output, "red")

    def handle_stdout(self):
        output = str(self.p.readAllStandardOutput(), 'utf-8')
        self.message(output, "blue")

    def handle_state(self, state):
        states = {   
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]

        self.message(f"State changed: {state_name}", "green")

    def process_finished(self):
        self.message("Process finished.", "green")
        self.p = None


