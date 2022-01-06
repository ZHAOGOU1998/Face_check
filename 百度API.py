import requests
import base64

from PyQt5.QtWidgets import QMessageBox, QMainWindow

AK = '2anRVVTrGYrnBURgSP4AbIjN'
SK = 'dA598q4POLMWgQosFIwo0NtHL4Vw1lFE'

class BaiDuAPI():
    def __init__(self):
        self.access_tonken = self.GetToken()
    def GetToken(self):

        host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}".format(
            AK, SK)
        response = requests.get(host)
        #access_token = ""
        if response:
            self.ret = response.json()
            access_token = self.ret["access_token"]
            return access_token
            #print(access_token)
        else:
            print("access_token 获取失败")
            return False
    #人脸特征检测
    def Face_recognition(self,Facebase64):
        #self.Picture_base()
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

        params = {"image": Facebase64, "image_type": "BASE64", "face_field": "age,gender,expression,face_shape,glasses,emotion"}
        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        # if response:
             #print(response.json())
        self.ret = response.json()
        if self.ret['error_msg'] == 'SUCCESS':
            face_num = self.ret['result']['face_num']
            print("人脸数目:", face_num)
            if face_num > 0:
                for face in self.ret['result']['face_list']:
                    face_location = face['location']
                    age = face["age"]
                    sex = face['gender']['type']
                    if sex == "female":
                        sex = "女"
                    else:
                        sex = "男"

                    expression = face["expression"]['type']
                    if expression == "none":
                        expression = "不笑"
                    elif expression == "smile":
                        expression = "笑"
                    elif expression == "laugh":
                        expression = "大笑"

                    face_shape = face["face_shape"]["type"]
                    if face_shape == "square":
                        face_shape = "正方形"
                    elif face_shape == "triangle":
                        face_shape = "三角形"
                    elif face_shape == "oval":
                        face_shape = "椭圆"
                    elif face_shape == "heart":
                        face_shape = "心型"
                    elif face_shape == "round":
                        face_shape = "圆形"

                    glasses = face["glasses"]["type"]
                    if glasses == "none":
                        glasses = "无眼镜"
                    elif glasses == "common":
                        glasses = "普通眼镜"
                    elif glasses == "sun":
                        glasses = "墨镜"

                    emotion = face["emotion"]["type"]
                    if emotion == "angry":
                        emotion = "愤怒 "
                    elif emotion == "disgust":
                        emotion = "厌恶 "
                    elif emotion == "fear":
                        emotion = "恐惧 "
                    elif emotion == "happy":
                        emotion = "高兴 "
                    elif emotion == "sad":
                        emotion = "伤心 "
                    elif emotion == "surprise":
                        emotion = "惊讶 "
                    elif emotion == "neutral":
                        emotion = "无表情"
                    elif emotion == "pouty":
                        emotion = "撅嘴 "
                    elif emotion == "grimace":
                        emotion = "鬼脸"

                    s= ("人脸年龄:{0},{1},表情:{2},脸型:{3},眼镜:{4},情绪:{5}".format(age, sex, expression, face_shape, glasses,
                                                                            emotion))
            #print("人脸检测成功")
            return s
        else:print("人脸检测失败")
    def Picture_base(self,pic):
        f = open(pic, "rb")#opencv123.jpg;
        res = f.read()
        s = base64.b64encode(res)
        return s

    # 人脸注册
    def Face_regest(self,Facebase64,GroupName,Userid,Userinfo):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"

        params = {"image":Facebase64,"image_type":"BASE64","group_id":GroupName,"user_id":Userid,"user_info":Userinfo,"quality_control":"LOW","liveness_control":"NORMAL"}

        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        # if response:
        #      print(response.json())
        self.ret = response.json()
        if self.ret['error_msg'] == 'SUCCESS':
             print("人脸注册成功")
             return self.ret['error_msg']
        else:
            print("人脸注册失败")
            return self.ret['error_msg']



    #人脸删除
    def Face_del(self,Userid,GroupName,Face_token):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete"

        params = {"group_id": GroupName, "user_id": Userid,"face_token":Face_token}

        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        # if response:
        #     print(response.json())
        self.ret = response.json()
        if self.ret['error_msg'] == 'SUCCESS':
            print("用户删除成功")
            return self.ret['error_msg']
        else:
            print("用户删除失败")
    #查询用户
    def User_select(self,Userid,Groupid):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get"
        params = {"user_id":Userid,"group_id":Groupid}
        #access_token = '[调用鉴权接口获取的token]'
        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        # if response:
        #     #print(0)
        #     print(response.json())
        self.ret = response.json()

        if self.ret['error_msg'] == 'SUCCESS':
            print("用户表查询成功")
            self.result = self.ret['result']
            self.uslist = self.result['user_list']
            self.usinfo = self.uslist[0]
            S = [self.usinfo, self.ret]
            #print(S)
            return S
        else:
            print("用户表查询失败")
            s = [{'user_info': '查询出错'},self.ret]
            return s

    #人脸搜索
    def Face_Check(self,Facebase64,GroupList):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
        params = {"image":Facebase64,"image_type":"BASE64","group_id_list":GroupList,"quality_control":"LOW","liveness_control":"NORMAL"}
        #access_token = '[调用鉴权接口获取的token]'
        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
        #     print(1)
            #print(response.json())
            self.ret = response.json()
            #print(self.ret)
        if self.ret['error_msg'] == 'SUCCESS':
            self.re = self.ret['result']
            s = self.re['user_list']

            u_list = s[0]
            gpid = u_list['group_id']
            usid = u_list['user_id']
            usinfo = u_list['user_info']
            sc = u_list['score']
            user_list = [gpid, usid, usinfo, sc]
            print("人脸搜索成功")
            return user_list
        else:
            user_list = [0,0,0,0]
            return user_list
            print("人脸搜索失败")

    #查询所有用户
    def All_users(self,Groupid):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"

        params = {"group_id":Groupid}
        #access_token = '[调用鉴权接口获取的token]'
        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            self.ret = response.json()
            #print(self.ret)
        if self.ret['error_msg'] == 'SUCCESS':
            self.result = self.ret['result']
            self.us_id_lt = self.result['user_id_list']
            #print(self.us_id_lt)
            return self.us_id_lt
        # else:
        #     return

    #人脸对比
    def Face_compa(self,Facebase64_1,Facebase64_2):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

        params = [{"image": Facebase64_1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
        {"image": Facebase64_2, "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"}]
        #access_token = '[调用鉴权接口获取的token]'
        request_url = request_url + "?access_token=" + self.access_tonken
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, json=params, headers=headers)
        if response:
            print(response.json())
