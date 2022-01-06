from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from BANBEN import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("123.jpg")

class banben01(QMainWindow,Ui_Form):
    def __init__(self):
        super(banben01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.label.setText("1.01")
        #self.pushButton.clicked.connect(self.Button_1)

