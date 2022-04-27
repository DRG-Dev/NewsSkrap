import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Check_db import *
from LoginF import *


class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin =Interface()
    mywin.show()
    sys.exit(app.exec_())