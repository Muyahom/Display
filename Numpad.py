# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keypad1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# Ui 클래스
class Host(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 561)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(140, 140, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(230, 140, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(320, 140, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(320, 230, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(140, 230, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(230, 230, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(320, 320, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(140, 320, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(230, 320, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(320, 400, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(140, 400, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.confirm.setFont(font)
        self.confirm.setObjectName("confirm")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(230, 400, 71, 71))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(200, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(36)
        self.textlabel.setFont(font)
        self.textlabel.setObjectName("textlabel")
        self.MainWindow_2 = QtWidgets.QLabel(self.centralwidget)
        self.MainWindow_2.setGeometry(QtCore.QRect(140, 90, 251, 41))
        self.MainWindow_2.setAutoFillBackground(True)
        self.MainWindow_2.setFrameShape(QtWidgets.QFrame.Box)
        self.MainWindow_2.setText("")
        self.MainWindow_2.setObjectName("MainWindow_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    

       # 버튼 정의
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.cancel.setText(_translate("MainWindow", "취소"))
        self.confirm.setText(_translate("MainWindow", "확인"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.textlabel.setText(_translate("MainWindow", "Check_IN"))

         # 버튼 액션 추가
        self.btn1.clicked.connect(self.action1)
        self.btn2.clicked.connect(self.action2)
        self.btn3.clicked.connect(self.action3)
        self.btn4.clicked.connect(self.action4)
        self.btn5.clicked.connect(self.action5)
        self.btn6.clicked.connect(self.action6)
        self.btn7.clicked.connect(self.action7)
        self.btn8.clicked.connect(self.action8)
        self.btn9.clicked.connect(self.action9)
        self.btn0.clicked.connect(self.action0)
        self.cancel.clicked.connect(self.action_cancel)
        self.confirm.clicked.connect(self.action_confirm)
        

    #각 버튼들에 대한 정의
    def action0(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "0")

    def action1(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "1")

    def action2(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "2")

    def action3(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "3")

    def action4(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "4")

    def action5(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "5")

    def action6(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "6")

    def action7(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "7")

    def action8(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "8")

    def action9(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "9")

    def action_cancel(self):
        # clearing the label text
        self.MainWindow_2.setText("")
    
    def action_confirm(self):
       confirm = self.MainWindow_2.setText()
       
       try:
           ans = eval(confirm)
           
           self.MainWindow_2.setText(str(ans))
       except:
           self.MainWindow_2.setText("잘못된 입력입니다.")
           
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Host()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

