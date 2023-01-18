"""
@Time ： 2021/4/7 15:30
@Auth ： liulian
@File ：test_audioRecordR_star.py
@IDE ：PyCharm
"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase
from utils.common import get_mysql


@pytest.mark.usefixture("cpb_api_scope")
class TestAudioRecordR(BaseTestCase):

    def test_audioRecordR_star_0(self, cpb_api_scope, setupdata, data):
        """
        desc:读环节上报90分，对应上报的星星数为3
        steps：
        1.获取用户的response
        2.断言接口是否请求成功'
        3.断言星星数是否上报成功
        """
        # 第1步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第2步：清除已有测试数据
        cpb_api_scope[1].query("delete FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2513 and audio_ref =462 and user_id ={}".format(
                user_id), True)
        # 第3步：请求接口，断言响应
        actual_res = cpb_api_scope[0].audioRecordR_star(setupdata.mobile, setupdata.password, data.type, data.score, data.retryTime, data.bookId, data.pageId,data.audioRef, data.audioType)
        print(actual_res)
        # 第4步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2513 and audio_ref =462 and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['star_count'])
        # 第5步：断言读环节90分区间上报星星数是否为3
        self.assert_equal(0, actual_res.code, "接口调用失败")
        self.assert_equal(expect_res[0]['star_count'], actual_res.data, "读环节星星数上报失败")

    def test_audioRecordR_star_1(self, cpb_api_scope, setupdata, data):
        """
        desc:读环节上报70分，对应上报的星星数为2
        """
        # 第1步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第2步：准备已有测试数据
        cpb_api_scope[1].query("delete FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2514 and audio_ref =634 and user_id ={}".format(
                user_id), True)
        # 第3步：请求接口，断言响应
        actual_res = cpb_api_scope[0].audioRecordR_star(setupdata.mobile, setupdata.password, data.type, data.score, data.retryTime, data.bookId, data.pageId,
                                                        data.audioRef, data.audioType)
        print(actual_res)
        # 第4步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]        # 第5步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2514 and audio_ref =634 and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['star_count'])
        # 第3步：断言读环节70分区间上报星星数是否为2
        self.assert_equal(0, actual_res.code, "接口调用失败")
        self.assert_equal(expect_res[0]['star_count'], actual_res.data, "读环节星星数上报失败")

    def test_audioRecordR_star_2(self, cpb_api_scope, setupdata, data):
        """
        desc:读环节上报40分，对应上报的星星数为1
        """
        # 第1步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]        # 第2步：清除已有测试数据
        cpb_api_scope[1].query("delete FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2536 and audio_ref =555 and user_id ={}".format(
                user_id), True)
        # 第3步：请求接口，断言响应
        actual_res = cpb_api_scope[0].audioRecordR_star(setupdata.mobile, setupdata.password, data.type, data.score, data.retryTime, data.bookId, data.pageId,
                                                        data.audioRef, data.audioType)
        print(actual_res)
        # 第4步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2536 and audio_ref =555 and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['star_count'])
        # 第5步：断言读环节50分区间上报星星数是否为0
        self.assert_equal(0, actual_res.code, "接口调用失败")
        self.assert_equal(expect_res[0]['star_count'], actual_res.data, "读环节星星数上报失败")

    def test_audioRecordR_star_3(self, cpb_api_scope, setupdata, data):
        """
        desc:读环节上报0分，对应上报的星星数为0
        """
        # 第1步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第2步：清除已有测试数据
        cpb_api_scope[1].query("delete FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2537 and audio_ref =556 and user_id ={}"
                               .format(user_id), True)
        # 第3步：请求接口，断言响应
        actual_res = cpb_api_scope[0].audioRecordR_star(setupdata.mobile, setupdata.password, data.type, data.score, data.retryTime, data.bookId, data.pageId,
                                                        data.audioRef, data.audioType)
        print(actual_res)
        # 第4步：查询mysql该用户年度打卡天数
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_STAR  where audio_type ='1' and book_id=3013 and page_id=2537 and audio_ref =556 and user_id ={}".format(
                user_id), True)
        print(expect_res[0]['star_count'])
        # 第5步：断言读环节50分区间上报星星数是否为0
        self.assert_equal(0, actual_res.code, "接口调用失败")
        self.assert_equal(expect_res[0]['star_count'], actual_res.data, "读环节星星数上报失败")

