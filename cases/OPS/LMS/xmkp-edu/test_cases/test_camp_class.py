"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestClassList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_class_list(self, data, setupdata):
        """
        desc:验证学期ID=595下的班级列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        class_list = self.ops.camp_class(data.timeStamp, data.page, data.pageSize, data.sum, "", setupdata.mobile, setupdata.password)
        for i in range(0, len(class_list["ortClassRetentionInfoList"])):
            edu_class = self.mysql.query(
                "SELECT * FROM xmkp_edu.EDU_CLASS WHERE semester_ref = '595' AND id = %s"
                % class_list["ortClassRetentionInfoList"][i]["id"])
            self.assert_equal(edu_class["class_name"], class_list["ortClassRetentionInfoList"][i]["className"])
            self.assert_equal(edu_class["head_teacher"], class_list["ortClassRetentionInfoList"][i]["headTeacher"])
            self.assert_equal(edu_class["student_num_limit"],
                              class_list["ortClassRetentionInfoList"][i]["studentNumLimit"])
    #        student_num = self.mysql.query(
    #            "SELECT count(*) num from xmkp_edu.EDU_CLASSMATE WHERE semester_ref = '595' AND class_ref = %s"
    #            % class_list["ortClassRetentionInfoList"][i]["id"])
    #        self.assert_equal(student_num["num"], class_list["ortClassRetentionInfoList"][i]["studentNum"])


