"""
@author:wangqi
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck

class TestBanner(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.m = HttpClientBck()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        pass

    def test_banner_one(self,setupdata):
        """
        desc:获取bck99元banner图
        steps:
        1、获取牛津树banner接口，获得返回jsongir
        2、验证banner的key是否等于99yuan
        """
        banner_info=self.m.bck_banner(setupdata.mobile,setupdata.password)
        print (banner_info)
        self.assert_equal("http://m.test.ximalaya.com/ort/router/invite/notcheck/monthLesson/1131?source=ertongshouqianye"
                          , banner_info[0]["url"], error_msg="99元url不一致")
        self.assert_equal("99yuan",banner_info[0]["key"], error_msg="key不等于99yuan")

    def test_banner_two(self,setupdata):
        """
        desc:获取bck0元banner图
        steps:
        1、获取牛津树banner接口，获得返回json
        2、验证banner的key是否等于0yuan
        """
        banner_info=self.m.bck_banner(setupdata.mobile,setupdata.password)
        print(banner_info)

        self.assert_equal("https://m.test.ximalaya.com/ort/router/invite/notcheck/trialClassActivity/129?fl=0&source=123"
                          , banner_info[1]["url"], error_msg="0元url不一致")
        self.assert_equal("0yuan",banner_info[1]["key"], error_msg="key不等于0yuan")
    def test_banner_three(self,setupdata):
        """
        desc:获取bck的banner图的url
        steps:
        1、获取牛津树banner接口，获得返回json
        2、验证banner的url是否为空
        """
        banner_info=self.m.bck_banner(setupdata.mobile,setupdata.password)
        self.assert_not_null(banner_info[0]["url"], error_msg="url为空")