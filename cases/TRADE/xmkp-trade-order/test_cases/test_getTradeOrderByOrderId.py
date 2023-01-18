import json

from cases.TRADE.enums import StatusCode, OrderError
from utils.tools.base_test_case import BaseTestCase


class TestGetTradeOrderByOrderId(BaseTestCase):
    """
    通过父单号查询子单详情
    """

    def test_not_exist_parent_order_id(self, rpc_client, setupdata, random_qimiao_order_id):
        """
        父单号不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = random_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])
        self.assert_equal(OrderError.ParentOrderNotExist.value, resp["resultMsg"])

    def test_empty_parent_order_id(self, rpc_client, setupdata):
        """
         父单号为空
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.SystemError.value, resp["resultCode"])
        self.assert_equal(OrderError.ParentOrderNotExist.value, resp["resultMsg"])

    def test_exist_parent_order_id(self, rpc_client, setupdata, exist_parent_qimiao_order_id):
        """
        父单号存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])

    def test_optional_source(self, rpc_client, setupdata, exist_parent_qimiao_order_id, random_string):
        """
        可选入参source
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.OK.value, json.loads(resp.content)["resultCode"])
        setupdata["payload"]["params"]["params"]["req"]["source"] = random_string
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.OK.value, json.loads(resp.content)["resultCode"])
