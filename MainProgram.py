from MainWindow import Ui_MainWindow
from MainWindow import constructMainWindow
from TaskExists import Ui_TaskExists
from TaskExists import constructTaskExists
from TaskNotFound import Ui_TaskNotFound
from TaskNotFound import constructTaskNotFound
from AddTask import Ui_AddTask
from AddTask import constructAddTask
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

constructMainWindow()
constructTaskExists()
constructTaskNotFound()
constructAddTask()



