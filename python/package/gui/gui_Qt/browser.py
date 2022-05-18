# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Browser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1142, 701)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 1141, 701))
        self.webEngineView.setUrl(QtCore.QUrl("http://101.35.49.209:7900/"))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

from PyQt5 import QtWebEngineWidgets
