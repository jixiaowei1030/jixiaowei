"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestQueryClassInfo(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_query_class_is_exist(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后获得返回json
        2、验证返回中是否为1093的数据
        """
        user_study_list = self.ops.query_class_info_is_exist(setupdata.mobile ,setupdata.password)
        self.assert_equal((user_study_list["id"]), 1093)

    def test_query_class_is_not_exist(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后获得返回json
        2、验证返回中是否为00000的数据
        """
        user_study_list = self.ops.query_class_info_is_not_exist(setupdata.mobile ,setupdata.password)
        self.assert_equal((user_study_list["id"]), None)