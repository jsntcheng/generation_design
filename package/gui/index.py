import sys

from PyQt5.QtWidgets import QApplication, QDialog
from gui_Qt.login import Ui_Dialog as login
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login()
        self.ui.setupUi(self)

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MyDialog()
    myDlg.show()
    sys.exit(myapp.exec_())


