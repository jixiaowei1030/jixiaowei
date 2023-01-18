"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckAnalysisRecord(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")


    def teardown_class(cls):
        LOGGER.info("TestBckAnalysisRecord测试结束")

    def test_bck_analysis_record(self, data,setupdata):
        """
        desc: 视频钻石结算
        step1:请求接口拿到返回信息
        """
        print(data)
        record = self.bck.bck_analysis_record(data.lessonRef, data.stepRef, data.campRef, data.analysisRef,setupdata.mobile,setupdata.password)
        self.assert_equal(3, record["diamond"], "钻石数为3")
        self.assert_equal("excellent", record["comment"], "钻石评价为excellent")
        # print(record)









