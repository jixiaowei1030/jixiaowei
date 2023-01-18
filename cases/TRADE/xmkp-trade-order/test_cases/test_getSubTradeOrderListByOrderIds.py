import json

from cases.TRADE.enums import StatusCode, OrderError
from utils.tools.base_test_case import BaseTestCase
from attrdict import AttrDict


class TestGetSubTradeOrderListByOrderIds(BaseTestCase):
    """
    通过子单号列表查询子单详情
    """

    def test_all_not_exist_order_id(self, rpc_client, setupdata, random_qimiao_order_id):
        """
        列表中的子单号都不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"].append(random_qimiao_order_id)
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.SystemError.value, resp.resultCode)
        self.assert_equal(OrderError.OrderNotExist.value, resp.resultMsg)

    def test_empty_order_id_list(self, rpc_client, setupdata):
        """
         列表为空列表
        """
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.OK.value, resp.resultCode)

    def test_error_type_order_id_list(self, rpc_client, setupdata, exist_qimiao_order_id):
        """
        错误类型的orderIdList入参
        """
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"] = exist_qimiao_order_id
        try:
            json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        except Exception:
            self.assert_equal(StatusCode.SystemError.value, StatusCode.SystemError.value)

    def test_part_not_exist_order_id(self, rpc_client, setupdata, exist_qimiao_order_id, random_qimiao_order_id):
        """
        子单号部分存在部分不存在
        """
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"].append(exist_qimiao_order_id)
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"].append(random_qimiao_order_id)
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.OK.value, resp.resultCode)
        self.assert_equal(len(resp["data"]), 1)

    def test_repeat_exist_order_id(self, rpc_client, setupdata, exist_qimiao_order_id):
        """
        重复的且存在的子单号
        """
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"].append(exist_qimiao_order_id)
        setupdata["payload"]["params"]["params"]["req"]["orderIdList"].append(exist_qimiao_order_id)
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.OK.value, resp.resultCode)
        self.assert_equal(len(resp.data), 1)

    def test_optional_source(self, rpc_client, setupdata, random_string):
        """
        可选入参source
        """
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.OK.value, resp.resultCode)
        setupdata["payload"]["params"]["params"]["req"]["source"] = random_string
        resp = AttrDict(json.loads(rpc_client.invoke_rpc(setupdata.payload).content))
        self.assert_equal(StatusCode.OK.value, resp.resultCode)
