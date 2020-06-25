# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasknotfound.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskNotFound = QtWidgets.QMainWindow()
    ui = Ui_TaskNotFound()
    ui.setupUi(TaskNotFound)
    TaskNotFound.show()
    app.exec_()
