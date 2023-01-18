"""
@author:liuzhiyang
"""
import allure

from utils.tools.base_test_case import BaseTestCase

@allure.epic("L3")
class TestLessonQuarterList(BaseTestCase):

    def test_lesson_quarter_list(self,math_client,setupdata):
        """L3全部课程"""
        quarter_list_info=math_client[0].quarter_list(setupdata.mobile,setupdata.password)
        quarter_list=math_client[1].query(
            'select * from goodxs.annual_lesson_quarter limit 4',fetch_all=True)
        for i in range(len(quarter_list)):
            with allure.step(f'第{i}季度信息校验'):
                pass
            self.assert_equal(quarter_list[i].name,quarter_list_info.data.quarterList[i].name)
            self.assert_equal(quarter_list[i].count,quarter_list_info.data.quarterList[i].count)
            self.assert_equal(quarter_list[i].type,quarter_list_info.data.quarterList[i].type)
