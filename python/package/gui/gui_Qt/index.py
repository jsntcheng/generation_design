# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class IndexPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 555)
        font = QtGui.QFont()
        font.setFamily("等线")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 400, 151, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 400, 151, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(300, 330, 151, 51))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(12)
        # self.pushButton_2.setFont(font)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(300, 180, 151, 51))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(12)
        # self.pushButton_4.setFont(font)
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_5.setGeometry(QtCore.QRect(300, 256, 151, 51))
        # font = QtGui.QFont()
        # font.setFamily("等线")
        # font.setPointSize(12)
        # self.pushButton_5.setFont(font)
        # self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "设计新流程"))
        self.pushButton_3.setText(_translate("MainWindow", "打开已有流程列表"))
        self.label.setText(_translate("MainWindow", "欢迎来到RPA自动化系统"))
        # self.pushButton_2.setText(_translate("MainWindow", "修改密码"))
        # self.pushButton_4.setText(_translate("MainWindow", "查看用户"))
        # self.pushButton_5.setText(_translate("MainWindow", "增加用户"))

