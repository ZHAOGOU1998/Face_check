#Opencv基础类
#from PIL import Image,ImageDraw,ImageFont

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtGui
from 百度API import BaiDuAPI
AI = BaiDuAPI()
class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        #self.Win = Window()
    def Read(self):
        if self.cap.isOpened():
            ret,img =self.cap.read()
            if ret :
                return img
        #self.Win.tanchuang()
        return False

    def face_detect_demo(self,img):
        gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_detect = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')#'D:/python(opencv)/opencv/sources/data/haarcascades;;;C:/Users/716/Desktop/HZY_dabian/haarcascades
        face = face_detect.detectMultiScale(gary)#,1.03,5,0,(100,100),(300,300)
        flag =0
        for x, y, w, h in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 255), thickness=3)
            flag +=1
            #print(flag)
        #cv2.imshow('result', img)
        #print(flag)
            # FC = AI.Picture_base("opencv123.jpg")
            # fc = AI.Face_Check(FC, "zhanggou_test01,zhaogou_test01,A507")
            # s = fc[2]
            # cv2.putText(img,s, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        p =[img,flag]
        return p#,flag      #p[img,x,y]
    def cvimg_to_QPixmap(self, cvimg):
        # print('图像转换')
        self.currentFrame = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        # self.currentFrame = cv2.resize(self.currentFrame, (640, 480))
        # print('图像设置 大小')  # 摄像头读取大小即 w * h = 640 * 480
        try:
            height, width = self.currentFrame.shape[:2]
            img = QImage(self.currentFrame, width, height,
                         QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            # print("图像获取OK")
            return img
        except:
            return None


    def Close(self):
        if self.cap.isOpened():
            self.cap.release()




