"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckNoReadRecord(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")


    def teardown_class(cls):
        LOGGER.info("TestBckNoReadRecord测试结束")

    def test_bck_noRead_record1(self, data,setupdata):
        """
        desc: 非单词跟读钻石结算-3颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_noRead_record(data.lessonRef, data.stepRef, data.campRef, data.productRef,
                                            data.homeworkRef, data.tryTimes, data.homeworkType,setupdata.mobile,setupdata.password)
        self.assert_equal(3, record["diamond"], "钻石数为3")
        self.assert_equal("excellent", record["comment"], "钻石评价为excellent")

    def test_bck_noRead_record2(self, data,setupdata):
        """
        desc: 非单词跟读钻石结算-2颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_noRead_record(data.lessonRef, data.stepRef, data.campRef, data.productRef,
                                            data.homeworkRef, data.tryTimes, data.homeworkType,setupdata.mobile,setupdata.password)
        self.assert_equal(2, record["diamond"], "钻石数为2")
        self.assert_equal("awesome", record["comment"], "钻石评价为awesome")

    def test_bck_noRead_record3(self, data,setupdata):
        """
        desc: 非单词跟读钻石结算-1颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_noRead_record(data.lessonRef, data.stepRef, data.campRef, data.productRef,
                                            data.homeworkRef, data.tryTimes, data.homeworkType,setupdata.mobile,setupdata.password)
        self.assert_equal(1, record["diamond"], "钻石数为3")
        self.assert_equal("goodJob", record["comment"], "钻石评价为goodJob")