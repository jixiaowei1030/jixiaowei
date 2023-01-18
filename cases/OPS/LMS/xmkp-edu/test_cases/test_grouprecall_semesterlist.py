"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestGroupRecallList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_grouprecall_semester_list(self, data,setupdata):
        """
        desc:查询用户找回列表
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        grouprecall_semester_list = self.ops.grouprecall_semester_list(data.timeStamp, data.pageSize, data.page,"",setupdata.mobile ,setupdata.password)
        edu_grouprecall_semester = self.mysql.query(
            "select * from xmkp_edu.EDU_GROUP_CODE_RECALL_SEMESTER order by semester_id desc ", True)
        for i in range(0, len(grouprecall_semester_list.data.list)):
            self.assert_equal((edu_grouprecall_semester[i]["semester_id"]),
                              grouprecall_semester_list.data.list[i]["semesterId"])
            self.assert_equal(edu_grouprecall_semester[i]["camp_id"],
                              grouprecall_semester_list.data.list[i]["campRef"])

    def test_grouprecall_semester_list_ONE(self, data,setupdata):
        """
        desc:查询用户找回列表
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        grouprecall_semester_list = self.ops.grouprecall_semester_list(data.timeStamp, data.pageSize, data.page,data.semesterId,setupdata.mobile ,setupdata.password)
        edu_grouprecall_semester = self.mysql.query(
            "select * from xmkp_edu.EDU_GROUP_CODE_RECALL_SEMESTER where semester_id=2164 ", True)
        for i in range(0, len(grouprecall_semester_list.data.list)):
            if grouprecall_semester_list.data.list[i]["semesterId"] == 2164:
                self.assert_equal((edu_grouprecall_semester[i]["semester_id"]),
                              grouprecall_semester_list.data.list[i]["semesterId"])
                self.assert_equal(edu_grouprecall_semester[i]["camp_id"],
                              grouprecall_semester_list.data.list[i]["campRef"])
                self.assert_equal(grouprecall_semester_list.data.list[i]["campName"],"【购1返9.9】牛津树少儿英语")