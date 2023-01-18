"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestUserStudy(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_user_study_list(self, data,setupdata):
        """
        desc:验证接口返回的学员学习数据
        steps:
        1、调接口后获得返回json
        2、验证返回中是否为307923的学习数据
        """
        user_study_list = self.ops.user_study(data.timeStamp, data.userId, data.classRef,setupdata.mobile ,setupdata.password)
        for i in range(0, len(user_study_list)):
            self.assert_equal((user_study_list[i]["userId"]), 307923)
