import requests
# url = 'https://test-asp.msfl.com.cn/asp/oss/upload/get-object'
# data =  {
# "data":{
# "objectName":"/email/annex/MSFL-2023-08-0071-Z-001-PH租赁物清单1691567039163.xlsx",
#      "bucketName":"ifc"
# },
# "header":{
# "orderNo":"",
# "sysCode":""
# }
# }
# res = requests.request(url = url,json = data,method='POST')
#
#
# print(res.text)

# import datetime
#
# time =str(datetime.datetime.now().date())
# print(time)
# a=[]
# a.append("1")
# a.append("2")
# print(a)
# a= 0.058
# b = float(a)
# c = b+1
# print(b,c)
# python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse


def dingtalksign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC0bcc0e49cc6b99f9ddb5e978071fa6b509b3bf592bdf64d82a605e2a2eb6ae0a'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign

timestamp, sign = dingtalksign()

token = 'd25e1f48e199321033bb5bc8d7b40f3337482f9a9974e70f3e3b471097c8d497'
url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s'% (
                        token, timestamp, sign)

tagUserid = {"jxw":"15705101126"}
UserIds = []
UserIds.append(tagUserid["jxw"])
headers = {
                        "Content-Type": "application/json",
                        "Charset": "UTF-8"
                    }
message ={
    "msgtype": "text",
    "text": {"content":"测试"},
    "at": {
        "atMobiles": UserIds,
        "isAtAll": False}
}
r = requests.post(url=url, json=message, headers=headers)
print(r.content.decode())
