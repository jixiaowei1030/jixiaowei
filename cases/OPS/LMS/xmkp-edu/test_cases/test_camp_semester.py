"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestSemesterList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_semester_list(self, data,setupdata):
        """
        desc:验证训练营ID=21下的学期列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        semester_list = self.ops.camp_semester(data.timeStamp, data.index, data.size, data.campId,setupdata.mobile ,setupdata.password)
        edu_semester = self.mysql.query(
            "select * from xmkp_edu.EDU_SEMESTER where camp_ref = '21' ORDER BY id DESC", True)
        for i in range(0, len(semester_list["ortClassRetentionInfoList"])):
            self.assert_equal(str(edu_semester[i]["sku_ref"]),
                              semester_list["ortClassRetentionInfoList"][i]["skuRef"])
            self.assert_equal(edu_semester[i]["id"],
                              semester_list["ortClassRetentionInfoList"][i]["id"])
            self.assert_equal(edu_semester[i]["semester_no"],
                              semester_list["ortClassRetentionInfoList"][i]["semesterNo"])
            self.assert_equal(str(edu_semester[i]["sale_start_time"]),
                              semester_list["ortClassRetentionInfoList"][i]["saleStartTime"])
            self.assert_equal(str(edu_semester[i]["sale_end_time"]),
                              semester_list["ortClassRetentionInfoList"][i]["saleEndTime"])
            self.assert_equal(edu_semester[i]["sale_num_limit"],
                              semester_list["ortClassRetentionInfoList"][i]["saleLimitNum"])
            # sale_num = self.mysql.query(
            #     "SELECT count(*) num from xmkp_edu.EDU_CLASSMATE WHERE semester_ref = {}".format(semester_list["ortClassRetentionInfoList"][i]["id"]))
            # self.assert_equal(sale_num["num"], semester_list["ortClassRetentionInfoList"][i]["saleNum"])
            #

