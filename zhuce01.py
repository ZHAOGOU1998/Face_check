from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox

from ZHUCE import Ui_Form
from QT import Window

from 百度API import BaiDuAPI
AI = BaiDuAPI()

#Facebase64 = AI.Picture_base("123.jpg")

class zhucu01(QMainWindow,Ui_Form):
    def __init__(self):
        super(zhucu01, self).__init__()
        self.setupUi(self)
        self.Qwindow = Window()
        self.pushButton.clicked.connect(self.Button_1)

    def Button_1(self):
        gpid = self.lineEdit.text()
        usid = self.lineEdit_2.text()
        info = self.lineEdit_3.text()
        #print(gpid)
        l = ("文件中选择图片", "缓存区图片")
        data, ret = QInputDialog.getItem(self, "图片选择", "请从下列窗口选择", l)
        if data =="文件中选择图片":
            #self.label.setText("你选择了：{0}".format(data))
            data = QFileDialog.getOpenFileNames(self,"选择文件")#,"*.jpg","*.png";;;,"Image *.jpg"
            print(data[0])
            #print(0)
            lujing = data[0]
            lj = lujing[0]
            #print(lj)
            fb = AI.Picture_base(lj)

            zhuce_info = AI.Face_regest(fb, gpid, usid, info)
            if zhuce_info =='SUCCESS':
                QMessageBox.information(self, "！！！", "注册成功", QMessageBox.Yes)  # , QMessageBox.No
                self.lineEdit_4.setText(zhuce_info)
            else:
                QMessageBox.information(self, "！！！", "注册失败", QMessageBox.Yes)  # , QMessageBox.No
                self.lineEdit_4.setText(zhuce_info)
        else:
            Facebase64 = AI.Picture_base("123.jpg")
            zhuce_info = AI.Face_regest(Facebase64, gpid, usid, info)  # zhaogou_test01
            #zhuce_info = AI.Face_regest(fb, gpid, usid, info)
            if zhuce_info == 'SUCCESS':
                QMessageBox.information(self, "！！！", "注册成功", QMessageBox.Yes)  # , QMessageBox.No
                self.lineEdit_4.setText(zhuce_info)
            else:
                QMessageBox.information(self, "！！！", "注册失败", QMessageBox.Yes)  # , QMessageBox.No
                self.lineEdit_4.setText(zhuce_info)