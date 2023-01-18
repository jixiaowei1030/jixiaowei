"""
@author:liuzhiyang
"""
import datetime

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestMathAddBabydocument(BaseTestCase):

    def test_math_add_babydocument(self,math_client,data,setupdata):
        """L3添加宝贝信息"""
        birthday=datetime.datetime.now().date().__str__()
        baby_info=math_client[0].add_baby_document(birthday,data.sex,data.name,setupdata.mobile,setupdata.password)
        print(baby_info)
        self.assert_equal(0,baby_info.code)
        self.assert_equal('成功',baby_info.msg)
        query=f"select * from goodxs.baby_info where sex='{data.sex}' and name='{data.name}' and birthday='{birthday} 00:00:00'"
        baby_data=math_client[1].query(query)
        self.assert_in('id',baby_data)