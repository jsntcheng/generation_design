# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMessageBox

from package.mysql.sql import SqlAction
from PyQt5 import QtCore, QtGui, QtWidgets

class NewUser(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(150, 100, 121, 21))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 31, 21))
        self.label_2.setObjectName("label_2")
        self.user_input = QtWidgets.QLineEdit(Dialog)
        self.user_input.setGeometry(QtCore.QRect(150, 60, 121, 21))
        self.user_input.setObjectName("user_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 60, 31, 21))
        self.label.setObjectName("label")
        self.password_input_2 = QtWidgets.QLineEdit(Dialog)
        self.password_input_2.setGeometry(QtCore.QRect(150, 140, 121, 21))
        self.password_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input_2.setObjectName("password_input_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(86, 140, 51, 21))
        self.label_3.setObjectName("label_3")
        self.password_input_3 = QtWidgets.QLineEdit(Dialog)
        self.password_input_3.setGeometry(QtCore.QRect(150, 180, 171, 21))
        self.password_input_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_input_3.setObjectName("password_input_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(86, 180, 51, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label.setText(_translate("Form", "账号"))
        self.label_3.setText(_translate("Form", "确认密码"))
        self.label_4.setText(_translate("Form", "密保邮箱"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.pushButton.clicked.connect(self.insert_user)

    def insert_user (self):
        sql_act = SqlAction()
        user_list = sql_act.get_data_from_mysql('user_info','user')
        user = self.user_input.text()
        if user == '':
            self.showDialog('请输入用户名')
            return 0
        passwd1 = self.password_input.text()
        passwd2 = self.password_input_2.text()
        if user in user_list:
            self.showDialog('用户名已存在')
            self.user_input.clear()
            return 0
        if passwd1 == '':
            self.showDialog('请输入密码')
            return 0
        if passwd2 == '':
            self.showDialog('请再次输入密码')
            return 0
        if passwd1 != passwd2:
            self.showDialog('两次密码不一致')
            self.password_input.clear()
            self.password_input_2.clear()
            return 0
        info = (self.user_input.text(),self.password_input.text(),'user',self.password_input_3.text())
        sql_act.insert_data_into_mysql('user_info',info)
        sql_act.quit_database()
        self.showDialog('注册成功')

    def showDialog(self, words):
        QMessageBox.about(self.Dialog,'RPA', words)