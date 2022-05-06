import sys
from PyQt5.QtWidgets import  *
from gui_Qt.login import Login_window
from gui_Qt.new_user import NewUser
from gui_Qt.index import IndexPage
from gui_Qt.design_studio import Design

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
                index.show()
            else:
                self.showDialog('密码错误')
        self.sql.quit_database()

class NewUserWin(QDialog, NewUser):
    def __init__(self):
        super(QDialog, self).__init__(None)
        self.setupUi(self)

class IndexWin(QMainWindow, IndexPage):
    def __init__(self):
        super(QMainWindow, self).__init__(None)
        self.setupUi(self)
class DesignWin(QMainWindow, Design):
    def __init__(self):
        super(DesignWin, self).__init__(None)
        self.setupUi(self)

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    index = IndexWin()
    login = LoginWin(index)
    newuser = NewUserWin()
    design = DesignWin()

    login.new_user.clicked.connect(newuser.show)
    login.login.clicked.connect(login.check_password)

    index.pushButton.clicked.connect(design.show)
    login.show()
    sys.exit(myapp.exec_())


