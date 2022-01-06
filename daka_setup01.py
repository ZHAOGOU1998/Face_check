from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from DAKA_SETUP import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("123.jpg")

class daka_setup01(QMainWindow,Ui_Form):
    def __init__(self):
        super(daka_setup01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.pushButton.clicked.connect(self.Button)

    def Button(self):
        pel_num = self.lineEdit.text()
        xl_name = self.lineEdit_2.text()
        #pel_num = int(pel_num)
        self.use =  [xl_name,pel_num]
        return self.use
        # print(type(pel_num))
        # print(pel_num)
        # print(xl_name)
        #self.pushButton.clicked.connect(self.Button_1)
    #def Use(self):

