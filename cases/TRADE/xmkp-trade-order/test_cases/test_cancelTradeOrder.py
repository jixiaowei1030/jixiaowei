import json
import time

from attrdict import AttrDict

from cases.TRADE.enums import StatusCode, OrderError, OrderStatus
from utils.tools.base_test_case import BaseTestCase


class TestCancelTradeOrder(BaseTestCase):
    """
    取消订单(父单)
    """

    def test_not_exist_order_id(self, rpc_client, setupdata, random_qimiao_order_id):
        """
        父单号不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = random_qimiao_order_id
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.OrderNotExist.value, resp.resultMsg)

    def test_empty_order_id(self, rpc_client, setupdata):
        """
        父单号为空
        """
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.OrderNotExist.value, resp.resultMsg)

    def test_payed_order_id(self, rpc_client, setupdata, payed_parent_qimiao_order_id):
        """
        订单状态为已支付
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = payed_parent_qimiao_order_id
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.OnlyCancelToBePayedOrder.value, resp.resultMsg)

    def test_empty_cancel_time(self, rpc_client, setupdata, exist_parent_qimiao_order_id):
        """
        取消时间为空(0)
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.EmptyCancelTime.value, resp.resultMsg)

    def test_cancel_time_less_zero(self, rpc_client, setupdata, exist_parent_qimiao_order_id):
        """
        取消时间小于0
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        setupdata["payload"]["params"]["params"]["req"]["cancelTime"] = -1
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.EmptyCancelTime.value, resp.resultMsg)

    def test_optional_source(self, rpc_client, setupdata, exist_parent_qimiao_order_id, random_string, now_time, db_client):
        """
        可选入参source
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        setupdata["payload"]["params"]["params"]["req"]["cancelTime"] = now_time
        setupdata["payload"]["params"]["params"]["req"]["source"] = random_string
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])
        time.sleep(5)
        sq1 = f"select order_status from xmkp_trade_order.sub_trade_order where parent_order_id = {exist_parent_qimiao_order_id}"
        sq2 = f"select order_status from xmkp_trade_order.trade_order where order_id = {exist_parent_qimiao_order_id}"
        self.assert_equal(OrderStatus.CANCEL.value, db_client.query(sq1).order_status)  # db内检查写入是否成功
        self.assert_equal(OrderStatus.CANCEL.value, db_client.query(sq2).order_status)  # db内检查写入是否成功

    def test_optional_cancel_reason(self, rpc_client, setupdata, exist_parent_qimiao_order_id, random_string, now_time, db_client):
        """
        可选入参cancelReason
        """
        setupdata["payload"]["params"]["params"]["req"]["orderId"] = exist_parent_qimiao_order_id
        setupdata["payload"]["params"]["params"]["req"]["cancelTime"] = now_time
        setupdata["payload"]["params"]["params"]["req"]["cancelReason"] = random_string
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(StatusCode.OK.value, resp["resultCode"])
        time.sleep(5)
        sq1 = f"select order_status from xmkp_trade_order.sub_trade_order where parent_order_id = {exist_parent_qimiao_order_id}"
        sq2 = f"select order_status from xmkp_trade_order.trade_order where order_id = {exist_parent_qimiao_order_id}"
        self.assert_equal(OrderStatus.CANCEL.value, db_client.query(sq1).order_status)  # db内检查写入是否成功
        self.assert_equal(OrderStatus.CANCEL.value, db_client.query(sq2).order_status)  # db内检查写入是否成功
