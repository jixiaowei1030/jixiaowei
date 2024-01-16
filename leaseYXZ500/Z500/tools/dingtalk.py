from Z500.tools import dingtalksign
import requests

def send_notify(env,custName,projectNo):
    timestamp, sign = dingtalksign.dingtalksign()

    token = 'd25e1f48e199321033bb5bc8d7b40f3337482f9a9974e70f3e3b471097c8d497'
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (
        token, timestamp, sign)

    tagUserid = {"jxw": "15705101126","xzw":"13623859715","fht": "15705101126","cm": "15705101126","zll": "15705101126"}
    UserIds = []
    UserIds.append(tagUserid[custName])
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {"content": "%s在%s环境新建项目成功，项目编号为%s"%(custName,env,projectNo)},
        "at": {
            "atMobiles": UserIds,
            "isAtAll": False}
    }
    r = requests.post(url=url, json=message, headers=headers, verify=False)
    print(r.content.decode())

def send_notify_approve(env,custName,projectNo):
    timestamp, sign = dingtalksign.dingtalksign()

    token = 'd25e1f48e199321033bb5bc8d7b40f3337482f9a9974e70f3e3b471097c8d497'
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (
        token, timestamp, sign)

    tagUserid = {"jxw": "15705101126","xzw":"13623859715","fht": "15705101126","cm": "15705101126","zll": "15705101126"}
    UserIds = []
    UserIds.append(tagUserid[custName])
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {"content": "%s在%s环境审批成功，项目编号为%s"%(custName,env,projectNo)},
        "at": {
            "atMobiles": UserIds,
            "isAtAll": False}
    }
    r = requests.post(url=url, json=message, headers=headers, verify=False)
    print(r.content.decode())