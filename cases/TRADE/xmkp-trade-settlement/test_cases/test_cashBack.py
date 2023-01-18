import random

from cases.TRADE.enums import StatusCode, CashBackError, Common, PayType
from cases.TRADE.utils import resp_to_attrdict
from utils.tools.base_test_case import BaseTestCase


class TestCashBack(BaseTestCase):
    """
    desc: 打卡返现-返现
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
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyReqId.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyReqId.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_businessType(self, rpc_client, setupdata, now_time):
        """
        businessType为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        del setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessType"]
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyBusinessType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyBusinessType.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_businessId(self, rpc_client, setupdata, now_time):
        """
        businessId为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyBusinessId.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyBusinessId.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_amount(self, rpc_client, setupdata, now_time):
        """
        amount为空(返现)
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyAmount.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyCashBackAmount.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_payType(self, rpc_client, setupdata, now_time):
        """
        payType为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        del setupdata["payload"]["params"]["params"]["cachBackRequest"]["payType"]
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyPayType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyPayType.value, resp_to_attrdict(resp).resultMsg)

    def test_wrong_payType(self, rpc_client, setupdata, now_time):
        """
        错误的payType(目前只支持支付宝)
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["payType"] = PayType.XI_DIAN.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.WrongPayType.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.WrongPayType.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_aliIdentityTypeId(self, rpc_client, setupdata, now_time):  # 默认 登录id和name
        """
        aliIdentityTypeId为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        del setupdata["payload"]["params"]["params"]["cachBackRequest"]["aliIdentityTypeId"]
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyALiIdentityTypeId.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyALiIdentityTypeId.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_aliPayAccount(self, rpc_client, setupdata, now_time):  # 默认 登录id和name
        """
        aliPayAccount为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyALiPayAccount.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyALiPayAccount.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_aliPayRealName(self, rpc_client, setupdata, now_time):
        """
        aliPayRealName为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["aliPayAccount"] = 15102100358
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyALiPayRealName.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyALiPayRealName.value, resp_to_attrdict(resp).resultMsg)

    def test_empty_remark(self, rpc_client, setupdata, now_time):
        """
        remark为空
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["aliPayAccount"] = 15102100358
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["realName"] = "施帅钢"
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.EmptyRemark.value, resp_to_attrdict(resp).resultCode)
        self.assert_equal(CashBackError.EmptyRemark.value, resp_to_attrdict(resp).resultMsg)

    def test_cashBack(self, rpc_client, setupdata, now_time):
        """
        正常返现请求
        """
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqSource"] = Common.ReqSource.value
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["reqId"] = now_time
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["businessId"] = f"{Common.ReqSource.value}_{now_time}"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["amount"] = round(random.random(), 2)
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["aliPayAccount"] = 15102100358
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["realName"] = "施帅钢"
        setupdata["payload"]["params"]["params"]["cachBackRequest"]["remark"] = Common.ReqSource.value
        resp = rpc_client.invoke_rpc(setupdata.payload)
        self.assert_equal(StatusCode.OK.value, resp_to_attrdict(resp).resultCode, resp_to_attrdict(resp).resultMsg)
