"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestClassIsAvailable(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_class_is_available_YES(self, data,setupdata):
        """
        desc:验证班级220是否可用
        steps:
        1、调接口后获得返回值
        2、验证返回中是否为YES
        """
        class_is_available = self.ops.class_is_available_YES(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal((class_is_available), "YES")

    def test_class_is_available_NO(self, data,setupdata):
        """
        desc:验证班级0是否可用
        steps:
        1、调接口后获得返回值
        2、验证返回中是否为NO
        """
        class_is_available = self.ops.class_is_available_NO(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal((class_is_available), "NO")
