# -*- coding: utf-8 -*-
import json
import time
from decimal import Decimal
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcsl_v1_5
import base64
import hashlib

import inspect


class LoginGetToken():
    def __init__(self, mobile, password, env):
        self.url = 'http://auto.test.ximalaya.com/api/open/handle_login'
        self.data = {
            "_id": "607d1788f4cba8305495cc9c",
            "name": mobile,
            "password": password,
            "website": "mobile",
            "env": "test",
            "desc": ""
        }
        self.mobile = mobile
        self.password = password
        self.env = env

    def Gettoken(self):
        request = requests.request('POST', self.url, data=self.data)
        json_result = json.loads(request.text)
        token = json_result['data']['res']
        return token

    def PublicEncrypt(self, data):
        # 得到公钥
        publicKey = '-----BEGIN PUBLIC KEY-----\n' + \
                    'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVhaR3Or7suUlwHUl2Ly36uVmboZ3+HhovogDjLgRE9CbaUokS2eqGaVFfbxAUxFThNDuXq/fBD+SdUgppmcZrIw4HMMP4AtE2qJJQH/KxPWmbXH7Lv+9CisNtPYOlvWJ/GHRqf9x3TBKjjeJ2CjuVxlPBDX63+Ecil2JR9klVawIDAQAB\n' + \
                    '-----END PUBLIC KEY-----\n';
        a = bytes(data, encoding="utf8")

        rsakey = RSA.importKey(publicKey)

        cipher = Cipher_pkcsl_v1_5.new(rsakey)

        base64Str = str(base64.b64encode(cipher.encrypt(a)), "utf8")

        return base64Str

    def GetHost(self, env):
        thirdUrl = {
            # api管理系统，用于获取http应用列表
            "opsProjectList": "http://ops.ximalaya.com/api-manager-open-api/project/getProjectList?pageSize=2000",
            "opsProjectInfo": "http://ops.ximalaya.com/api-manager-open-api/project/getProjectInfo?projectId=",
            "opsLogin": "http://ops.ximalaya.com/cas-server/login?locale=zh_CN&service=",
            "opsLogout": "http://ops.ximalaya.com/cas-server/logout?locale=zh_CN&service=",
            "opsPassport": "http://cms.9nali.com/thriftTester/v3/noauth/invoke.htm",
            "thriftTester": "http://192.168.3.54:8901/thriftTester",
            "thriftTesterInvoke": "http://192.168.3.54:8901/thriftTester/invoke.htm",
            "loginPassport": "https://passport.ximalaya.com/",
            "uatPassport": "https://passport.uat.ximalaya.com/",
            "testPassport": "https://passport.test.ximalaya.com/",
            "workbenchSaveCase": "http://yunxiao.xmly.work/workbench/apiresult/saveTestresult",
            "localWorkbenchSaveCase": "http://127.0.0.1:8000/workbench/apiresult/saveTestresult",
            "testWorkbenchSaveCase": "http://192.168.60.245:8080/workbench/apiresult/saveTestresult",
            "MainstayAdmin": "http://cms.9nali.com/mainstay-admin/",  # mainstay后台
        };

        # 设置后端请求host
        host = ''
        if env == 'release':
            host = thirdUrl['loginPassport']
        elif env == 'uat':
            host = thirdUrl['uatPassport']
        elif env == 'test':
            host = thirdUrl['testPassport']

        return host

    def GetNonce(self, host, website):
        # 1 - 2.用户登录 - 获取nonce
        nonce = ''
        timestamp = time.time()
        timestamp = str(Decimal((timestamp / 1000)).quantize(Decimal('0.00')))
        # 例如： / release / mobile / nonce / 1565672271.50 -> https: // passport.ximalaya.com / mobile / nonce / 1565672271.50
        result = requests.request('GET', host + website + '/nonce/' + timestamp ,verify=False)
        resultes = json.loads(result.text)
        if resultes["ret"] == 0:
            nonce = resultes["nonce"]
        else:
            print({
                'status': False,
                'res': '登录失败: 获取nonce失败'
            })
        return nonce

    def GetUserSignature(self, website, env, user, nonce, encrypt_pwd):
        appSecret = 'MOBILE-V1-PRODUCT-7D74899B338B4F348E2383970CC09991E8E8D8F2BC744EF0BEE94D76D718C089'  # mobile 线上
        appuatSecret = 'MOBILE-V1-TEST-63B2E1D0E0DD40928342D3D9BC8AC4956F9DD8637BF04853B49F0690FD3BE684'  # mobile 测试 / uat
        webSecret = 'WEB-V1-PRODUCT-E7768904917C4154A925FBE1A3848BC3E84E2C7770744E56AFBC9600C267891F'  # web & h5 线上
        webuatSecret = 'WEB-V1-TEST-08A5F0C2A54B4F899E3F9ECFE14DC128B6D1FB3F5FB744ABB76BEAA9534D3B2F'  # web & h5 测试 / uat

        Secret = ''
        if website == 'mobile':
            # mobile
            if env == 'release':
                Secret = appSecret  # 线上
            else:
                Secret = appuatSecret  # uat & test
        else:
            #  web & h5
            if env == 'release':
                Secret = webSecret  # 线上
            else:
                Secret = webuatSecret  # uat & test

        #  使用 & 连接
        params = {
            'account': user,
            'nonce': nonce,
            'password': encrypt_pwd
        }

        key = ''
        for p in params:
            key += p + '=' + params[p] + '&'
        # // 拼接客户端的securityKey
        key = key + Secret
        #  url转换为大写
        key = key.upper()
        # SHA1(url)
        sha = hashlib.sha1(key.encode('utf-8'))
        signature = sha.hexdigest()
        return signature

    def LoginGetToken(self):
        # 1 - 1.用户登录 - 获取登录参数
        # 15055555550 xmly9876054321 mobile release
        user = self.mobile
        password = self.password
        env = self.env
        website = "mobile"
        if website == 'web' or website == 'h5':
            website = 'mobile'

        host = self.GetHost(env)

        # 1 - 2.用户登录 - 获取nonce
        nonce = self.GetNonce(host, website)
        # 1 - 3.用户登录 - 密码rsa加密处理
        encrypt_pwd = self.PublicEncrypt(password)
        # 1 - 4.用户登录 - 生成签名
        signature = self.GetUserSignature(website, env, user, nonce, encrypt_pwd)
        # 1 - 5.用户登录 - 密码登录
        data = {
            'account': user,
            'password': encrypt_pwd,
            'nonce': nonce,
            'signature': signature
        }

        one_token = ''
        headers = {
            "Content-Type": "application/json",
        }


        res = requests.request('POST', host + website + '/login/pwd/v1', data=json.dumps(data), headers=headers ,verify=False)
        resultes = json.loads(res.text)
        if resultes["ret"] == 0:
            one_token = str(resultes["uid"]) + '&' + str(resultes["token"])
        else:
            print({'status': False, 'res': resultes["msg"] + '登录失败'})
        return one_token


if __name__ == '__main__':
    # login = LoginGetToken("17602163851", "asdf3.14", "test")
    login = LoginGetToken("18056548888", "zxc123456", "test")
    print(login.Gettoken())
    print(login.LoginGetToken())
