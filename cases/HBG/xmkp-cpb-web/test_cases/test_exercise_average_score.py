"""
@Time ： 2021/1/28 22:35
@Auth ： wangtao
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestExerciseAverageScore(BaseTestCase):

    def test_exercise_average_score(self, cpb_api_scope, setupdata):
        """
        desc:验证用户练环节存在平均分
        steps:
        1、查询用户练环节存在平均分
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].exercise_average_score(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        book_id = 2867
        study_number = 22
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "select ROUND(avg(score),0) as avg_score from xmkp_child_picture_book.CPB_EXERCISE_SCORE "
            f"where user_id = {user_id} and book_id = {book_id} and study_number = {study_number} and is_deleted = 0 ", False)
        print(expect_res)
        expect_res = expect_res.avg_score if expect_res.avg_score is not None else 0
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 数据库断言
        self.assert_equal(expect_res, actual_res.data, "exercise_average_score接口返回的分数和数据库不一致")
