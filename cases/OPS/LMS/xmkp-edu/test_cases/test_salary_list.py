"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestSalaryList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_salary_list_experience(self, data,setupdata):
        """
        desc:验证接口返回获取体验营薪资统计表
        steps:
        1、调接口后获得返回json
        2、查询数据库返回数据
        3、断言接口返回的数据与数据库一致
        """
        salary_list = self.ops.salary_list(data.timeStamp, data.pageSize, data.page, data.teacherId, data.campus,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 1024")
        edu_salary_list =self.mysql.query(
            "select * from xmkp_middle.EDU_SALARY  WHERE id = 1024")

        for i in range(0, len(salary_list.data.list)):
            self.assert_equal((edu_salary_list["id"]), salary_list.data.list[i]["id"])
            self.assert_equal(edu_salary_list["album_level"], salary_list.data.list[i]["albumLevel"])
            self.assert_equal(edu_salary_list["class_id"], salary_list.data.list[i]["classId"])

    def test_salary_list_month(self, data,setupdata):
        """
        desc:验证接口返回获取月课薪资统计表
        steps:
        1、调接口后获得返回json
        2、查询数据库返回数据
        3、断言接口返回的数据与数据库一致
        """
        salary_list = self.ops.salary_list(data.timeStamp, data.pageSize, data.page, data.teacherId, data.campus,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 1352")
        edu_salary_list =self.mysql.query(
            "select * from xmkp_middle.EDU_SALARY  WHERE id = 1352")

        for i in range(0, len(salary_list.data.list)):
            self.assert_equal((edu_salary_list["id"]), salary_list.data.list[i]["id"])
            self.assert_equal(edu_salary_list["album_level"], salary_list.data.list[i]["albumLevel"])
            self.assert_equal(edu_salary_list["class_id"], salary_list.data.list[i]["classId"])

    def test_salary_list_long(self, data,setupdata):
        """
        desc:验证接口返回获取长期组薪资统计表
        steps:
        1、调接口后获得返回json
        2、查询数据库返回数据
        3、断言接口返回的数据与数据库一致
        """
        salary_list = self.ops.salary_list(data.timeStamp, data.pageSize, data.page, data.teacherId, data.campus,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 2001")
        edu_salary_list =self.mysql.query(
            "select * from xmkp_middle.EDU_SALARY  WHERE id = 2001")

        for i in range(0, len(salary_list.data.list)):
            self.assert_equal((edu_salary_list["id"]), salary_list.data.list[i]["id"])
            self.assert_equal(edu_salary_list["album_level"], salary_list.data.list[i]["albumLevel"])
            self.assert_equal(edu_salary_list["class_id"], salary_list.data.list[i]["classId"])