from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from SHANCHU import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("opencv123.jpg")

class shanchu01(QMainWindow,Ui_Form):
    def __init__(self):
        super(shanchu01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.pushButton.clicked.connect(self.Button_1)

    def Button_1(self):
        gpid = self.lineEdit.text()
        usid = self.lineEdit_2.text()
        # print(type(usid))
        # print(usid)
        #info = self.lineEdit_3.text()
        #print(gpid)
        f_token = AI.GetToken()
        shanchu_info = AI.Face_del(usid,gpid,f_token)
        if shanchu_info =='SUCCESS':
            QMessageBox.information(self, "！！！", "删除成功", QMessageBox.Yes)  # , QMessageBox.No
        else:
            QMessageBox.information(self, "！！！", "删除失败", QMessageBox.Yes)  # , QMessageBox.No
        #print(shanchu_info)

