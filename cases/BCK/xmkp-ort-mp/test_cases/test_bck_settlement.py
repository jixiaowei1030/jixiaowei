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

    def test_data_settlement(self, data,setupdata):

        """
        desc:星星结算
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """
        star = self.bck.daka_settlement(data.campRef,setupdata.mobile,setupdata.password)
        print(star)
        starResp = self.mysql.query("SELECT * FROM xmkp_oxford_english.LATEST_STAR WHERE uid = '344746' AND lesson_ref = '248'", True)
        self.assert_equal(starResp[0]["lesson_ref"], star.lessonId, "课程id")
        self.assert_equal(starResp[0]['star'], star.star, "星星数")
