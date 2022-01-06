import sys
from cammer import Camera
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui import Ui_MainWindow
from 百度API import BaiDuAPI
import cv2 as cv

class Window(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        self.Cam = False
        self.BDapi = False
        self.actionopen.triggered.connect(self.openCap)
        self.actionclose.triggered.connect(self.closeCap)
        self.Cam = False

        self.tm = QTimer()
        self.tm.timeout.connect(self.timeout)

        self.pushButton.clicked.connect(self.Button_1)
        self.pushButton_2.clicked.connect(self.Button_2)
    def openCap(self):
        self.Cam = Camera()
        self.tm.start(30)

    def closeCap(self):
        self.Cam.Close()
        self.tm.stop()

    def timeout(self):
        img = self.Cam.Read()
        img = self.Cam.cvimg_to_QPixmap(img)
        self.label.setPixmap(img)

    def Button_1(self):

        Vshow = self.Cam.Read()
        #cv.imshow("Capture", Vshow)
        cv.imwrite("D:/Users/716/PycharmProjects/HZY_dabian/"+"123"+".jpg",Vshow)
        #self.label.setPixmap("123.jpg")
        print("拍照成功！")
    def Button_2(self):
        self.BDapi = BaiDuAPI()
        #self.BDapi.Face_recognition()
        #self.BDapi.api()
        print(2)

class Main:
    def Window_show(self):
        app = QApplication(sys.argv)
        w = Window()
        w.show()
        w.activateWindow()
        app.exec()
        sys.exit(0)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Window()
#     w.show()
#     w.activateWindow()
#     app.exec()
#     sys.exit(0)