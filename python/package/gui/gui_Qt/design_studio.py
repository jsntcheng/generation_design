# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_studio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from python.package.gui.gui_Qt.return_event_dialog import ReturnEventDialog
from python.package.gui.gui_Qt.noreturn_event_dialog import NoReturnEventDialog
from python.package.actions.web_actions import *
from python.package.mysql.sql import SqlAction

class Return(QDialog, ReturnEventDialog):
    def __init__(self):
        super(Return, self).__init__(None)
        self.setupUi(self)

class NoReturn(QDialog, NoReturnEventDialog):
    def __init__(self):
        super(NoReturn, self).__init__(None)
        self.setupUi(self)

class Design(object):
    def setupUi(self, MainWindow):
        self.tree_dict = {
            '启动浏览器':'create_browser(',
            '关闭浏览器':'close_browser(',
            '切换操作页面':'switch_page(',
            '刷新页面':'refresh_page(',
            '等待元素出现':'wait_element(',
            '获取所有元素':'get_all_element(',
            '点击元素':'click_element(',
            '获取元素属性':'get_element_attr(',
            '设置输入框':'set_input(',
            '获取元素内文字':'get_element_txt('
        }
        self.no_return_list = ['关闭浏览器','切换操作页面','刷新页面','点击元素','设置输入框']
        self.user = ''
        self.Return = Return()
        self.NoReturn = NoReturn()
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 50, 256, 391))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(290, 50, 621, 501))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 16, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 450, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 500, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "操作"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "浏览器操作"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "启动浏览器"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "关闭浏览器"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "切换操作页面"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "刷新页面"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "等待元素出现"))
        self.treeWidget.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "获取所有元素"))
        self.treeWidget.topLevelItem(0).child(6).setText(0, _translate("MainWindow", "点击元素"))
        self.treeWidget.topLevelItem(0).child(7).setText(0, _translate("MainWindow", "获取元素属性"))
        self.treeWidget.topLevelItem(0).child(8).setText(0, _translate("MainWindow", "设置输入框"))
        self.treeWidget.topLevelItem(0).child(9).setText(0, _translate("MainWindow", "获取元素内文字"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "excel操作"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "打开Excel文件"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "创建Excel文档"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "保存Excel文档"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "新建Sheet页"))
        self.treeWidget.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "删除Sheet页"))
        self.treeWidget.topLevelItem(1).child(5).setText(0, _translate("MainWindow", "合并单元格"))
        self.treeWidget.topLevelItem(1).child(6).setText(0, _translate("MainWindow", "写入内容"))
        self.treeWidget.topLevelItem(1).child(7).setText(0, _translate("MainWindow", "读取内容"))
        self.treeWidget.topLevelItem(1).child(8).setText(0, _translate("MainWindow", "设置背景色"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "word操作"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "新建Word文档"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "打开Word文档"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "保存Word文档"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "读取内容"))
        self.treeWidget.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "写入内容"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "编程相关"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "创建变量"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "打印变量"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "赋值操作"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("MainWindow", "for循环"))
        self.treeWidget.topLevelItem(3).child(4).setText(0, _translate("MainWindow", "while循环"))
        self.treeWidget.topLevelItem(3).child(5).setText(0, _translate("MainWindow", "if判断"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "邮件"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "发送邮件"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "HTTP"))
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "下载"))
        self.treeWidget.topLevelItem(5).child(1).setText(0, _translate("MainWindow", "Get请求"))
        self.treeWidget.topLevelItem(5).child(2).setText(0, _translate("MainWindow", "Post请求"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "控件选择"))
        self.label_2.setText(_translate("MainWindow", "代码编辑"))
        self.pushButton.setText(_translate("MainWindow", "运行"))
        self.pushButton_2.setText(_translate("MainWindow", "保存"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "账户"))
        self.menu_3.setTitle(_translate("MainWindow", "运行"))
        self.actionsave.setText(_translate("MainWindow", "打开"))
        self.action.setText(_translate("MainWindow", "保存"))
        self.action_2.setText(_translate("MainWindow", "修改密码"))
        self.action_3.setText(_translate("MainWindow", "退出登录"))
        self.treeWidget.itemDoubleClicked['QTreeWidgetItem*','int'].connect(self.function)
        self.pushButton.clicked.connect(self.run_it)

    def function(self, item):
        _translate = QtCore.QCoreApplication.translate
        if item.text(0) in self.no_return_list:
            self.NoReturn.tool.setText(_translate('Dialog',item.text(0)))
            self.NoReturn.param.setText(_translate("Dialog", get_doc(self.tree_dict[item.text(0)][:-1])))
            self.NoReturn.show()
        else:
            self.Return.tool.setText(_translate("Dialog", item.text(0)))
            self.Return.param.setText(_translate("Dialog", get_doc(self.tree_dict[item.text(0)][:-1])))
            self.Return.show()



    def run_it(self):
        temp_file = open('temp.py','w',encoding='gbk')
        temp_file.write(self.plainTextEdit.toPlainText())
        path = os.path.dirname(__file__)
        path2 = path
        path.strip('package\gui\gui_Qt')
        os.system(path + 'python' + path2 + '\\temp.py')

    def change_title(self,name):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", name))