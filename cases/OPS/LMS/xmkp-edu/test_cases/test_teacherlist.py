"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestTeachersList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_teachers_list(self, data,setupdata):
        """
        desc:查询老师信息列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        teacher_list = self.ops.teacher_list(data.timeStamp, data.pageSize, data.page,setupdata.mobile ,setupdata.password)
        edu_teacher = self.mysql.query(
            "SELECT *FROM xmkp_edu.EDU_TEACHER WHERE is_deleted=0", True)
        for i in range(0, len(teacher_list["entitiesList"])):
            self.assert_equal((edu_teacher[i]["teacher_realname"]),
                              teacher_list["entitiesList"][i]["teacherRealname"])
            self.assert_equal(edu_teacher[i]["id"],
                              teacher_list["entitiesList"][i]["id"])
            self.assert_equal(edu_teacher[i]["teacher_nickname"],
                             teacher_list["entitiesList"][i]["teacherNickname"])
            self.assert_equal(edu_teacher[i]["teacher_name"],
                             teacher_list["entitiesList"][i]["teacherName"])

