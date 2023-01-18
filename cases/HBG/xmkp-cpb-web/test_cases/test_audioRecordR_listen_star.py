"""
@Time ： 2021/3/31 14:35
@Auth ： wangtao
@File ：test_audioRecordR_listen_star.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestAudioRecordRListenStar(BaseTestCase):

    def test_audioRecordR_listen_star(self, cpb_api_scope, setupdata, data):
        """
        desc:验证星星上报是否成功
        steps:
        1、查询获取轮播图的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].audioRecordR_listen_star(setupdata.mobile, setupdata.password,data.retryTime, data.bookId, data.pageId, data.audioRef)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_response(actual_res)
        self.assert_equal(0, actual_res.data, "星星上报失败")
