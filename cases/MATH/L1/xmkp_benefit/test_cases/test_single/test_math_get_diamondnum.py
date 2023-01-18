"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time


@allure.epic("L1")
class TestMathGetDiamondnum(BaseTestCase):
    """
                    desc:验证获取钻石数量的查询
                    steps:
                    1、查询获取课程练习列表的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，

                    """
    @allure.title("{data.case_name}")
    def test_math_get_diamondnum(self,math_client,data,setupdata):
        """L1获取钻石数量"""
        # 第一步：调用接口，获取返回结果
        get_diamondnum=math_client[0].get_diamondnum(data.albumId,data.lessonId,data.practiceId,data.practiceSeq,data.uniqueNo,setupdata.mobile,setupdata.password)
        # 第二步：断言
        self.assert_equal(0,get_diamondnum.code)
        self.assert_equal("success",get_diamondnum.message)




