"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestUserDetailInfo(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_user_detail_info(self, data,setupdata):
        """
        desc:验证接口返回的学员详细信息
        steps:
        1、调接口后获得返回json
        2、验证返回中是否为307923的详细信息
        """
        user_detail_info = self.ops.user_detail_info(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal((user_detail_info["userId"]), 307923)
        self.assert_equal((user_detail_info["classId"]), 89)
