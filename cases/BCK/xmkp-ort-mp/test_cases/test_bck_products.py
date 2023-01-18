"""
@author:wangqi
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck

class TestProducts(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.m = HttpClientBck()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        pass

    def test_products(self,setupdata):
        """
        desc:获取bck首页信息
        steps：
        1、获取牛津树首页接口，获得返回json
        2、验证products的totalPage是否为空
        3、验证products的businessType是否等于1
        """
        products_info=self.m.bck_products(setupdata.mobile,setupdata.password)
        self.assert_not_null(products_info["totalPage"],error_msg="totalPage是空的")
        self.assert_equal("1",products_info["data"][0]["businessType"], error_msg="不一致")
