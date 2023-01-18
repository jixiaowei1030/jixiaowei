"""
@Time ： 2021/3/31 13:50
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
import json


@pytest.mark.usefixtures("cpb_api_scope")
class TestPointAnanlysisPointData(BaseTestCase):

    def test_point_analysis_point_data(self, cpb_api_scope, setupdata, data):
        """
        desc:验证绘本是否曝光
        steps:
        1、查询获取绘本曝光的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].point_analysis_point_data(setupdata.mobile, setupdata.password, data.bookId, data.typeId, data.level)
        print(data.bookId)
        print(actual_res)
        print(actual_res.data)
        # 接口断言
        self.assert_equal('success', actual_res.data, "point_analysis_point_data接口调用失败")
        self.assert_response(actual_res)

