"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestMProduct(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        LOGGER.info("TestMProduct测试结束")

    def test_bck_coreVocabulary(self,setupdata,):

        """
        desc:获取课程248的核心单词
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """
        coreVocabulary= self.bck.m_coreVocabulary(setupdata.mobile,setupdata.password)
        print(coreVocabulary)
        coreVocabularyResp = self.mysql.query("SELECT * FROM `xmkp_edu`.`EDU_LESSON_CORE_VOCABULARY` WHERE `lesson_ref` = '248'", True)
        self.assert_equal(coreVocabularyResp[0]["vocabulary"], coreVocabulary[0]["vocabulary"], "单词vocabulary英文")
        self.assert_equal(coreVocabularyResp[0]["chinese_interpretation"], coreVocabulary[0]["chineseInterpretation"], "单词vocabulary中文")

