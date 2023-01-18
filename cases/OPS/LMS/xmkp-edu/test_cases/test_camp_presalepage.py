"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
import time,datetime
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestPresaleInfo(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_presalepage_one(self, data,setupdata):
        """
        desc:获取新售前页为384的详情
        steps:
          1.查接口新售前页为384详情返回列表
          2.查数据库的新售前页为384 数据
          3.列表返回ID与数据库ID字段对比
          4.列表返回title与数据库title字段对比

        """
        presalepage = self.ops.camp_presalepage_one(data.timeStamp,setupdata.mobile ,setupdata.password)

        edu_presalepages = self.mysql.query("SELECT * FROM xmkp_edu.EDU_NEW_PRESALE_PAGE WHERE  id =384  ",True)
        self.assert_equal(edu_presalepages[0]["id"],presalepage.data["id"])
        self.assert_equal(edu_presalepages[0]["title"],presalepage.data["title"])

    def test_presalepage_two(self, data,setupdata):
        """
        desc:获取新售前页为不存在的详情
        steps:
          1.查接口新售前页为不存在的详情返回列表
          2.验证data为null

        """
        presalepage = self.ops.camp_presalepage_two(data.timeStamp,setupdata.mobile ,setupdata.password)

        self.assert_equal(presalepage["data"], None)