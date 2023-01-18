"""
@Time ： 2021/4/12 11:10
@Auth ： Aries
@File ：test_audioRecordR_exercise_star.py
@IDE ：PyCharm

"""
import re
import datetime
import pytest
from utils.tools.base_test_case import BaseTestCase
from utils.common import get_redis


@pytest.mark.usefixtures("cpb_api_scope")
class TestAudioRecordRExerciseStar(BaseTestCase):

    def test_audioRecordR_exercise_star(self, cpb_api_scope, setupdata, data):
        """
        desc:验证练环节，练习题上报分数
        steps:
        1、查询获取练环节，练习题上报分数,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].audioRecordR_exercise_star(setupdata.mobile, setupdata.password, data.type, data.score, data.retryTime, data.bookId,
                                                                 data.exerciseRef, data.isRead, data.studyNumber)
        print(actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_EXERCISE_SCORE a WHERE a.user_id ={} AND a.book_id={}".format(
                user_id, data.bookId), False)
        print(expect_res)
        print(expect_res.score)
        # 第四步：断言
        self.assert_response(actual_res)
        # 数据库断言
        self.assert_is_not_none(expect_res.score, "练环节上报分数接口获取失败")
