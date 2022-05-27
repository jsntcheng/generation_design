import sys

from PyQt5.QtWidgets import *

from package.gui.gui_Qt.browser import Browser
from package.gui.gui_Qt.create_project import CreateProject
from package.gui.gui_Qt.design_studio import Design
from package.gui.gui_Qt.forget import Forget
from package.gui.gui_Qt.index import IndexPage
from package.gui.gui_Qt.login import Login_window
from package.gui.gui_Qt.new_user import NewUser
from python.package.mysql.sql import SqlAction


class LoginWin(QDialog, Login_window):
    def __init__(self, index):
        super(QDialog, self).__init__(None)
        self.setupUi(self)

    def check_password(self):
        user = self.user_input.text()
        password = self.password_input.text()
        if user == '':
            self.showDialog('用户名为空')
            self.password_input.clear()
            return 0
        user_tuple = self.sql.get_data_from_mysql('user_info', 'user')
        if user not in user_tuple:
            self.showDialog('用户名不存在')
            return 0
        else:
            password_true = self.sql.get_data_from_mysql('user_info', 'password', f'user="{user}"')
            if password_true == password:
                self.showDialog('密码正确')
                self.user = user
                index.user = user
                design.user = user
                create_project.user = user
                open_project.user = user
                self.close()
                index.show()
            else:
                self.showDialog('密码错误')
        self.sql.quit_database()

class CreateProjectWin(QDialog, CreateProject):
    def __init__(self):
        super(CreateProjectWin, self).__init__(None)
        self.setupUi(self)
        self.user = ''
        self.pushButton.clicked.connect(self.click_ok)

    def click_ok(self):
        sql = SqlAction()
        session_list = sql.get_data_from_mysql('session_list', 'distinct project', f'user="{self.user}"')
        session_insert = self.lineEdit.text()
        if session_insert == '':
            self.showDialog('请输入项目名')
            return 0
        if session_insert in session_list:
            self.showDialog('项目名已存在')
            return 0
        sql.insert_data_into_mysql('session_list', (self.user, session_insert, '', '', ''))
        sql.quit_database()
        design.project_name = session_insert
        design.change_title(session_insert)
        design.plainTextEdit.setPlainText('from actions.web_actions import *\nfrom actions.excel_actions import *')
        self.close()
        design.show()

class OpenProjectWin(QDialog, CreateProject):
    def __init__(self):
        super(OpenProjectWin, self).__init__(None)
        self.setupUi(self)
        self.user = ''
        self.pushButton.clicked.connect(self.click_ok)

    def click_ok(self):
        sql = SqlAction()
        session_list = sql.get_data_from_mysql('session_list', 'distinct project', f'user="{self.user}"')
        session_insert = self.lineEdit.text()
        if session_insert == '':
            self.showDialog('请输入项目名')
            return 0
        if session_insert not in session_list:
            self.showDialog('项目名不存在')
            return 0
        design.project_name = session_insert
        design.change_title(session_insert)
        design.plainTextEdit.setPlainText('from actions.web_actions import *\nfrom actions.excel_actions import *')
        infos = sql.get_data_from_mysql('session_list','mem,use_info,param',f"user = '{self.user}' and project = '{session_insert}'")
        for i in infos[1:]:
            if i[0]!='':
                design.input_code_return(i[0],i[1],i[2])
            else:
                design.input_code_noreturn(i[1],i[2])
        self.close()
        design.show()

class NewUserWin(QDialog, NewUser):
    def __init__(self):
        super(QDialog, self).__init__(None)
        self.setupUi(self)

class IndexWin(QMainWindow, IndexPage):
    def __init__(self):
        super(QMainWindow, self).__init__(None)
        self.setupUi(self)
        self.user = ''

class DesignWin(QMainWindow, Design):
    def __init__(self):
        super(DesignWin, self).__init__(None)
        self.setupUi(self)
        self.user = ''
        self.project_name = ''
        self.NoReturn.pushButton.clicked.connect(self.get_noreturn_param)
        self.Return.pushButton.clicked.connect(self.get_return_param)
        self.plainTextEdit.setPlainText('from actions.web_actions import *\nfrom actions.excel_actions import *')
        self.tab_num = 0

    def get_return_param(self):
        param = self.Return.lineEdit.text()
        mem = self.Return.lineEdit_2.text()
        tool = self.Return.tool.text()
        self.Return.close()
        sql = SqlAction()
        # print(self.user,self.project_name,self.mem,self.tool)
        sql.insert_data_into_mysql('session_list', (self.user, self.project_name, mem, tool, param))
        sql.quit_database()
        self.Return.lineEdit.clear()
        self.Return.lineEdit_2.clear()
        self.input_code_return(mem, tool, param)

    def input_code_return(self, mem, tool, param):
        code = '    ' * self.tab_num + '#' + tool + '\n' + '    ' * self.tab_num + mem + '=' + self.tree_dict[
            tool] + param + ')\n'
        self.plainTextEdit.appendPlainText(code)

    def get_noreturn_param(self):
        param = self.NoReturn.lineEdit.text()
        tool = self.NoReturn.tool.text()
        self.NoReturn.close()
        sql = SqlAction()
        # print(self.user,self.project_name,self.mem,self.tool)
        sql.insert_data_into_mysql('session_list', (self.user, self.project_name, '', tool, param))
        sql.quit_database()
        self.NoReturn.lineEdit.clear()
        self.input_code_noreturn(tool, param)

    def input_code_noreturn(self, tool, param):
        code = '    ' * self.tab_num + '#' + tool + '\n' + '    ' * self.tab_num + self.tree_dict[tool] + param + ')\n'
        self.plainTextEdit.appendPlainText(code)


class ForgetWin(QDialog, Forget):
    def __init__(self):
        super(ForgetWin, self).__init__(None)
        self.setupUi(self)


class BrowserWin(QDialog, Browser):
    def __init__(self):
        super(BrowserWin, self).__init__(None)
        self.setupUi(self)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    index = IndexWin()
    login = LoginWin(index)
    newuser = NewUserWin()
    design = DesignWin()
    forget = ForgetWin()
    browser = BrowserWin()
    create_project = CreateProjectWin()
    open_project = OpenProjectWin()
    login.forget.clicked.connect(forget.show)
    login.new_user.clicked.connect(newuser.show)
    login.login.clicked.connect(login.check_password)
    index.pushButton.clicked.connect(create_project.show)
    index.pushButton_3.clicked.connect(open_project.show)
    login.show()
    sys.exit(myapp.exec_())
