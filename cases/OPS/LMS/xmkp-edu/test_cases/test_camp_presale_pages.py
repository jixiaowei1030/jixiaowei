"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
import time,datetime
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestPresalePagesList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass
    #此接口增长更改维护
    # def test_presale_pages_list_one(self, data,setupdata):
    #     """
    #     desc:获取campID=21下面新售前页列表
    #     steps:
    #       1.查接口返回列表
    #       2.查数据库campID=21的 数据
    #       3.列表返回ID与数据库ID字段对比
    #       4.列表返回title与数据库title字段对比
    #
    #     """
    #     presale_pages_list = self.ops.camp_presale_pages_one(time.time(), data.currentPage, data.pageSize,setupdata.mobile ,setupdata.password)
    #     edu_presale_pages_page = self.mysql.query("SELECT * FROM xmkp_edu.EDU_NEW_PRESALE_PAGE WHERE camp_ref = '21' and is_deleted='0'",
    #                                               True)
    #     for i in range(0, len(presale_pages_list.data.data)):
    #         self.assert_equal(edu_presale_pages_page[i]["id"], presale_pages_list.data.data[i]["id"])
    #         self.assert_equal(edu_presale_pages_page[i]["title"], presale_pages_list.data.data[i]["title"])

    def test_presale_pages_list_two(self, data,setupdata):
        """
        desc:获取campID=0（不存在的campID）下面新售前页列表
        steps:
          1.查接口campID=0（不存在的campID）的 数据
          2.验证data为null


        """
        presale_pages_list = self.ops.camp_presale_pages_two(time.time(), data.currentPage, data.pageSize,setupdata.mobile ,setupdata.password)
        self.assert_equal( presale_pages_list.data.data,[])

