
import sys
import time
import os
from cammer import Camera
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog, QFileDialog
from PyQt5 import QtGui
from Ui import Ui_MainWindow
import cv2 as cv
from goongneng import Gongn
from zhuce01 import zhucu01
from shanchu01 import shanchu01
from chaxun01 import chaxun01
from yonghu01 import yonghu01
from shuoming01 import shuoming01
from banben01 import banben01
from daka_setup01 import daka_setup01
#验证百度AI
from 百度API import BaiDuAPI
AI = BaiDuAPI()
class Window(QMainWindow,Ui_MainWindow):

    def __init__(self):
        self.GN = Gongn()
        self.students = [0]
        self.n =1
        self.sum = 5
        self.conter = 0
        self.location_x = 1
        self.name_falg = 0
        super(Window,self).__init__()
        self.setupUi(self)
        self.Cam = False
        self.BDapi = False
        self.actionopen.triggered.connect(self.openCap)
        self.actionclose.triggered.connect(self.closeCap)
        self.Cam = False
        self.actionFace_regest.triggered.connect(self.Face_regest)#人脸注册
        self.actiondelete.triggered.connect(self.delete)#删除
        self.actionselect.triggered.connect(self.select)#识别
        self.actionuserlist.triggered.connect(self.userlist)
        self.actionbegin_daka.triggered.connect(self.sutup_daka)#打卡前设置
        self.actionexplain.triggered.connect(self.explain)#说明
        self.actionversion.triggered.connect(self.version)#版本
        self.tm = QTimer()
        self.tm.timeout.connect(self.timeout1)
        self.qtm = QTimer()
        self.qtm.timeout.connect(self.timout2)
        self.local_tm = QTimer()
        self.local_tm.timeout.connect(self.timeout3)
        self.pushButton.clicked.connect(self.Button_1)
        self.pushButton_2.clicked.connect(self.Button_2)
        #self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.Button_3)
        self.pushButton_4.clicked.connect(self.Button_4)
        #导入子窗口
        self.w_zhuce = zhucu01()
        self.w_shanchu = shanchu01()
        self.w_chaxun = chaxun01()
        self.w_yonghu = yonghu01()
        self.w_shuoming = shuoming01()
        self.w_banben = banben01()
        self.w_setup = daka_setup01()
        # backgd = QtGui.QPixmap("背景.png")
        # backgd = backgd.scaled(self.label_18.width(),self.label_18.height())
        # self.label_18.setPixmap(backgd)
    def openCap(self):
        self.Cam = Camera()
        self.tm.start(30)

    def closeCap(self):
        self.Cam.Close()
        self.tm.stop()
        self.qtm.stop()

    def timeout3(self):
        self.label_4.setText(self.GN.Get_time())

    def timout2(self):#定时拍摄照片
        self.sum1 = self.w_setup.Button()[1]
        self.xl_name = self.w_setup.Button()[0]
        if self.sum1 =="":
            self.sum1 =self.sum
        if self.xl_name =="":
            self.xl_name ="测试表"
        self.sum1 = int(self.sum1)
        print(type(self.sum1))
        self.label_14.setNum(self.sum1)
        flag = self.Cam.face_detect_demo(self.Cam.Read())[1]
        if flag > 0:
            Vshow = self.Cam.Read()
            cv.imwrite("123.jpg", Vshow)  # E:/hzy/1/opencv/

            pic = QtGui.QPixmap("123.jpg")#opencv123.jpg
            #pic = pic.scaled(self.label_2.width(),self.label_2.height())
            self.label_2.setPixmap(pic)
            #print("拍照成功！")

            self.BDapi = BaiDuAPI()
            Facebase64 = AI.Picture_base("123.jpg")
            self.BDapi.Face_recognition(Facebase64)
            #self.BDapi.Face_Check(Facebase64,"zhaogou_test01,test,A507")
            check =self.BDapi.Face_Check(Facebase64,"zhaogou_test01,test,A507")#zhaogou_test01,test,
            if check[0] ==0:
                QMessageBox.information(self, "检测失败", "人脸缺少活性", QMessageBox.Yes)  # , QMessageBox.No
            else:

                if check[3]<90:
                    QMessageBox.information(self, "！！！", "不在数据库中，相似度{0}".format(check[3]), QMessageBox.Yes)

                else:
                    self.lineEdit.setText(check[0])
                    self.lineEdit_2.setText(check[1])
                    self.lineEdit_3.setText(check[2])
                    sc = str(check[3])
                    self.lineEdit_4.setText(sc)
                    self.students.append(check[2])
                    print(self.students)
                    print(self.students[self.n])
                    if self.students[self.n] ==self.students[self.n -1]:
                        #name = self.students[self.n]
                        if self.name_falg ==0:
                            QMessageBox.information(self, "！！！", "已完成签到", QMessageBox.Yes)
                            self.name_falg +=1
                        #print("已完成签到")
                    else:
                        self.name_falg =self.name_falg - self.name_falg
                        self.conter +=1
                        n =self.sum1 -self.conter
                        self.label_16.setNum(n)
                        self.label_15.setNum(self.conter)
                        self.textEdit_2.append(check[2])
                        self.cg_xlname = self.xl_name + ".xls"

                        if self.location_x ==1:
                            self.GN.Write_xl(self.xl_name, 0, "组号", "ID号", "姓名", "打卡时间", self.cg_xlname)
                            self.GN.change_xl(self.cg_xlname,self.location_x,check[0],check[1],check[2],self.label_4.text(),self.cg_xlname)
                            self.pushButton_3.setEnabled(True)
                        else:
                            self.GN.change_xl(self.cg_xlname, self.location_x, check[0], check[1], check[2],
                                              self.label_4.text(), self.cg_xlname)
                            self.pushButton_3.setEnabled(True)
                        self.location_x +=1
                    self.n += 1
                    #print(self.n)
                    self.textEdit.setText(self.BDapi.Face_recognition(Facebase64))
    def timeout1(self):#显示视频

        img = self.Cam.face_detect_demo(self.Cam.Read())[0]#self.Cam.Read()
        #print(flag)
        img = self.Cam.cvimg_to_QPixmap(img)

        self.label.setPixmap(img)

    def Button_1(self):
        self.qtm.start(5000)#3s打一次卡
        #print(self.label.text())
        if self.label.text() == "摄像头":
            QMessageBox.information(self, "！！！", "请先打开摄像头", QMessageBox.Yes)#, QMessageBox.No
        else:
            flag = self.Cam.face_detect_demo(self.Cam.Read())[1]
            if flag >0:
                Vshow = self.Cam.Read()
                cv.imwrite("123.jpg", Vshow)  # E:/hzy/1/opencv/
                pic = QtGui.QPixmap("123.jpg")

                self.label_2.setPixmap(pic)
                print("拍照成功！")

    def Button_2(self):

        if self.label.text() == "摄像头":
            QMessageBox.information(self, "！！！", "请先打开摄像头", QMessageBox.Yes)#, QMessageBox.No
        else:
            print(0)
            flag = self.Cam.face_detect_demo(self.Cam.Read())[1]
            if flag >0:
                Vshow = self.Cam.Read()
                cv.imwrite("123.jpg", Vshow)  # E:/hzy/1/opencv/
                pic = QtGui.QPixmap("123.jpg")
                self.label_2.setPixmap(pic)
                print("拍照成功！")

    def Button_3(self):

        data ,ret = QFileDialog.getOpenFileNames(self, "选择文件", "*.xls")  # ,"Image *.png;;"
        os.system(data[0])
        # print(data)
        # print(ret)
        print(0)
    def Button_4(self):
        exit()
    def tanchuang(self):
        QMessageBox.information(self, "xiaoxi", "赵狗", QMessageBox.Yes, QMessageBox.No)

    def TM(self):
        self.label_4.setText(self.GN.Get_time())
        #print(0)

    def Face_regest(self):
        #print("注册")
        self.w_zhuce.show()

    def delete(self):
        #print("删除")
        self.w_shanchu.show()

    def select(self):
        #print("查询")
        self.w_chaxun.show()
        #AI.User_select("02", "A507")

    def userlist(self):
        #AI.All_users("A507")
        self.w_yonghu.show()
    def sutup_daka(self):
        #print("daka")
        self.w_setup.show()
        #print(self.w_setup.Button())
    def explain(self):
        #print("说明")
        self.w_shuoming.show()
    def version(self):
        #print("版本")
        self.w_banben.show()

if __name__ =="__main__":

    Facebase64 = AI.Picture_base("123.jpg")
    Token = AI.GetToken()
    app = QApplication(sys.argv)
    w = Window()
    locol_tm =w.local_tm.start(10)
    w.show()
    w.activateWindow()
    app.exec()

    sys.exit(0)


