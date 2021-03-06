# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParseFormNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: rgb(42, 93, 120);")

        fontL = QtGui.QFont()
        fontL.setFamily("Arial")
        fontL.setPointSize(12)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.label_listWidget = QtWidgets.QLabel(Form)
        self.label_listWidget.setGeometry(QtCore.QRect(255, 4, 300, 20))
        self.label_listWidget.setFont(fontL)
        self.label_listWidget.setStyleSheet("color: rgba(255, 250, 250, 150);")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setGeometry(QtCore.QRect(250, 25, 746, 335))
        self.listWidget.setFont(font)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSpacing(3)
        self.listWidget.setStyleSheet("color: rgba(255, 250, 250, 185);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"padding: 0 0 2px 5px;\n")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QtCore.QRect(2, 365, 996, 530))
        self.textEdit.toPlainText().encode("utf-8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("color: rgba(255, 250, 250, 185);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"padding: 0 0 0 10px;\n"
"text-align : left;\n"
"text-indent : 100px\n")

#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.setGeometry(QtCore.QRect(2, 890, 996, 50))
#         font = QtGui.QFont()
#         font.setPointSize(13)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setStyleSheet("background-color: rgb(128, 172, 196);\n"
# "color: rgb(42, 93, 120);\n"
# "border-radius: 20px;")

        self.label_Categories = QtWidgets.QLabel(Form)
        self.label_Categories.setGeometry(QtCore.QRect(7, 4, 150, 20))
        self.label_Categories.setFont(fontL)
        self.label_Categories.setStyleSheet("color: rgba(255, 250, 250, 150);")

        self.listWidget_Categories = QtWidgets.QListWidget(Form)
        self.listWidget_Categories.setObjectName("listWidget_Categories")
        self.listWidget_Categories.setGeometry(QtCore.QRect(2, 25, 240, 335))
        self.listWidget_Categories.setWordWrap(True)
        fontCateg = QtGui.QFont()
        fontCateg.setFamily("Arial")
        fontCateg.setPointSize(15)
        self.listWidget_Categories.setFont(fontCateg)
        self.listWidget_Categories.setStyleSheet("color: rgba(255, 250, 250, 185);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"padding: 0 0 0 6px;")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_listWidget.setText(_translate("Headers:", "??????????????????:"))
        self.label_Categories.setText(_translate("Categories:", "??????????????????:"))
