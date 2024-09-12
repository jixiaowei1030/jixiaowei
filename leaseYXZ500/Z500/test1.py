#encoding='utf-8'
import datetime
# import requests
# # url = 'https://test-asp.msfl.com.cn/asp/oss/upload/get-object'
# # data =  {
# # "data":{
# # "objectName":"/email/annex/MSFL-2023-08-0071-Z-001-PH租赁物清单1691567039163.xlsx",
# #      "bucketName":"ifc"
# # },
# # "header":{
# # "orderNo":"",
# # "sysCode":""
# # }
# # }
# # res = requests.request(url = url,json = data,method='POST')
# #
# #
# # print(res.text)
#
# # import datetime
# #
# # time =str(datetime.datetime.now().date())
# # print(time)
# # a=[]
# # a.append("1")
# # a.append("2")
# # print(a)
# # a= 0.058
# # b = float(a)
# # c = b+1
# # print(b,c)
# # python 3.8
# import time
# import hmac
# import hashlib
# import base64
# import urllib.parse
#
#
# def dingtalksign():
#     timestamp = str(round(time.time() * 1000))
#     secret = 'SEC0bcc0e49cc6b99f9ddb5e978071fa6b509b3bf592bdf64d82a605e2a2eb6ae0a'
#     secret_enc = secret.encode('utf-8')
#     string_to_sign = '{}\n{}'.format(timestamp, secret)
#     string_to_sign_enc = string_to_sign.encode('utf-8')
#     hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
#     sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
#     return timestamp, sign
#
# timestamp, sign = dingtalksign()
#
# token = 'd25e1f48e199321033bb5bc8d7b40f3337482f9a9974e70f3e3b471097c8d497'
# url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s'% (
#                         token, timestamp, sign)
#
# tagUserid = {"jxw":"15705101126"}
# UserIds = []
# UserIds.append(tagUserid["jxw"])
# headers = {
#                         "Content-Type": "application/json",
#                         "Charset": "UTF-8"
#                     }
# message ={
#     "msgtype": "text",
#     "text": {"content":"测试"},
#     "at": {
#         "atMobiles": UserIds,
#         "isAtAll": False}
# }
# r = requests.post(url=url, json=message, headers=headers)
# print(r.content.decode())


# import asyncio
#
#
# async def foo():
#     await asyncio.sleep(2)  # 模拟耗时操作
#     print("异步任务完成")
#
#
# async def main():
#     print("开始执行异步任务")
#     await asyncio.gather(foo(), foo())  # 同时执行多个异步任务
#     print("所有异步任务执行完毕")
#
#
# asyncio.run(main())
# import datetime
# print(datetime.datetime.now().date()+datetime.timedelta(days=1))
# a= "    abc "
# print(len(a))
# a.strip()
# print(len(a.strip()))

import urllib.request
import base64

# import requests
#
# url='http://test-vrip.msfl.com.cn/web-cs/web/cs/v1/doc/631131785879056384/preview'
# # response=urllib.request.urlopen(url)
# # string=response.read()
# # print(string)
# # html=string.decode('utf-8')
# # print(html)
#
# res = requests.get(url)
#
#
# print(res.content)



# import requests
# url='http://www.baidu.com/'
# response = requests.get(url)
# print(response)   # 打印状态码
# print(response.content.decode())  # 第三种方法


#
# str ="2.1.1甲方与乙方签订编号"
# print(len(str))


# import random
# from random import choice
# list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# PCC_wi=[1,3,5,7,11,2,13,1,1,17,19,97,23,29];
# d = random.randint(1,100)
# while True:
#     result = 0
#     sum = 0
#     code = []
#     for i in range(14):
#         # print(i)
#         a = choice(list)
#         code.append(a)
#         c = list.index(a)
#         b = PCC_wi[i]
#         sum += b*c
#     result = sum%97 +1
#     if result == d :
#         # print(code)
#         break;
# if d <10:
#     print(''.join(code)+'0'+ str(d))
# else:
#     print(''.join(code)+ str(d))
#
#

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(1.03**204)

# {"id": "10910",
# "did": "10911",
# "mid": "10912",
# "dname": "测试手环3",
# "assetId": "1733374431032481111",
# "assetNo": "LH00001098",
# "assetName": "第一个租赁物",
# "contract_no": "MSFL-2024-01-0028-Z-001-PH",
# "atype": "1",
# "alevel": "1",
# "adesc": "测试告警推送0119",
# "atime": "2024-01-19 14:13:28",
# "no": "10913"
# }
