import sys
import json
from PyQt5.QtGui import QTextCursor,QImage
from PyQt5.QtWidgets import QDesktopWidget
from Check_db import *
from LoginP import *
from ParseFormPN import *
from RequestsHandler import *

class InterfaceR(QtWidgets.QWidget):

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __init__(self, parent=None):
        super(InterfaceR, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parser('world')
        self.getCategories()

        self.ui.pushButton.clicked.connect(self.OpenNews)
        self.ui.listWidget_Categories.currentRowChanged.connect(self.updateParse)

    def updateParse(self):
        self.ui.listWidget.clear()
        jsonConnect = open("data/categories.json")
        data = json.load(jsonConnect)
        n = self.ui.listWidget_Categories.currentRow()
        curCategory = data[f"{n}"]['category_Link']
        self.parser(curCategory)


    def getCategories(self):
        url = "https://ria.ru"
        soup = GetSoup(self, url)
        i = 0
        categories_card = soup.find_all("a", {"class": "cell-extension__item-link"}, limit=6)
        category_info = {}
        for category in categories_card:
            category_Name = category.find("span", class_="cell-extension__item-title").text.strip()
            category_Link = category.get("href")
            category_info[i] = {
                    'category_Name': category_Name,
                    'category_Link':category_Link
            }
            i += 1
            self.ui.listWidget_Categories.addItem(category_Name)
            with open(f"data/categories.json", "w") as file:
                json.dump(category_info, file, indent=4, ensure_ascii=False)

    def parser(self,category):
        url = "https://ria.ru/" + category

        i = 0
        news_cards = GetSoup(self, url).findAll("div", {"class": "list-item"})
        card_info = {}
        for card in news_cards:
            card_Header = card.find("a", class_="list-item__title").text.strip()
            card_Url = card.find("a", class_="list-item__title").get("href")
            card_Date = card.find("div", class_="list-item__date").text.strip()
            card_info[i] = {
                 "cards": {
                                'card_Header':card_Header,
                                'card_Date': card_Date,
                                'card_Url':card_Url
                 }
            }
            i+=1
            self.ui.listWidget.addItem(card_Header)
            with open("data/news.json", "w") as file:
                json.dump(card_info, file, indent=4, ensure_ascii=False)


    def OpenNews(self):
        n = self.ui.listWidget.currentRow()
        jsonConnect = open("data/news.json")
        data = json.load(jsonConnect)
        sub_Url = data[f"{n}"]['cards']['card_Url']
        soup = GetSoup(self, sub_Url)
        imgSrc = soup.find("div", class_="photoview__open").img.get("src")
        dateInfo = soup.find("div", class_="article__info-date").a.get_text()
        at_Layout = soup.find_all("div", class_="article__text")
        finalLayout = ''
        for at in at_Layout:
            finalLayout +=(f"{at.get_text()}\n")

        image = QImage()
        image.loadFromData(requests.get(imgSrc).content)
        image = image.scaledToWidth(myR.width() - 100)
        document = self.ui.textEdit.document()
        cursor = QTextCursor(document)
        cursor.insertImage(image)
        cursor.insertText("\n\n" + finalLayout)
        cursor.insertText(dateInfo)




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
    mywin.setWindowTitle('NewsScrap')
    mywin.setFixedSize(600, 700)
    myR = InterfaceR()
    myR.setWindowTitle('NewsScrap')
    myR.setFixedSize(1000, 950)
    myR.center()
    mywin.show()
    #myR.show()
    sys.exit(app.exec_())