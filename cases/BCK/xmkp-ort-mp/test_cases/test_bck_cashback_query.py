
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER
class TestBckCashBackQuery(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck=HttpClientBck()
        cls.mysql=get_mysql()
        cls.setup_data = getattr(cls, "setup_data")
    def teardown_class(cls):
        LOGGER.info("TestBckCashBackQuery测试结束！")

    def test_bck_cashback_query(self,data,setupdata):
        respone_data=self.bck.bck_cashback_query(data.semesterRef,setupdata.mobile,setupdata.password)
        self.assert_equal("3",str(respone_data['cashBackStatus']))
        activity_status = self.mysql.query("SELECT activity_status FROM xmkp_oxford_english.USER_ACTIVITY_STATUS WHERE user_id=344746 and semester_ref = 4229", True)
        status = self.mysql.query("SELECT status FROM xmkp_oxford_english.CASh_BACK_STATEMENT where user_id = 344746",True)
        self.assert_equal(activity_status[0].activity_status,status[0].status,"关联表状态存储正确")
        self.assert_equal(respone_data['cashBackStatus'],3,"接口返回返现状态正确")

