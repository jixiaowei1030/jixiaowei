"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestMemberInClassList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_member_in_class_list(self, data,setupdata):
        """
        desc:验证班级ID=1210下的学员列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        member_in_class_list = self.ops.camp_member_in_class(data.timeStamp, data.index, data.size, "", setupdata.mobile ,setupdata.password)
        edu_classmate = self.mysql.query(
            "SELECT * FROM xmkp_edu.EDU_CLASSMATE WHERE semester_ref = '595' AND class_ref = '1093'", True)
        for i in range(0, len(member_in_class_list["data"]["list"])):
            self.assert_equal(edu_classmate[i]["user_id"], member_in_class_list["data"]["list"][i]["userId"])