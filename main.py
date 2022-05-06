import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Check_db import *
from LoginF import *
from RegW import *

class InterfaceR(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InterfaceR,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.auth)

class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.base_line_edit =[self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckTheread()
        self.check_db.mysignal.connect(self.signal_handler)

    #def eventFilter(self, obj, e):
        #if e.type() == 2:
            #btn = e.button()
            #if btn == 1:
                #self.label_2.setText('Clicked Left Button')
            #elif btn == 2:
            #    self.label.setText('Clicked Right Button')
        #return super(Ui_MainWindow, self).eventFilter(obj, e)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self,'Оповещение', value)

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    myR = InterfaceR
    myR.show()
    mywin.show()
    sys.exit(app.exec_())