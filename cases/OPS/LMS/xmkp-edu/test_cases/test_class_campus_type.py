"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestClassCampusType(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_class_campus_type_tiyanying(self, data,setupdata):
        """
        desc:验证班级所属训练营类型为体验营
        steps:
        1、调接口后获得返回值
        2、验证返回中是否为体验营
        """
        class_type = self.ops.class_campus_type(data.timeStamp, data.classRef,setupdata.mobile ,setupdata.password)
        self.assert_equal(class_type, "体验营")

    def test_class_campus_type_yueke(self, data,setupdata):
        """
        desc:验证班级所属训练营类型为月课
        steps:
        1、调接口后获得返回值
        2、验证返回中是否为月课
        """
        class_type = self.ops.class_campus_type(data.timeStamp, data.classRef,setupdata.mobile ,setupdata.password)
        self.assert_equal(class_type, "月课")

    def test_class_campus_type_changqizu(self, data,setupdata):
        """
        desc:验证班级所属训练营类型为长期组
        steps:
        1、调接口后获得返回值
        2、验证返回中是否为长期组
        """
        class_type = self.ops.class_campus_type(data.timeStamp, data.classRef,setupdata.mobile ,setupdata.password)
        self.assert_equal(class_type, "长期组")
