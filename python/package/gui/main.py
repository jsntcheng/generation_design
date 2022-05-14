import sys
from PyQt5.QtWidgets import  *
from gui_Qt.login import Login_window
from gui_Qt.new_user import NewUser
from gui_Qt.index import IndexPage
from gui_Qt.design_studio import Design
from gui_Qt.forget import Forget
from gui_Qt.browser import Browser
from gui_Qt.create_project import CreateProject
from package.mysql.sql import SqlAction


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
                self.close()
                index.show()
            else:
                self.showDialog('密码错误')
        self.sql.quit_database()

class CreateProjectWin(QDialog,CreateProject):
    def __init__(self):
        super(CreateProjectWin, self).__init__(None)
        self.setupUi(self)
        self.user = ''
        self.pushButton.clicked.connect(self.click_ok)
    def click_ok(self):
        sql = SqlAction()
        session_list = sql.get_data_from_mysql('session_list','distinct project',f'user="{self.user}"')
        session_insert = self.lineEdit.text()
        if session_insert == '':
            self.showDialog('请输入项目名')
            return 0
        if session_insert in session_list:
            self.showDialog('项目名已存在')
            return 0
        sql.insert_data_into_mysql('session_list',(self.user,session_insert,'',''))
        sql.quit_database()
        design.project_name = session_insert
        design.change_title(session_insert)
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
    login.forget.clicked.connect(forget.show)
    login.new_user.clicked.connect(newuser.show)
    login.login.clicked.connect(login.check_password)
    index.pushButton.clicked.connect(create_project.show)
    login.show()
    sys.exit(myapp.exec_())


