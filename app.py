from main import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = myapp()
    application.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()