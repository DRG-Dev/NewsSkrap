import sys, re, urllib, html2text
from urllib import request
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor,QImage
import requests
from Check_db import *
from LoginP import *
from ParseFormP import *

class InterfaceR(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InterfaceR,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.newsURL=[]
        self.parser()


        self.ui.pushButton.clicked.connect(self.OpenNews)

    def parser(self):
        s = 'https://russian.rt.com/news'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        doc = doc.replace('\n', '')
        zagolovki = re.findall('<a class="link link_color" href="(.+?)</a>', doc)
        for x in zagolovki:
            self.newsURL.append(x.split('">')[0])
            self.ui.listWidget.addItem(x.split('">')[1].strip() + "\n")


    def OpenNews(self):
        n= self.ui.listWidget.currentRow()
        u = 'https://russian.rt.com'+self.newsURL[n]
        doc = urllib.request.urlopen(u).read().decode('utf-8', errors='ignore')
        h = html2text.HTML2Text()
        h.ignore_links= True
        h.body_width= False
        h.ignore_images= True
        doc = h.handle(doc)
        mas = doc.split('\n')
        newstext = ''
        imgsrc = "https://cdni.rt.com/russian/images/2022.05/article/6291c0f5ae5ac933e1109912.jpg"
        image = QImage()
        image.loadFromData(requests.get(imgsrc).content)
        image = image.scaledToWidth(myR.width() - 100)
        document = self.ui.textEdit.document()
        cursor = QTextCursor(document)

        for x in mas:
            if(len(x)>90):
                newstext = newstext+x+'\n\n'
                self.ui.textEdit.setText(newstext)
                cursor.insertImage(image)




class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.reg)
        self.base_line_edit =[self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckTheread()
        self.check_db.mysignal.connect(self.signal_handler)


    #def eventFilter(self, obj, e):
        #if e.type() == 2:
            #btn = e.button()
            #if btn == 1:
                #self.label_2.setText('Clicked Left Button')
            #elif btn == 2:
                #self.label_2.setText('Clicked Right Button')
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
        if value == 'Успешная авторизация':
            myR.show()
            mywin.close()



    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.setWindowTitle('NewsSkrap')
    mywin.setFixedSize(600,700)
    myR = InterfaceR()
    myR.setWindowTitle('NewsSkrap')
    myR.setFixedSize(800,900)
    myR.ui.textEdit.toHtml()
    mywin.show()
    sys.exit(app.exec_())