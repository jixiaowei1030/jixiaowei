"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L3")
class TestNewStudy(BaseTestCase):
    """
            desc:验证亲讲课的查询
            steps:
            1、查询获取亲讲课的接口,获得返回json
            2、接口断言：2.1返回code为0，
                       2.2msg为成功，
                       2.3页面展示记录2条

            """
    @allure.title("{data.case_name}")
    def test_math_new_study(self,math_client,data,setupdata):
        '''
        L3亲讲课
        '''
        # 第一步：调用接口，获取返回结果
        new_study=math_client[0].new_study(setupdata.mobile,setupdata.password)
        # 第二步：断言
        self.assert_equal(0,new_study.code,"接口调用失败")
        self.assert_equal("成功",new_study.msg)
        self.assert_equal(2,len(new_study.data.myStudy.myStudy))


