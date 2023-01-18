"""
@Time ： 2021/3/24 14:40
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
import datetime

@pytest.mark.usefixtures("cpb_api_scope")
class TestIsShowDakaTip(BaseTestCase):

    def test_is_show_daka_tip(self, cpb_api_scope, setupdata):
        """
        desc:判断是否提示打卡成功信息或者是否播放打卡成功的动画
        steps:
        1、查询是否播放过打卡成功提示,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].is_show_daka_tip(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        user_id = cpb_api_scope[3]
        sys_date = datetime.date.today()
        print(sys_date)
        # 第三步：查数据库获取数据库期望结果
        redis_key = f"newDaka:{user_id}:{sys_date}"
        print(redis_key)
        redis_rsp = cpb_api_scope[2].get(redis_key)
        print(type(redis_rsp), redis_rsp)
        expect_res = True if redis_rsp == str(user_id)  else False
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # redis断言
        # self.assert_equal(expect_res, actual_res.data, "is_show_daka_tip断言失败")
