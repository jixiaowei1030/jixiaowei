import requests
import demjson
import json


class LoginGetToken():
    def __init__(self,moblie, env="test"):
        self.env = env
        self.moblie = moblie

    def GetHost(self,env):
        host = ''
        thirdUrl = {
            # api管理系统，用于获取http应用列表
            "loginPassport": "https://m.ximalaya.com/xmkp-math-thinking/api/login/verifyPhone",
            "loginPassToken": "https://m.ximalaya.com/xmkp-math-thinking/api/login/loginAfterCheck",
            "uatPassport": "https://m.uat.ximalaya.com/xmkp-math-thinking/api/login/verifyPhone",
            "uatPassToken": "https://m.uat.ximalaya.com/xmkp-math-thinking/api/login/loginAfterCheck",
            "testPassport": "https://m.test.ximalaya.com/xmkp-math-thinking/api/login/verifyPhone",
            "testPassToken": "https://m.test.ximalaya.com/xmkp-math-thinking/api/login/loginAfterCheck"
        };

        if env == 'release':
            host = thirdUrl['loginPassport']
            tokenhost = thirdUrl['testPassToken']
        elif env == 'uat':
            host = thirdUrl['uatPassport']
            tokenhost = thirdUrl['testPassToken']
        elif env == 'test':
            host = thirdUrl['testPassport']
            tokenhost = thirdUrl['testPassToken']

        return host,tokenhost

    def LoginGetToken(self):
        # 1 - 1.获取用户 - 获取登录参数
        host,tokenhost = self.GetHost(self.env)
        moblie = self.moblie

        # 1 - 2.获取登陆token
        s = requests.Session()
        headers = {"Content-Type": "application/json"}
        data = {
            "uid":"0",
            "code":"111111",
            "phone":moblie,
            "deviceModel":"ELS-AN00",
            "deviceCode":"e6fe87e590abfddaeb8601e9ac7393d8"
        }
        re2 = requests.post(url=host, data=demjson.encode(data), headers=headers)
        print (re2)

        data = {
            "phone": moblie,
        }
        re3 = requests.post(url=tokenhost, data=demjson.encode(data), headers=headers)
        data = json.loads(re3.text)

        return data["data"]["token"]

if __name__ == '__main__':
    print (LoginGetToken("leslie", "kafka").LoginGetToken())