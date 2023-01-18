"""
@Time ： 2021/4/7 11:26
@Auth ： liulian
@File ：test_adConfig_get.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestUserStudyDetail(BaseTestCase):

    def test_user_study_detail_0(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取"该用户的打卡日历"列表（时间段【2020/01/01-2020/10/31】所有用户均不存在打卡记录）
        steps:
        1、查询"该用户的打卡日历"列表的接口,获得返回json
        2、接口断言：接口调用是否成功,
        3、接口断言：返回的打卡记录数组是否为空，数组长度为0
        """
        # 第1步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].user_study_detail(data.beginDate, data.endDate, setupdata.mobile,
                                                        setupdata.password)
        print(type(actual_res), actual_res)
        print(len(actual_res.data))
        # 第2步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "user_study_detail_0接口返回状态码错误")
        self.assert_equal("success", actual_res.message, "user_study_detail_0接口返回信息错误")
        # 断言该用户在【2020/01/01-2020/10/31】期间不存在打卡记录
        self.assert_equal(0, len(actual_res.data), "该用户【2020/01/01-2020/10/31】期间存在异常打卡记录")

    def test_user_study_detail_1(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取"该用户在2020年间是否存在打卡记录）
        steps:
        1、查询"该用户的打卡日历"列表的接口,获得返回json
        2、接口断言：接口调用是否成功,
        3、接口断言：返回的打卡记录是否与数据库一致，数组长度为0
        """
        # 第1步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].user_study_detail(data.beginDate, data.endDate, setupdata.mobile,
                                                        setupdata.password)
        print(type(actual_res), actual_res.data)
        # 第2步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        print(user_id)
        # 第3步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT sum(complete_days) FROM xmkp_child_picture_book.CPB_DAKA_DETAIL WHERE month BETWEEN '2020-11' AND '2020-12' and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['sum(complete_days)'])
        # 第4步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "user_study_detail_1接口返回状态码错误")
        # self.assert_not_null(actual_res.data, "user_study_detail_1接口返回信息错误")
        # 断言用户累计打卡次数是否与数据库一致
        # 接口返回的该用户累计打卡天数
        Totalnum = int(0)
        for i in range(0, len(actual_res.data) - 1):
            if actual_res.data[i].complete == True:
                Totalnum = Totalnum + 1
        print(Totalnum)
        try:
            self.assert_equal(expect_res[0]['sum(complete_days)'], Totalnum, "用户完成打卡天数数数据与数据库不一致")
        except:
            self.assert_is_none(expect_res[0]['sum(complete_days)'])



    def test_user_study_detail_2(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取"该用户在2021年间是否存在打卡记录）
        steps:
        1、查询"该用户的打卡日历"列表的接口,获得返回json
        2、接口断言：接口调用是否成功,
        3、接口断言：返回的打卡记录是否与数据库一致，数组长度为0
        """
        # 第1步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].user_study_detail(data.beginDate, data.endDate, setupdata.mobile,
                                                        setupdata.password)
        print(type(actual_res), actual_res.data)
        # 第2步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        # 第3步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT sum(complete_days) FROM xmkp_child_picture_book.CPB_DAKA_DETAIL WHERE month BETWEEN '2021-01' AND '2021-12' and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['sum(complete_days)'])
        # 第4步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "user_study_detail_2接口返回状态码错误")
        self.assert_not_null(actual_res.data, "user_study_detail_2接口返回信息错误")
        # 断言用户累计打卡次数是否与数据库一致
        # 接口返回的该用户累计打卡天数
        Totalnum = int(0)
        for i in range(0, len(actual_res.data) - 1):
            if actual_res.data[i].complete == True:
                Totalnum = Totalnum + 1
        print(Totalnum)
        self.assert_equal(expect_res[0]['sum(complete_days)'], Totalnum, "用户完成打卡天数数数据与数据库不一致")
