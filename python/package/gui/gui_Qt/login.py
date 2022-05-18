# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QMessageBox
from python.package.mysql.sql import SqlAction


class Login_window(object):
    def setupUi(self, Dialog):
        self.sql = SqlAction()
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 317)
        self.user_input = QtWidgets.QLineEdit(Dialog)
        self.user_input.setGeometry(QtCore.QRect(130, 160, 121, 21))
        self.user_input.setObjectName("user_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 160, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 31, 21))
        self.label_2.setObjectName("label_2")
        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(130, 200, 121, 21))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(54, 50, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(96, 250, 75, 23))
        self.login.setObjectName("login")
        self.new_user = QtWidgets.QPushButton(Dialog)
        self.new_user.setGeometry(QtCore.QRect(260, 159, 75, 23))
        self.new_user.setObjectName("new_user")
        self.forget = QtWidgets.QPushButton(Dialog)
        self.forget.setGeometry(QtCore.QRect(260, 200, 75, 23))
        self.forget.setObjectName("forget")
        self.reset_all = QtWidgets.QPushButton(Dialog)
        self.reset_all.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.reset_all.setObjectName("reset_all")

        self.retranslateUi(Dialog)
        self.reset_all.clicked.connect(self.password_input.clear)
        self.reset_all.clicked.connect(self.user_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "欢迎使用RPA自动化系统"))
        self.login.setText(_translate("Dialog", "登录"))
        self.new_user.setText(_translate("Dialog", "注册"))
        self.forget.setText(_translate("Dialog", "忘记密码"))
        self.reset_all.setText(_translate("Dialog", "重置"))

    # def check_password(self):
    #     user = self.user_input.text()
    #     password = self.password_input.text()
    #     if user == '':
    #         self.showDialog('用户名为空')
    #         self.password_input.clear()
    #         return 0
    #     user_tuple = self.sql.get_data_from_mysql('user_info','user')
    #     if user not in user_tuple:
    #         self.showDialog('用户名不存在')
    #         return 0
    #     else:
    #         password_true = self.sql.get_data_from_mysql('user_info','password',f'user="{user}"')
    #         if password_true == password:
    #             self.showDialog('密码正确')
    #         else:
    #             self.showDialog('密码错误')
    #     self.sql.quit_database()

    def showDialog(self, words):
        QMessageBox.about(self.Dialog,'RPA', words)

