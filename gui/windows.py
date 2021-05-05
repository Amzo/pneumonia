from PySide2.QtWidgets import  QMainWindow
from PySide2.QtCore import QProcess

#Import our generated class to create a child class
from gui.ui.ui_mainwindow import Ui_MainWindow

from lib import file
from lib import errors

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


    def connectSignalsSlots(self):
        self.ui.browseFilesButton.clicked.connect(self.bbrowseFiles)
        self.ui.selectTestFolderButton.clicked.connect(self.selectTestFolder)
        self.ui.selectTrainFolderButton.clicked.connect(self.selectTrainFolder)
        self.ui.selectValFolderButton.clicked.connect(self.selectValFolder)
        self.ui.trainButton.clicked.connect(self.trainModel)
        self.ui.modelList.currentTextChanged.connect(self.updateModel)
        self.ui.optimiserList.currentTextChanged.connect(self.updateOptim)

        for index, optimiser in enumerate(self.allOptimiser):
            self.ui.optimiserList.addItem(optimiser)
        
    def updateModel(self, value):
        if (value == "CNN"):
            self.message("Changed to CNN model", "black")
            self.arguements = errors.removeValuesFromList(self.arguments, "--vgg")
            self.arguements = errors.removeValuesFromList(self.arguments, "--resnet")
        elif(value == "ResNet50"):
            self.message("Changed to ResNet50 model", "black")
            self.addArgument("--resnet")
            self.addArgument(self.trainImageFolder)
        elif (value == "vgg16"):
            self.addArgument("--vgg")
            self.addArgument(self.trainImageFolder)
            self.message("Changed to VGG16 model", "black")
            
            
    def updateOptim(self, value):
        self.optimiser = value
        
    def bbrowseFiles(self):
        folderName = file.browseFiles()
        self.ui.fileInput.setText(folderName)

        images = file.addAllPngFiles(folderName)

        for item in images:
            self.ui.imageList.addItem(item)
            
    def addArgument(self, args):
        self.arguements = errors.removeValuesFromList(self.arguments, args)
        self.arguments.append(args)
        
    def selectTrainFolder(self):
        self.trainImageFolder = file.browseFiles()
        self.message("Selected Training folder: " + self.trainImageFolder, "blue")
        # ensure we keep a clean list without duplicates
        # could use a set or different datastructure and cast
        self.addArgument("-i")
        self.addArgument(self.trainImageFolder)


    def selectTestFolder(self):
        self.testImageFolder = file.browseFiles()
        self.message("Updating test folder to: " + self.testImageFolder, "blue")
        self.arguements = errors.removeValuesFromList(self.arguments, "-c")
        self.arguments.append("-c")
        self.arguements = errors.removeValuesFromList(self.arguments, self.testImageFolder)
        self.arguments.append(self.testImageFolder)
        
    def selectValFolder(self):
        self.valImageFolder = file.browseFiles()
        self.message("Updating Validation folder to: " + self.valImageFolder, "blue")
        self.arguements = errors.removeValuesFromList(self.arguments, "--inputValidate")
        self.arguments.append("--inputValidate")
        self.arguements = errors.removeValuesFromList(self.arguments, self.valImageFolder)
        self.arguments.append(self.valImageFolder)
 
    def message(self, s, colour):
        
        if (colour == "red"):
            self.ui.trainOutput.setTextColor("red");
        elif (colour == "green"):
            self.ui.trainOutput.setTextColor("green");
        elif (colour == "blue"):
            self.ui.trainOutput.setTextColor("blue");
        else:
            self.ui.trainOutput.setTextColor("black");
            
        self.ui.trainOutput.append(s)

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
        
    def trainModel(self):
        self.message("running model with the following options: ", "black")
        self.message(' '.join(self.arguments), "red")
        self.startProcess()
        

