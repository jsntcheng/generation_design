# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from package.mysql.sql import SqlAction
from package.email.smtp_sender import SMTPSender

class Forget(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 223)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 93, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 133, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(154, 170, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "找回密码"))
        self.label_2.setText(_translate("Dialog", "账户"))
        self.label_3.setText(_translate("Dialog", "密保邮箱"))
        self.pushButton.setText(_translate("Dialog", "找回"))
        self.pushButton.clicked.connect(self.send_email)

    def send_email(self):
        input_user = self.lineEdit.text()
        input_email = self.lineEdit_2.text()
        if input_user == '':
            self.showDialog('请输入用户名')
            return 0
        if input_email == '':
            self.showDialog('请输入密保邮箱')
            return 0
        sql = SqlAction()
        user_list = sql.get_data_from_mysql('user_info','user')
        if input_user not in user_list:
            self.showDialog('不存在此用户名')
            return 0
        sql_email = sql.get_data_from_mysql('user_info','email',f'user = "{input_user}"')
        if sql_email != input_email:
            self.showDialog('密保邮箱输入错误')
            return 0
        print(sql_email)
        password = sql.get_data_from_mysql('user_info','password',f'user="{input_user}"')
        SMTPSender.get_instance().send_mail({
            'subject': '找回密码',
            'recipient': [f'{input_email}'],
            'content': f'用户名:{input_user}||密码:{password}||请牢记'
        })
        self.showDialog('密码已经发送到邮箱，请查收')
        self.Dialog.close()

    def showDialog(self, words):
        QMessageBox.about(self.Dialog,'RPA', words)