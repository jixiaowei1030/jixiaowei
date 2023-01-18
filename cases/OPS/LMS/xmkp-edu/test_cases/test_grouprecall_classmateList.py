"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestGroupRecallClassMateList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_grouprecall_Classmate_list(self, data,setupdata):
        """
        desc:查询用户找回列表
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        grouprecall_Classmate_list = self.ops.grouprecall_Classmate_list(data.timeStamp, data.pageSize, data.page, "",setupdata.mobile ,setupdata.password)
        edu_grouprecall_Classmate = self.mysql.query(
            "select *from xmkp_edu.EDU_GROUP_CODE_RECALL where semester_id =860"
            " and teacher_id in (188888887,1,15284,233333331,17403,17191,11154,11412,"
            "199999998,255555553,244444442,266666664,211111109,55555555,17421,66666666,"
            "88888888,20095,99999999,133333332,111111110,144444443,11027,140319360,19162,"
            "11029,7773,20149) and is_deleted =0 order by class_id desc  ,id desc ", True)
        for i in range(0, len(grouprecall_Classmate_list.data.list)):
            self.assert_equal((edu_grouprecall_Classmate[i]["uid"]),
                             grouprecall_Classmate_list.data.list[i]["studentId"])
            self.assert_equal(edu_grouprecall_Classmate[i]["class_id"],
                              grouprecall_Classmate_list.data.list[i]["classId"])
            self.assert_equal(edu_grouprecall_Classmate[i]["teacher_id"],
                              grouprecall_Classmate_list.data.list[i]["teacherId"])
            self.assert_equal(edu_grouprecall_Classmate[i]["status"],
                              grouprecall_Classmate_list.data.list[i]["status"])

    # def test_grouprecall_Classmate_list_status(self, data,setupdata):
    #     """
    #     desc:查询用户找回列表
    #     steps:
    #     1、调接口后获得返回json
    #     2、查数据库获得查询数据
    #     3、断言1 2的值是否一致
    #     """
    #     grouprecall_Classmate_list = self.ops.grouprecall_Classmate_list(data.timeStamp, data.pageSize, data.page, data.status,setupdata.mobile ,setupdata.password)
    #     if grouprecall_Classmate_list.data.list[0]["status"] == 2:
    #         for i in range(0, len(grouprecall_Classmate_list.data.list)):
    #          self.assert_equal(grouprecall_Classmate_list.data.list[0]["studentId"],797823)
    #         self.assert_equal(grouprecall_Classmate_list.data.list[0]["classId"],70048)
    #         self.assert_equal(grouprecall_Classmate_list.data.list[0]["teacherId"],2)



