from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from YONGHU import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("123.jpg")

class yonghu01(QMainWindow,Ui_Form):
    def __init__(self):
        super(yonghu01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()

        self.pushButton.clicked.connect(self.Button)

    def Button(self):
        self.textEdit.setText("")
        gpid = self.lineEdit.text()
        usid = AI.All_users(gpid)
        for i in usid:
            #print(i)
            user = AI.User_select(i,gpid)[0]
            user_info = user['user_info']
            # print(user)
            # print(user_info)
            self.textEdit.append(user_info)
        #self.lineEdit_2.setText()

