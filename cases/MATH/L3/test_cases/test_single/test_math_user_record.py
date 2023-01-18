"""
@author:liuzhiyang
"""

from utils.common import get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure


@allure.epic("L3")
class TestMathUserRecord(BaseTestCase):

    def test_data_user_record1(self, data, math_client,setupdata):
        '''
        L3用户学习记录，从首页点击进入学习，请求该接口
        从当前学习页点击学习记录，同样请求该接口
        '''
        annual_info = math_client[0].user_record(data.type,setupdata.mobile,setupdata.password)
        self.assert_equal(0, annual_info.code)
        self.assert_equal('成功', annual_info['msg'])
        self.assert_in('lessonCount',annual_info.data)
        self.assert_in('practiceCount',annual_info.data)