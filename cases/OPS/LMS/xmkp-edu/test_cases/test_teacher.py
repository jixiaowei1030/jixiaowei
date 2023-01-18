"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestTeacherList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_teacher_id_list(self, data,setupdata):
        """
        desc:查询老师1109详情信息字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        teacher_id_list = self.ops.teacher_id_list(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_teacher_id = self.mysql.query(
            "SELECT *FROM xmkp_edu.EDU_TEACHER WHERE id=1109", True)
        self.assert_equal(str(edu_teacher_id[0]["teacher_realname"]),
                              teacher_id_list.data["teacherRealname"])
        self.assert_equal(edu_teacher_id[0]["id"],
                              teacher_id_list.data["id"])
        self.assert_equal(edu_teacher_id[0]["teacher_nickname"],
                              teacher_id_list.data["teacherNickname"])


