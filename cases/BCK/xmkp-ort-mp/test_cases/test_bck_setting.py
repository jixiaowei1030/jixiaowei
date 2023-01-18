"""
@author:wangqi
"""

from utils.common import get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck

class TestSetting(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.m = HttpClientBck()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        pass

    def test_setting_one(self,setupdata):
        setting_info = self.m.bck_setting(setupdata.mobile,setupdata.password)
        return setting_info
        self.assert_equal("false", setting_info["data"][0]["isForceRead"], error_msg="isForceRead不一致")

    def test_setting_two(self,setupdata):
        setting_info = self.m.bck_setting(setupdata.mobile,setupdata.password)
        return setting_info
        self.assert_equal("1", setting_info["data"][0]["analysisType"], error_msg="analysisType不一致")

    def test_setting_three(self,setupdata):
        setting_info = self.m.bck_setting(setupdata.mobile,setupdata.password)
        return  setting_info
        self.assert_not_null(setting_info["isForceRead"],error_msg="isForceRead为空")
    def test_setting_four(self,setupdata):
        setting_info = self.m.bck_setting(setupdata.mobile,setupdata.password)
        return setting_info
        self.assert_not_null(setting_info["analysisType"],error_msg="analysisType")