import json

from cases.TRADE.constant import SF
from utils.tools.base_test_case import BaseTestCase


class TestGetLogisticsTrace(BaseTestCase):
    """
    获取物流轨迹
    """

    def test_empty_transport_note(self, rpc_client, setupdata):
        """
        logisticNoteId为空
        """
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_empty_transport_company(self, rpc_client, setupdata, exist_transport_company_and_transport_note):
        """
        logisticsCompany为空
        """
        setupdata["payload"]["params"]["params"]["logisticNoteId"] = exist_transport_company_and_transport_note.transport_note
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_transport_company_not_match_transport_note(self, rpc_client, setupdata, exist_transport_company_and_transport_note):
        """
        logisticNoteId和logisticsCompany不匹配
        """
        setupdata["payload"]["params"]["params"]["logisticNoteId"] = exist_transport_company_and_transport_note.transport_note
        setupdata["payload"]["params"]["params"]["logisticsCompany"] = SF
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        self.assert_equal(resp, [])

    def test_normal_request(self, rpc_client, setupdata, exist_transport_company_and_transport_note, db_client):
        """
        正常请求
        """
        setupdata["payload"]["params"]["params"]["logisticsCompany"] = exist_transport_company_and_transport_note.transport_company
        setupdata["payload"]["params"]["params"]["logisticNoteId"] = exist_transport_company_and_transport_note.transport_note
        resp = json.loads(rpc_client.invoke_rpc(setupdata.payload).content)
        sq = f"select count(1) as length from xmkp_logistics.TRANSPORT_TRACE where transport_note = {exist_transport_company_and_transport_note.transport_note}"
        self.assert_equal(len(resp), db_client.query(sq).length)
