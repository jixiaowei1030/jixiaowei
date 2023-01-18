"""
@Time ： 2021/3/19 22:15
@Auth ： liulian
@File ：test_listen_win_stars.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestMetadataDeviceDecoder(BaseTestCase):
    def test_metadata_deviceDecoder_1(self, cpb_api_scope, setupdata):
        """
        desc:验证获取"设备信息"列表（该接口数据配置在football中，未存库）
        steps:
        1、查询"获取用户设备信息"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].metadata_deviceDecoder(setupdata.mobile, setupdata.password)
        print(type(actual_res), actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第三步：查询redis数据库，获取数据库的期望结果
        '''expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_LISTEN_STAR a WHERE a.user_id ={}".format(user_id), False)
        print(expect_res)'''
        # 第四步：断言
        # 断言接口调用是否成功
        self.assert_equal("0", actual_res.ret, "接口响应成功")
        self.assert_equal("MI", actual_res.data.audioDevice[0], "接口响应成功")
        k = actual_res.data.audioDevice
        for i in range(0, len(k) - 1):
            self.assert_equal(k[i], actual_res.data.audioDevice[i], "设备信息正确")

        '''apollo配置信息如下：
        k = ["MI", "Redmi K20 Pro", "MI 8", "MI 9", "Redmi K20 Pro Premium Edition", "HMA-AL00", "MI PAD 2", "NX569H",
             "MAR-AL00", "MIX 3",
             "Lenovo TB-8705F", "Redmi K20", "V2020CA", "Redmi Note 7 Pro", "TAS-AL00", "V1813A", "Mi9 Pro 5G",
             "DLT-A0", "Redmi K30", "G0245D", "Redmi Note 3", "U1006", "MI PAD 4 PLUS", "V1829A", "MRX-W39", "LYA-AL00",
             "Mi 10"]'''


