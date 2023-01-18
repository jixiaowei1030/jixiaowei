import requests

class LoginGetToken():
    def __init__(self, mobile, password, env="test"):
        self.env = env
        self.mobile = mobile
        self.password = password

    def GetHost(self, env):
        host = ''
        thirdUrl = {
            # api管理系统，用于获取http应用列表
            # "loginPassport": "https://passport.ximalaya.com/",
            "loginPassport": "http://ops.ximalaya.com/eduOps/product",
            # "uatPassport": "https://passport.uat.ximalaya.com/",
            "uatPassport": "http://ops.uat.ximalaya.com/eduOps/product",
            # "testPassport": "https://passport.test.ximalaya.com/"，
            "testPassport": "http://ops.test.ximalaya.com/eduOps/product"
        };

        if env == 'release':
            host = thirdUrl['loginPassport']
        elif env == 'uat':
            host = thirdUrl['uatPassport']
        elif env == 'test':
            host = thirdUrl['testPassport']

        return host

    def LoginGetToken(self):
        # 1 - 1.获取用户 - 获取登录参数
        host = self.GetHost(self.env)
        mobile = self.mobile
        password = self.password

        # 1 - 2.获取登陆token
        # url1 = "http://ops.test.ximalaya.com/eduOps/product"
        s = requests.Session()
        re = s.get(url=host, allow_redirects=False)
        url2 = re.headers["Location"]

        ltexecution = s.get(url=url2)
        execution = ltexecution.text.split('<input type="hidden" name="execution" value="')[1].split('"/>')[0]
        lt = ltexecution.text.split('name="lt" value="')[1].split('"/>')[0]

        data = {
            "username": mobile,
            "password": password,
            "lt": lt,
            "execution": execution,
            "_eventId": "submit"
        }
        re2 = s.post(url=url2, data=data, allow_redirects=False)

        url3 = re2.headers["Location"]
        re3 = s.get(url=url3, allow_redirects=False)

        url4 = re3.headers["Location"]
        re4 = s.get(url=url4)
        
        return url4.split('ticket-c=')[1].replace(';','')

if __name__ == '__main__':
    print (LoginGetToken('leslie', 'kafka', "test").LoginGetToken())
