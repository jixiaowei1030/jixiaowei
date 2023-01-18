"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import  get_mysql
from utils.log import LOGGER


class TestMProduct(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        LOGGER.info("TestMProduct测试结束")

    def test_m_product(self,setupdata):

        """
        desc:获取chinastory课程配置信息
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """
        product = self.bck.m_product(setupdata.mobile,setupdata.password)
        #self.assert_equal(0,res["code"])
        #self.assert_equal(173,res["data"]["id"])
        productinfo =self.mysql.query("SELECT * FROM xmkp_edu.EDU_PRODUCT WHERE business_type='5'", True)
        self.assert_equal(productinfo[0]["id"], product.data.id, "产品id")
        self.assert_equal(productinfo[0]["product_title"], product.data.productTitle, "产品标题")
        self.assert_equal(productinfo[0]["description"], product.data.description, "产品描述")
        self.assert_equal(productinfo[0]["business_type"], product.data.businessType, "产品类型")