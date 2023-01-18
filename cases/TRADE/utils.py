import json

from attrdict import AttrDict


def resp_to_attrdict(json_data):
    """
    rpc接口固定的返回数据结构
    {
        "targetApplication": "xmkp-trade-settlement",
        "cost": 5,
        "IDLid": 23175,
        "env": "TEST",
        "content": "{\n\t\"data\":{\n\t\t\"rechargeStatus\":3,\n\t\t\"reqSource\":\"ShiShuaiGangTest\",\n\t\t\"reqId\":\"1631696002813\"\n\t},\n\t\"resultCode\":\"96603001\",\n\t\"resultMsg\":\"充值金额不能为空\"\n}",
        "email": "joe.shi@ximalaya.com"
    }
    所有的结果都在content中
    """
    return AttrDict(json.loads(json_data.content))
