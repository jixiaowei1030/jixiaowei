import json

from cases.TRADE.enums import StatusCode, OrderError
from utils.tools.base_test_case import BaseTestCase


class TestGetSubTradeOrderByXmOrderId(BaseTestCase):
    """
    通过喜马订单号查询奇妙订单号
    """

    def test_not_exist_xima_order_id(self, rpc_client, setupdata, random_xima_order_id):
        """
        喜马订单号不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["xmOrderId"] = random_xima_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OrderNotExist.value, resp["resultCode"])
        self.assert_equal(OrderError.OrderNotExist.value, resp["resultMsg"])

    def test_empty_xima_order_id(self, rpc_client, setupdata):
        """
        喜马订单号为空
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])

    def test_exist_xima_order_id(self, rpc_client, setupdata, exist_xm_order_id):
        """
        喜马订单号存在
        """
        setupdata["payload"]["params"]["params"]["req"]["xmOrderId"] = exist_xm_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"], error_msg="喜马订单号不存在")
