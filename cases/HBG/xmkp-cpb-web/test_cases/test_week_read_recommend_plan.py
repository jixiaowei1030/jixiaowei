"""
@Time ： 2021/3/30 19:55
@Auth ： liulian
@File ：test_cashBack_learnDuration.py
@IDE ：PyCharm
"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestWeekReadRecommendPlan(BaseTestCase):
    def test_week_read_recommend_plan_1(self, cpb_api_scope, data, setupdata):
        """
        desc:修改用户绘本馆学习计划
        steps：
        1.获取用户的response
        2.assert1接口是否请求成功'
        3.assert2绘本等级是否正确
        4.assert3绘本数量是否正确
        """
        # 第1步：请求接口，断言响应
        print(data)
        print(str(data.level) + "-----" + str(data.bookCount))
        actual_res = cpb_api_scope[0].week_read_recommend_plan(setupdata.mobile, setupdata.password,
                                                               data.level, data.bookCount)
        print(actual_res)
        # 第2步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        print(user_id)
        self.assert_response(actual_res)
        # 第3步：查询redis该用户学习计划的绘本数量
        redis_key = f"redisCache::cpb_week_read_recommend_book_count_{user_id}"
        print(redis_key)
        redis_res = cpb_api_scope[2].get(redis_key)
        self.assert_equal(int(redis_res), actual_res.data.bookCount, "绘本数量修改失败")
        # 第4步：查询mysql该用户学习计划的绘本等级并做判断
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER WHERE user_id ={}".format(user_id), True)
        self.assert_equal(expect_res[0].level, actual_res.data.level, "绘本数等级修改失败")
        # 第5步：接口响应成功
        self.assert_equal(0, actual_res.code, "绘本数修改错误")

    def test_week_read_recommend_plan_2(self, cpb_api_scope, data, setupdata):
        """
        desc:修改用户绘本馆学习计划（异常场景）
        steps：
        1.获取用户的response
        2.assert1接口是否请求成功'
        3.assert2绘本等级是否正确
        4.assert3绘本数量是否正确
        @type data: object
        """
        # 第1步：请求接口，断言响应
        print(data)
        print(str(data.level) + "-----" + str(data.bookCount))
        actual_res = cpb_api_scope[0].week_read_recommend_plan(setupdata.mobile, setupdata.password,data.level, data.bookCount)
        # 第2步：默认值：绘本等级：1、绘本数量：5
        print(actual_res.data.bookCount)
        print(actual_res.data.level)
        self.assert_equal(5, actual_res.data.bookCount, "绘本数量修改失败")
        self.assert_equal(1, actual_res.data.level, "绘本数等级修改失败")
        # 第3步：接口响应成功
        self.assert_equal(0, actual_res.code, "绘本数修改错误")
