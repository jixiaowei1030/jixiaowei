"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L1")
class TestMathQuerylessonPracticelist(BaseTestCase):
    """
                desc:验证课程练习列表的查询
                steps:
                1、查询获取课程练习列表的接口,获得返回json
                2、接口断言：2.1返回code为0，
                           2.2msg为success，
                           2.3页面展示记录4条

                """

    @allure.title('{data.case_name}')
    def test_math_querylesson_practicelist(self,math_client,setupdata,data):
        """L1课程练习列表"""
        # 第一步：调用接口，获取返回结果
        lesson_practicelist=math_client[0].lesson_practicelist(data.albumId,data.lessonId,setupdata.mobile,setupdata.password)
        print(lesson_practicelist)
        # 第二步：断言
        self.assert_equal(0,lesson_practicelist.code)
        self.assert_equal("success",lesson_practicelist.message)
        self.assert_equal(4,len(lesson_practicelist.data.lessonStepDTO.stepList))
