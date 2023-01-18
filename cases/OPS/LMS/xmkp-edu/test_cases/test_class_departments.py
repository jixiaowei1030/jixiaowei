"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestClassDepartmentsList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_departments_list(self, data,setupdata):
        """
        desc:验证部门信息列表
        steps:
        1、调接口后获得返回json
        2、验证返回中是否包含(110, 测试1组)
        """
        departments_list = self.ops.class_departments(data.timeStamp,setupdata.mobile ,setupdata.password)
        for i in range(0, len(departments_list)):
            if departments_list[i]["id"] == 110:
                self.assert_equal(departments_list[i]["name"], "测试1组")
