import json

from cases.TRADE.enums import StatusCode, OrderError
from utils.tools.base_test_case import BaseTestCase


class TestGetSubTradeOrderByOrderId(BaseTestCase):
    """
    通过子单号查询子单详情
    """

    def test_not_exist_order_id(self, rpc_client, setupdata, random_qimiao_order_id):
        """
        子单号不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = random_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OrderNotExist.value, resp["resultCode"])
        self.assert_equal(OrderError.SubOrderNotExist.value, resp["resultMsg"])

    def test_empty_order_id(self, rpc_client, setupdata):
        """
         子单号为空
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OrderNotExist.value, resp["resultCode"])
        self.assert_equal(OrderError.SubOrderNotExist.value, resp["resultMsg"])

    def test_exist_order_id(self, rpc_client, setupdata, exist_qimiao_order_id):
        """
        子单号存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])

    def test_optional_source(self, rpc_client, setupdata, exist_qimiao_order_id, random_string):
        """
        可选入参source
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])
        setupdata["payload"]["params"]["params"]["req"]["source"] = random_string
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])
