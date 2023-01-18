import json

from cases.TRADE.enums import StatusCode
from utils.tools.base_test_case import BaseTestCase


class TestUpdateXmOrderId(BaseTestCase):
    """
    desc: 修改奇妙订单对应的喜马订单号
    """

    def test_no_exist_qimiao_order_id(self, rpc_client, random_qimiao_order_id, setupdata):
        """
        不存在的奇妙订单号
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = random_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])

    def test_exist_qimiao_order_id(self, rpc_client, db_client, exist_qimiao_order_id, random_xima_order_id, setupdata):
        """
        存在的奇妙订单号
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_qimiao_order_id
        setupdata["payload"]["params"]["params"]["req"]["xmOrderId"] = random_xima_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])
        sql = f"select xm_order_id from xmkp_trade_order.sub_trade_order where sub_order_id ='{exist_qimiao_order_id}'"
        self.assert_equal(random_xima_order_id, db_client.query(sql).xm_order_id)  # db内检查写入是否成功

    def test_opitinal_param(self, rpc_client, exist_qimiao_order_id, random_xima_order_id, setupdata):
        """
        可选入参字段source
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_qimiao_order_id
        setupdata["payload"]["params"]["params"]["req"]["xmOrderId"] = random_xima_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])

    def test_empty_qimiao_order_id(self, rpc_client, random_xima_order_id, setupdata):
        """
        奇妙订单号不能为空
        """
        setupdata["payload"]["params"]["params"]["req"]["xmOrderId"] = random_xima_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])

    def test_empty_xima_order_id(self, rpc_client, exist_qimiao_order_id, setupdata):
        """
        喜马订单号不能为空
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])
