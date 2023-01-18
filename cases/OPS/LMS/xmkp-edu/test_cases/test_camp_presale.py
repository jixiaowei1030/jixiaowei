"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestPresaleList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_presale_list(self, data,setupdata):
        """
        desc:验证练营ID=21下的售前页列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        presale_list = self.ops.camp_presale(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_presale_page = self.mysql.query("SELECT * FROM xmkp_edu.EDU_PRESALE_PAGE WHERE camp_ref = '35'", True)
        for i in range(0, len(presale_list)):
            self.assert_equal(edu_presale_page[i]["id"], presale_list[i]["id"])
            self.assert_equal(edu_presale_page[i]["title"], presale_list[i]["title"])


