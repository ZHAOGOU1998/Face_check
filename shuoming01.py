from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from SHUOMING import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("123.jpg")

class shuoming01(QMainWindow,Ui_Form):
    def __init__(self):
        super(shuoming01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.textEdit.setText("赵狗")

