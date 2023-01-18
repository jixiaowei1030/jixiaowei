from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER
class TestBckCashBackConfirm(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck=HttpClientBck()
        cls.mysql=get_mysql()
        cls.setup_data = getattr(cls, "setup_data")
    def teardown_class(cls):
        LOGGER.info("TestBckCashBackConfirm测试结束！")
    def test_bck_cashback_confirm(self,data,setupdata):
        record=self.bck.bck_cashback_confirm(data.account,data.aliAccountName,data.semesterRef,setupdata.mobile,setupdata.password)
        self.assert_equal(record['confirmStatus'],3,"已经返现成功，再次发起返回系统异常对应code正确")
