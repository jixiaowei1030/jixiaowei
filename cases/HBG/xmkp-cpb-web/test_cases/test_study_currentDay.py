"""
@Time ： 2021/1/26 22:15
@Auth ： wangtao
@File ：test_adConfig_get.py
@IDE ：PyCharm

"""

import re
import datetime
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestStudyCurrentDay(BaseTestCase):

    def test_study_currentDay(self, cpb_api_scope, setupdata):
        """
        desc:验证未完成打卡的用户，打卡状态为"未打卡"
        steps:
        1、查询获取用户打卡状态的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].study_currentDay(setupdata.mobile, setupdata.password)
        print(type(actual_res), actual_res)
        # 第二步：准备测试数据，获取用户的user_id

        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        # user_id = re.search("=(.*?)&", UserToken.get_vget_valuealue()["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        # 第二步：查询数据库，获取数据库的期望结果
        sysdate = datetime.datetime.now().strftime("%Y-%m-%d")
        redis_key = f"newDaka:{user_id}:{sysdate}".format(user_id)
        redis_rsp = cpb_api_scope[2].get(redis_key)
        print(redis_rsp)
        expect_res = True if redis_rsp is not None else False
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "study_currentDay接口调用失败")
        # 断言用户的打卡状态是否正确
        self.assert_equal(expect_res,actual_res.data.status, "用户打卡状态返回错误")
