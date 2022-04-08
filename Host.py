import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

form_thirdwindow = uic.loadUiType("Host.ui")[0]

class Form1(QDialog,QWidget,form_thirdwindow):
    def __init__(self):
        super(Form1,self).__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.setupUi(self)
        self.btnBack1.clicked.connect(self.back_to_main)

    def back_to_main(self):
        self.close()
        
