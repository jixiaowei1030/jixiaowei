"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestSalaryDropdownList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_salary_dropdown_list_experience(self, data,setupdata):
        """
        desc:验证接口返回获取体验营薪资统计表的渠道名list
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        salary_dropdown_list = self.ops.salary_dropdown_list(data.timeStamp, data.campus, data.dropDownListType, data.teacherId,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 1024")
        self.assert_equal((salary_dropdown_list["data"][0]), "站内1级")


    def test_salary_dropdown_list_month(self, data,setupdata):
        """
        desc:验证接口获取月课薪资统计表的渠道名list
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        salary_dropdown_list = self.ops.salary_dropdown_list(data.timeStamp, data.campus, data.dropDownListType, data.teacherId,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 1352")
        self.assert_equal((salary_dropdown_list["data"][0]), "首购")

    def test_salary_dropdown_list_long(self, data,setupdata):
        """
        desc:验证接口获取长期组薪资统计表的渠道名list
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        salary_dropdown_list = self.ops.salary_dropdown_list(data.timeStamp, data.campus, data.dropDownListType,
                                                             data.teacherId,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_middle.EDU_SALARY set create_date =now() WHERE id = 2001")
        self.assert_equal((salary_dropdown_list["data"][0]), "0元体验营")