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
class TestShareRecord(BaseTestCase):
    def test_share_record(self, cpb_api_scope, data, setupdata):
        """
        desc:验证获取分享录音是否成功(没有token的用户)
        steps:
        1、查询获分享录音是否成功的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].share_record(setupdata.mobile, setupdata.password, data.uid, data.bookId)
        print(actual_res)
        # 第二步：断言
        # 接口状态断言
        self.assert_equal(2027, actual_res.code, "share_record接口调用失败")
        # 接口字段断言
        self.assert_equal("没有权限！", actual_res.message, "share_record接口,message应该为'没有权限！'")
