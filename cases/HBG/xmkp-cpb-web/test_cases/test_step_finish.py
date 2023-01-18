"""
@Time ： 2021/5/20 17：00
@Auth ： Aries
@File ：test_step_finish.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
import json



@pytest.mark.usefixtures("cpb_api_scope")
class TestStepFinish(BaseTestCase):
    def test_step_finish(self, cpb_api_scope, data, setupdata):
        """
        desc:验证绘本结算页上报手否成功
        steps:
        1、查询获分享录音是否成功的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].step_finish(setupdata.mobile, setupdata.password, data.bookId, data.stepType)
        print(actual_res)
        # print(type(actual_res.data), actual_res.data)
        # print(type(actual_res.data), actual_res)
        # 第二步：断言
        # 接口状态断言
        self.assert_equal(0, actual_res.code, "step_finish接口调用失败")
        # 接口字段断言
        self.assert_equal(True, actual_res.data, "绘本结算页上报成功")