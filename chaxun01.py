from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from CHAXUN import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

Facebase64 = AI.Picture_base("opencv123.jpg")

class chaxun01(QMainWindow,Ui_Form):
    def __init__(self):
        super(chaxun01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.pushButton.clicked.connect(self.Button_1)


    def Button_1(self):
        gpid = self.lineEdit.text()
        usid = self.lineEdit_2.text()
        # print(type(usid))
        # print(usid)
        ZT = AI.User_select(usid, gpid)[1]
        chaxun_info =  AI.User_select(usid, gpid)[0]
        #ZT = AI.User_select(usid, gpid)[1]
        #print(ZT)
        if ZT['error_msg'] =='SUCCESS':
            QMessageBox.information(self, "！！！", "查询成功", QMessageBox.Yes)  # , QMessageBox.No
            self.lineEdit_3.setText(chaxun_info['user_info'])
            self.lineEdit_4.setText(chaxun_info['group_id'])
        else:
            QMessageBox.information(self, "！！！", "查询失败", QMessageBox.Yes)
        # print(chaxun_info)
        # print(ZT['error_msg'])

