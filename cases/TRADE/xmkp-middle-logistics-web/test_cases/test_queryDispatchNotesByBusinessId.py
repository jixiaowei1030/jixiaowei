import json

from cases.TRADE.constant import ONE_HUNDRED
from utils.tools.base_test_case import BaseTestCase


class TestQueryDispatchNotesByBusinessId(BaseTestCase):
    """
    通过订单查询发货单
    """

    def test_empty_business_id(self, rpc_client, setupdata):
        """
        businessId为空
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_not_exist_business_id(self, rpc_client, setupdata, random_string):
        """
        businessId不存在
        """
        setupdata["payload"]["params"]["params"]["businessId"] = random_string
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_empty_business_type(self, rpc_client, setupdata, exist_business_id_and_type):
        """
        businessType为空(0)
        """
        setupdata["payload"]["params"]["params"]["businessId"] = exist_business_id_and_type.business_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_business_id_not_match_business_type(self, rpc_client, setupdata, exist_business_id_and_type):
        """
        businessId和businessType不匹配
        """
        setupdata["payload"]["params"]["params"]["businessId"] = exist_business_id_and_type.business_id
        setupdata["payload"]["params"]["params"]["businessType"] = ONE_HUNDRED
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_normal_request(self, rpc_client, setupdata, exist_business_id_and_type, db_client):
        """
        正常请求
        """
        setupdata["payload"]["params"]["params"]["businessId"] = exist_business_id_and_type.business_id
        setupdata["payload"]["params"]["params"]["businessType"] = exist_business_id_and_type.business_type
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        sq = f"select count(1) as length from xmkp_logistics.DISPATCH_NOTE where business_id = '{exist_business_id_and_type.business_id}'"
        self.assert_equal(len(resp), db_client.query(sq).length)
