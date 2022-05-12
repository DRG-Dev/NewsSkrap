from PyQt5 import QtCore, QtGui, QtWidgets
from Handler.db_handler import *

class CheckTheread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name,passw,self.mysignal)

    def thr_register(self, name, passw):
        register(name,passw, self.mysignal)