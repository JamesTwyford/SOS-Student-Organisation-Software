from MainWindow import Ui_MainWindow
from TaskExists import Ui_TaskExists
from TaskExists import constructTaskExists
from TaskNotFound import Ui_TaskNotFound
from TaskNotFound import constructTaskNotFound
from AddTask import Ui_AddTask
from AddTask import constructAddTask
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#constructMainWindow()   
#print("dighsdig")
#constructTaskExists()
#constructTaskNotFound()
#constructAddTask()

def subMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    winMainWindow = QtWidgets.QMainWindow()
    uiMainWindow = MainWindow.Ui_MainWindow()
    uiMainWindow.setupUi(winMainWindow)
    winMainWindow.show()

subMainWindow()
