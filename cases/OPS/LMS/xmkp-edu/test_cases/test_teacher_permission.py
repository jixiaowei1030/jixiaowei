"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestTeacherPermission(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_teacher_permission(self, data,setupdata):
        """
        desc:验证leslie的ops权限
        steps:
        1、调接口后获得str类型的返回值
        2、断言验证权限是否为SUPER_ADMIN
        """
        permission = self.ops.teacher_permission(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal(permission, "SUPER_ADMIN")
