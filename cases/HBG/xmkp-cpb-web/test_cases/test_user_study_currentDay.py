"""
@Time ： 2021/3/24 11:40
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
from datetime import datetime


@pytest.mark.usefixtures("cpb_api_scope")
class TestUserStudyInfo(BaseTestCase):

    def test_user_study_currentDay(self, cpb_api_scope,setupdata):
        """
        desc:获取用户学习状态
        steps:
        1、查询用户学习状态,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].user_study_currentDay(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        user_id = cpb_api_scope[3]  # 获取uid
        today_date = datetime.today().date()  # 获取今天的日期
        # 第三步：查数据库获取数据库期望结果
        expect_sql_res = cpb_api_scope[1].query(
            f"SELECT * from xmkp_child_picture_book.CPB_DAKA_DETAIL a WHERE a.user_id = {user_id}", True)
        print(expect_sql_res)
        # 获得期望的创建时间
        expect_res_create_time = [expect_sql_res[i].create_time.date() for i in range(len(expect_sql_res))]
        # 获得期望的更新时间
        expect_res_update_time = [
            expect_sql_res[i].update_time.date() if isinstance(expect_sql_res[i].update_time, datetime)
            else datetime.strptime("1970-01-01", "%Y-%m-%d") for i in
            range(len(expect_sql_res))]
        # 期望的创建时间和期望的创建时间进行合并
        expect_res = expect_res_create_time + expect_res_update_time
        print(expect_res)
        # 第四步：断言
        # 接口状态断言
        self.assert_response(actual_res)
        if today_date in expect_res:
            # 如果今天的日期在数据库中的创建时间和更新时间中
            self.assert_true(actual_res.data.status)
        else:
            self.assert_false(actual_res.data.status)
