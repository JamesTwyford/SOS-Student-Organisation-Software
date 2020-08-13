import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from datetime import datetime
import csv

TaskList = []
TimeList =[]
HoursLeft = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
NewTimeList = []
TotalHoursLeft = 0

with open("Task List.txt") as fh:
    for line in fh:
        TaskList.append(line.rstrip("\n"))

with open("Time Allocations.csv") as file:
    for i in range(1, 14):
        data = csv.reader(file)
        for row in data:
            TimeList.append(row)

#Code to format the CSV to fit the current date

#The function that writes the new times to the CSV
def CSVWriteFunc(y, x, TimeNeeded):
    #j begins at 0 but for this code to work it needs to be between 1 - 14 instead of 0 - 13
    x += 1
    #The new time allocated is added to that specific part of the list
    NewTimeList[y][x] = float(NewTimeList[y][x]) + TimeNeeded
    with open("Time Allocations.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(NewTimeList)

def OkBtn():
    print("e")

def AddTaskBtn():
    flt_Temp = 0
    NewTimeList = TimeList
    for i in range(1, len(TimeList)):
        int_TimeNeeded = int(TaskList[i*3])
        for j in range(1, 15):
            flt_Temp = float(TimeList[i][j])
            HoursLeft.insert(j-1, HoursLeft[j-1] - flt_Temp)
            #flt_Temp = 0
        for k in range(0, 14):
            TotalHoursLeft += HoursLeft[k]
        if TotalHoursLeft < int_TimeNeeded:
            print("Task could not be added: Not enough time available for given constraints")
        else:
            for m in range(0, 14):
                if int_TimeNeeded == 0:
                    pass
                else:
                    #If the current date already has 2 hours of tasks, don't use 
                    if HoursLeft[j] == 0:
                        pass
                    elif int_TimeNeeded >= 7 and HoursLeft[j] >= 0.5:
                        if HoursLeft[j] == 2:
                            int_TimeNeeded -= 2
                            CSVWriteFunc(i, j, 2)
                        else:
                            if HoursLeft[j] >= 1:
                                int_TimeNeeded -= 1
                                CSVWriteFunc(i, j, 1)
                            else:
                                int_TimeNeeded -= 0.5
                                CSVWriteFunc(i, j, 0.5)
                    elif j < 3 and HoursLeft[j] >= 0.5:
                        if int_TimeNeeded == 0.5:
                            int_TimeNeeded -= 0.5
                            CSVWriteFunc(i, j, 0.5)
                        else:
                            if int_TimeNeeded >= 2:
                                if HoursLeft[j] == 2:
                                    int_TimeNeeded -= 2
                                    CSVWriteFunc(i, j, 2)
                                else:
                                    if HoursLeft[j] >= 1:
                                        int_TimeNeeded -= 1
                                        CSVWriteFunc(i, j, 1)
                                    else:
                                        int_TimeNeeded -= 0.5
                                        CSVWriteFunc(i, j, 0.5)
                            else:
                                if int_TimeNeeded >= 1:
                                    if HoursLeft[j] >= 1:
                                        int_TimeNeeded -= 1
                                        CSVWriteFunc(i, j, 1)
                                    else:
                                        int_TimeNeeded -= 0.5
                                        CSVWriteFunc(i, j, 0.5)
                                #we dont need an else statement here as we already checked above if int_TimeNeeded == 0.5
                    elif HoursLeft[j] == 2:
                        if int_TimeNeeded >= 2:
                            int_TimeNeeded -= 1
                            CSVWriteFunc(i, j, 1)
                        else:
                            if int_TimeNeeded >= 1:
                                int_TimeNeeded -= 1
                                CSVWriteFunc(i, j, 1)
                            else:
                                int_TimeNeeded -= 0.5
                                CSVWriteFunc(i, j, 0.5) 
                    elif HoursLeft[j] >= 1:
                        if int_TimeNeeded >= 1:
                            int_TimeNeeded -= 0.5
                            CSVWriteFunc(i, j, 0.5)
                        else:
                            int_TimeNeeded -= 0.5
                            CSVWriteFunc(i, j, 0.5)
                    elif HoursLeft[j] == 0.5:
                        int_TimeNeeded -= 0.5
                        CSVWriteFunc(i, j, 0.5)
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1084, 625))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleBack = QtWidgets.QFrame(self.centralwidget)
        self.TitleBack.setGeometry(QtCore.QRect(0, -10, 1091, 91))
        self.TitleBack.setStyleSheet("background-color: rgb(91, 155, 213);")
        self.TitleBack.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack.setObjectName("TitleBack")
        self.TitleBack2 = QtWidgets.QFrame(self.TitleBack)
        self.TitleBack2.setGeometry(QtCore.QRect(40, 20, 1002, 62))
        self.TitleBack2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.TitleBack2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack2.setObjectName("TitleBack2")
        self.Title = QtWidgets.QLabel(self.TitleBack2)
        self.Title.setGeometry(QtCore.QRect(430, 10, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.SearchBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.SearchBox.setGeometry(QtCore.QRect(290, 80, 500, 62))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SearchBox.setFont(font)
        self.SearchBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SearchBox.setPlainText("")
        self.SearchBox.setObjectName("SearchBox")
        self.OKBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OKBtn.setGeometry(QtCore.QRect(490, 190, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.OKBtn.setFont(font)
        self.OKBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.OKBtn.setObjectName("OKBtn")
        #BUTTON CLICK CONNECTION 
        self.OKBtn.clicked.connect(OkBtn)
        self.ViewTasksBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ViewTasksBtn.setGeometry(QtCore.QRect(890, 510, 182, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.ViewTasksBtn.setFont(font)
        self.ViewTasksBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.ViewTasksBtn.setObjectName("ViewTasksBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Search Task"))
        self.OKBtn.setText(_translate("MainWindow", "OK"))
        self.ViewTasksBtn.setText(_translate("MainWindow", "View Tasks"))

def constructMainWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

class Ui_TaskExists(object):
    def setupUi(self, TaskExists):
        TaskExists.setObjectName("TaskExists")
        TaskExists.resize(1084, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskExists.sizePolicy().hasHeightForWidth())
        TaskExists.setSizePolicy(sizePolicy)
        TaskExists.setMaximumSize(QtCore.QSize(1084, 625))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        TaskExists.setFont(font)
        TaskExists.setAutoFillBackground(False)
        TaskExists.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(TaskExists)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleBack = QtWidgets.QFrame(self.centralwidget)
        self.TitleBack.setGeometry(QtCore.QRect(0, -10, 1091, 91))
        self.TitleBack.setStyleSheet("background-color: rgb(91, 155, 213);")
        self.TitleBack.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack.setObjectName("TitleBack")
        self.TitleBack2 = QtWidgets.QFrame(self.TitleBack)
        self.TitleBack2.setGeometry(QtCore.QRect(40, 20, 1002, 62))
        self.TitleBack2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.TitleBack2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack2.setObjectName("TitleBack2")
        self.Title = QtWidgets.QLabel(self.TitleBack2)
        self.Title.setGeometry(QtCore.QRect(380, 10, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.DeleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBtn.setGeometry(QtCore.QRect(190, 160, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DeleteBtn.setFont(font)
        self.DeleteBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.ViewCurrentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ViewCurrentBtn.setGeometry(QtCore.QRect(730, 160, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.ViewCurrentBtn.setFont(font)
        self.ViewCurrentBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.ViewCurrentBtn.setObjectName("ViewCurrentBtn")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(920, 490, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.CancelBtn.setObjectName("CancelBtn")
        TaskExists.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskExists)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 18))
        self.menubar.setObjectName("menubar")
        TaskExists.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TaskExists)
        self.statusbar.setObjectName("statusbar")
        TaskExists.setStatusBar(self.statusbar)

        self.retranslateUi(TaskExists)
        QtCore.QMetaObject.connectSlotsByName(TaskExists)
    def retranslateUi(self, TaskExists):
        _translate = QtCore.QCoreApplication.translate
        TaskExists.setWindowTitle(_translate("TaskExists", "MainWindow"))
        self.Title.setText(_translate("TaskExists", "This task already exists!"))
        self.DeleteBtn.setText(_translate("TaskExists", "Delete Task"))
        self.ViewCurrentBtn.setText(_translate("TaskExists", "View Info"))
        self.CancelBtn.setText(_translate("TaskExists", "Cancel"))

def constructTaskExists():
    app = QtWidgets.QApplication(sys.argv)
    TaskExists = QtWidgets.QMainWindow()
    ui = Ui_TaskExists()
    ui.setupUi(TaskExists)
    TaskExists.show()
    app.exec_()

class Ui_TaskNotFound(object):
    def setupUi(self, TaskNotFound):
        TaskNotFound.setObjectName("TaskNotFound")
        TaskNotFound.resize(1084, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskNotFound.sizePolicy().hasHeightForWidth())
        TaskNotFound.setSizePolicy(sizePolicy)
        TaskNotFound.setMaximumSize(QtCore.QSize(1084, 625))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        TaskNotFound.setFont(font)
        TaskNotFound.setAutoFillBackground(False)
        TaskNotFound.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(TaskNotFound)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleBack = QtWidgets.QFrame(self.centralwidget)
        self.TitleBack.setGeometry(QtCore.QRect(0, -10, 1091, 91))
        self.TitleBack.setStyleSheet("background-color: rgb(91, 155, 213);")
        self.TitleBack.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack.setObjectName("TitleBack")
        self.TitleBack2 = QtWidgets.QFrame(self.TitleBack)
        self.TitleBack2.setGeometry(QtCore.QRect(40, 20, 1002, 62))
        self.TitleBack2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.TitleBack2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack2.setObjectName("TitleBack2")
        self.Title = QtWidgets.QLabel(self.TitleBack2)
        self.Title.setGeometry(QtCore.QRect(410, 10, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.AddWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddWinBtn.setGeometry(QtCore.QRect(460, 160, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.AddWinBtn.setFont(font)
        self.AddWinBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.AddWinBtn.setObjectName("AddWinBtn")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(920, 490, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.CancelBtn.setObjectName("CancelBtn")
        TaskNotFound.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskNotFound)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 18))
        self.menubar.setObjectName("menubar")
        TaskNotFound.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TaskNotFound)
        self.statusbar.setObjectName("statusbar")
        TaskNotFound.setStatusBar(self.statusbar)

        self.retranslateUi(TaskNotFound)
        QtCore.QMetaObject.connectSlotsByName(TaskNotFound)

    def retranslateUi(self, TaskNotFound):
        _translate = QtCore.QCoreApplication.translate
        TaskNotFound.setWindowTitle(_translate("TaskNotFound", "MainWindow"))
        self.Title.setText(_translate("TaskNotFound", "Task not found!"))
        self.AddWinBtn.setText(_translate("TaskNotFound", "Add a Task"))
        self.CancelBtn.setText(_translate("TaskNotFound", "Cancel"))


def constructTaskNotFound():
    app = QtWidgets.QApplication(sys.argv)
    TaskNotFound = QtWidgets.QMainWindow()
    ui = Ui_TaskNotFound()
    ui.setupUi(TaskNotFound)
    TaskNotFound.show()
    app.exec_()

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(1084, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddTask.sizePolicy().hasHeightForWidth())
        AddTask.setSizePolicy(sizePolicy)
        AddTask.setMaximumSize(QtCore.QSize(1084, 625))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        AddTask.setFont(font)
        AddTask.setAutoFillBackground(False)
        AddTask.setStyleSheet("background-color: rgb(189, 215, 238);\n"
"border-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(AddTask)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleBack = QtWidgets.QFrame(self.centralwidget)
        self.TitleBack.setGeometry(QtCore.QRect(0, -10, 1091, 91))
        self.TitleBack.setStyleSheet("background-color: rgb(91, 155, 213);")
        self.TitleBack.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack.setObjectName("TitleBack")
        self.TitleBack2 = QtWidgets.QFrame(self.TitleBack)
        self.TitleBack2.setGeometry(QtCore.QRect(40, 20, 1002, 62))
        self.TitleBack2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.TitleBack2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBack2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBack2.setObjectName("TitleBack2")
        self.Title = QtWidgets.QLabel(self.TitleBack2)
        self.Title.setGeometry(QtCore.QRect(440, 10, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.AddTaskBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddTaskBtn.setGeometry(QtCore.QRect(740, 490, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.AddTaskBtn.setFont(font)
        self.AddTaskBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.AddTaskBtn.setObjectName("AddTaskBtn")
        #PRETTY MUCH THE MOST INMPORTANT LINE OF CODE
        self.AddTaskBtn.clicked.connect(AddTaskBtn)
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(920, 490, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.CancelBtn.setObjectName("CancelBtn")
        self.TaskName = QtWidgets.QLabel(self.centralwidget)
        self.TaskName.setGeometry(QtCore.QRect(30, 130, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.TaskName.setFont(font)
        self.TaskName.setObjectName("TaskName")
        self.NameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.NameBox.setGeometry(QtCore.QRect(170, 145, 611, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.NameBox.setFont(font)
        self.NameBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameBox.setObjectName("NameBox")
        self.DueDate = QtWidgets.QLabel(self.centralwidget)
        self.DueDate.setGeometry(QtCore.QRect(30, 230, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DueDate.setFont(font)
        self.DueDate.setObjectName("DueDate")
        self.DateDayBox = QtWidgets.QLineEdit(self.centralwidget)
        self.DateDayBox.setGeometry(QtCore.QRect(170, 245, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DateDayBox.setFont(font)
        self.DateDayBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DateDayBox.setObjectName("DateDayBox")
        self.EstTime = QtWidgets.QLabel(self.centralwidget)
        self.EstTime.setGeometry(QtCore.QRect(30, 330, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.EstTime.setFont(font)
        self.EstTime.setObjectName("EstTime")
        self.TimeBox = QtWidgets.QLineEdit(self.centralwidget)
        self.TimeBox.setGeometry(QtCore.QRect(320, 345, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.TimeBox.setFont(font)
        self.TimeBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TimeBox.setObjectName("TimeBox")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(430, 330, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(280, 230, 31, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.DateMonthBox = QtWidgets.QLineEdit(self.centralwidget)
        self.DateMonthBox.setGeometry(QtCore.QRect(300, 245, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DateMonthBox.setFont(font)
        self.DateMonthBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DateMonthBox.setObjectName("DateMonthBox")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(410, 230, 31, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.DateMonthBox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.DateMonthBox_2.setGeometry(QtCore.QRect(430, 245, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.DateMonthBox_2.setFont(font)
        self.DateMonthBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DateMonthBox_2.setObjectName("DateMonthBox_2")
        AddTask.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddTask)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 18))
        self.menubar.setObjectName("menubar")
        AddTask.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddTask)
        self.statusbar.setObjectName("statusbar")
        AddTask.setStatusBar(self.statusbar)

        self.retranslateUi(AddTask)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "MainWindow"))
        self.Title.setText(_translate("AddTask", "Add Task"))
        self.AddTaskBtn.setText(_translate("AddTask", "Add Task"))
        self.CancelBtn.setText(_translate("AddTask", "Cancel"))
        self.TaskName.setText(_translate("AddTask", "Task Name:"))
        self.DueDate.setText(_translate("AddTask", "Due Date:"))
        self.EstTime.setText(_translate("AddTask", "Estimated Time Needed:"))
        self.label1.setText(_translate("AddTask", "Hours"))
        self.label2.setText(_translate("AddTask", "/"))
        self.label3.setText(_translate("AddTask", "/"))


def constructAddTask():
    app = QtWidgets.QApplication(sys.argv)
    AddTask = QtWidgets.QMainWindow()
    ui = Ui_AddTask()
    ui.setupUi(AddTask)
    AddTask.show()
    app.exec_()

constructMainWindow()


