import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

form_secondwindow = uic.loadUiType("GuestUI.ui")[0]

class Form(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(Form,self).__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.setupUi(self)
        self.btnBack.clicked.connect(self.back_to_main)

    def back_to_main(self):
        self.close()
        
