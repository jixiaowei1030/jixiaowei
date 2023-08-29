from Z500.tools import dingtalksign
import requests

def send_notify(custName,projectNo):
    timestamp, sign = dingtalksign.dingtalksign()

    token = 'd25e1f48e199321033bb5bc8d7b40f3337482f9a9974e70f3e3b471097c8d497'
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (
        token, timestamp, sign)

    tagUserid = {"jxw": "15705101126"}
    UserIds = []
    UserIds.append(tagUserid["jxw"])
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {"content": "%s新建项目成功，项目编号为%s"%(custName,projectNo)},
        "at": {
            "atMobiles": UserIds,
            "isAtAll": False}
    }
    r = requests.post(url=url, json=message, headers=headers, verify=False)
    print(r.content.decode())