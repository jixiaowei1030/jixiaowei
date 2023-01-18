"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time




@allure.epic("L3")
class TestMathInformation(BaseTestCase):
    """
                desc:验证专项训练的查询
                steps:
                1、查询获取亲讲课的接口,获得返回json
                2、接口断言：2.1返回code为0，
                           2.2msg为成功，
                           2.3页面展示模块数量

                """


    @allure.title("{data.case_name}")
    def test_math_getinformation(self,math_client,data,setupdata):
        """L3专项训练"""
        # 第一步：调用接口，获取返回结果
        get_information=math_client[0].get_information(data.specialType,setupdata.mobile,setupdata.password)
        time.sleep(0.5)
        # 第二步：断言
        self.assert_equal(0,get_information.code)
        self.assert_equal("成功",get_information.msg)
        self.assert_equal(data.count,get_information.data.count)


