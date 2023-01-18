"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckReadBookRecord(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")


    def teardown_class(cls):
        LOGGER.info("TestBckReadBookRecord测试结束")

    def test_bck_readBook_record1(self, data,setupdata):
        """
        desc: 绘本跟读钻石结算-3颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_readBook_record(data.stepRef, data.lessonRef,  data.productRef, data.campRef,
                                              data.tryTimes, data.score, data.audioUrl, data.duration,
                                              data.originAudioUrl, data.dialogRef, data.text,setupdata.mobile,setupdata.password)
        self.assert_equal(3, record["diamond"], "钻石数为3")
        self.assert_equal("excellent", record["comment"], "钻石评价为excellent")
        # print(record)

    def test_bck_readBook_record2(self, data,setupdata):
        """
        desc: 绘本跟读钻石结算-2颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_readBook_record(data.stepRef, data.lessonRef,  data.productRef, data.campRef,
                                              data.tryTimes, data.score, data.audioUrl, data.duration,
                                              data.originAudioUrl, data.dialogRef, data.text,setupdata.mobile,setupdata.password)
        self.assert_equal(2, record["diamond"], "钻石数为2")
        self.assert_equal("awesome", record["comment"], "钻石评价为awesome")
        # print(record)

    def test_bck_readBook_record3(self, data,setupdata):
        """
        desc: 绘本跟读钻石结算-1颗钻石
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_readBook_record(data.stepRef, data.lessonRef,  data.productRef, data.campRef,
                                              data.tryTimes, data.score, data.audioUrl, data.duration,
                                              data.originAudioUrl, data.dialogRef, data.text,setupdata.mobile,setupdata.password)
        self.assert_equal(1, record["diamond"], "钻石数为1")
        self.assert_equal("goodJob", record["comment"], "钻石评价为goodJob")
        # print(record)-

    def test_bck_readBook_record4(self, data,setupdata):
        """
        desc: 绘本跟读钻石结算-0颗钻石-（连续三次未跟读提示try again）
        step1:请求接口拿到返回信息
        """
        # print(data)
        record = self.bck.bck_readBook_record(data.stepRef, data.lessonRef,  data.productRef, data.campRef,
                                              data.tryTimes, data.score, data.audioUrl, data.duration,
                                              data.originAudioUrl, data.dialogRef, data.text,setupdata.mobile,setupdata.password)
        self.assert_equal(0, record["diamond"], "钻石数为0")
        self.assert_equal("bad", record["comment"], "钻石评价为bad")
        # print(record)











