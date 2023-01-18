import random

from cases.TRADE.enums import StatusCode, CashBackError, Common, CardType
from cases.TRADE.utils import resp_to_attrdict
from utils.tools.base_test_case import BaseTestCase


class TestRecharge(BaseTestCase):
    """
    desc: 打卡返现-充值
    """

    def test_empty_reqSource(self, rpc_client, setupdata):
        """
        reqSource为空
        """
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyReqSource.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyReqSource.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_reqId(self, rpc_client, setupdata):
        """
        reqId为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyReqId.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyReqId.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_realName(self, rpc_client, setupdata, now_time):
        """
        realName为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyRealName.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyRealName.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_businessType(self, rpc_client, setupdata, now_time, real_person):
        """
        businessType为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"] = random.choice(real_person)[0]
        del setupdata["payload"]["params"]["params"]["rechargeDto"]["businessType"]
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyBusinessType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyBusinessType.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_businessId(self, rpc_client, setupdata, now_time, real_person):
        """
        businessId为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"] = random.choice(real_person)[0]
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyBusinessId.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyBusinessId.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_cardType(self, rpc_client, setupdata, now_time, real_person):
        """
        cardType为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"] = random.choice(real_person)[0]
        setupdata["payload"]["params"]["params"]["rechargeDto"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        del setupdata["payload"]["params"]["params"]["rechargeDto"]["cardType"]
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyCardType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyCardType.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_cardCode(self, rpc_client, setupdata, now_time, real_person):
        """
        cardCode为空
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"] = random.choice(real_person)[0]
        setupdata["payload"]["params"]["params"]["rechargeDto"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyCardCode.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyCardCode.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_amount(self, rpc_client, setupdata, now_time, real_person):
        """
        amount为空(充值)
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"], setupdata["payload"]["params"]["params"]["rechargeDto"]["cardCode"] = random.choice(real_person)
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyAmount.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyRechargeAmount.value, resp_to_attrdict(resp).resultMsg)

    def test_wrong_cardType(self, rpc_client, setupdata, now_time, real_person):
        """
        错误的cardType,目前只支持二代身份证
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"], setupdata["payload"]["params"]["params"]["rechargeDto"]["cardCode"] = random.choice(real_person)
        setupdata["payload"]["params"]["params"]["rechargeDto"]["amount"] = random.random()
        setupdata["payload"]["params"]["params"]["rechargeDto"]["cardType"] = CardType.PASSPORT.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.WrongCardType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.WrongCardType.value, resp_to_attrdict(resp).resultMsg)

    def test_recharge(self, rpc_client, setupdata, now_time, real_person):
        """
        正常充值请求
        """
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["rechargeDto"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["rechargeDto"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["rechargeDto"]["realName"], setupdata["payload"]["params"]["params"]["rechargeDto"]["cardCode"] = random.choice(real_person)
        setupdata["payload"]["params"]["params"]["rechargeDto"]["amount"] = round(random.random(), 2)  # 2位小数
        setupdata["payload"]["params"]["params"]["rechargeDto"]["cardType"] = CardType.ID_CARD.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.OK.value, resp_to_attrdict(resp).resultCode, resp_to_attrdict(resp).resultMsg)
