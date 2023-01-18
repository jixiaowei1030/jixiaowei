import json

from cases.TRADE.constant import ONE_HUNDRED
from utils.tools.base_test_case import BaseTestCase


class TestQueryDispatchNotesByUid(BaseTestCase):
    """
    通过UID查询发货单
    """

    def test_empty_id(self, rpc_client, setupdata):
        """
        uid为空(0)
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_not_exist_uid(self, rpc_client, setupdata, random_uid):
        """
        uid不存在
        """
        setupdata["payload"]["params"]["params"]["uid"] = random_uid
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_empty_business_type(self, rpc_client, setupdata, exist_uid_and_type):
        """
        businessType为空(0)
        """
        setupdata["payload"]["params"]["params"]["uid"] = exist_uid_and_type.user_id
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_uid_not_match_business_type(self, rpc_client, setupdata, exist_uid_and_type):
        """
        uid和businessType不匹配
        """
        setupdata["payload"]["params"]["params"]["uid"] = exist_uid_and_type.user_id
        setupdata["payload"]["params"]["params"]["businessType"] = ONE_HUNDRED
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_normal_request(self, rpc_client, setupdata, exist_uid_and_type, db_client):
        """
        正常请求
        """
        setupdata["payload"]["params"]["params"]["uid"] = exist_uid_and_type.user_id
        setupdata["payload"]["params"]["params"]["businessType"] = exist_uid_and_type.business_type
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        sq = f"select count(1) as length from xmkp_logistics.DISPATCH_NOTE where user_id = {exist_uid_and_type.user_id}"
        self.assert_equal(len(resp), db_client.query(sq).length)
