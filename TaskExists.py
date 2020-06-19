# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskExists.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.ViewTasksBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ViewTasksBtn.setGeometry(QtCore.QRect(890, 510, 182, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.ViewTasksBtn.setFont(font)
        self.ViewTasksBtn.setStyleSheet("background-color: rgb(91, 155, 213);\n"
"color: rgb(255, 255, 255);")
        self.ViewTasksBtn.setObjectName("ViewTasksBtn")
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
        self.Title.setText(_translate("TaskExists", "Search Task"))
        self.OKBtn.setText(_translate("TaskExists", "OK"))
        self.ViewTasksBtn.setText(_translate("TaskExists", "View Tasks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskExists = QtWidgets.QMainWindow()
    ui = Ui_TaskExists()
    ui.setupUi(TaskExists)
    TaskExists.show()
    sys.exit(app.exec_())
