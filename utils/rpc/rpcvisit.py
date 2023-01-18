import requests
from common.const import Env

class RpcVisit():
    def __init__(self,XRequestGroup,XRequestService,XRequestMethod):
        if Env.ENV == "test":
            url = "http://ops.test.ximalaya.com/mosn"
        elif Env.ENV == "uat":
            url = "http://ops.uat.ximalaya.com/mosn"
        elif Env.ENV == "release":
            url = "http://ops.ximalaya.com/mosn"
        else:
            pass
        self.url = url

        self.headers = {
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "x-client-app": "mosn-tester",
            # "x-request-group": "xmkp-pms-abtesting",
            "x-request-group": XRequestGroup,
            "x-request-scope": "openapi",
            # "x-request-service": "com.ximalaya.xmkp.abtesting.api.thrift.TAbtestingService$Iface",
            "x-request-service": XRequestService,
            # "x-request-method": "testing",
            "x-request-method": XRequestMethod,
            "x-request-timeout": "2000"
        }

    def Senddata(self,data):
        re = requests.post(url=self.url, json=data, headers=self.headers)

        return re.json()

if __name__ == '__main__':
    client = RpcVisit("xmkp-pms-abtesting", "com.ximalaya.xmkp.abtesting.api.thrift.TAbtestingService$Iface","testing")
    print (client.Senddata({
                  "testingCode": "114",
                  "deviceId": "直接"
                }))