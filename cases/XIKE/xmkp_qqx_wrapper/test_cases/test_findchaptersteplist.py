"""
@author:lhz
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time


@allure.epic("bookworm")
class TestBookWormFindChapterSteplist(BaseTestCase):
    """
                    desc:根据章节id获取环节列表
                    steps:
                    1、查询环节id的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，

                    """
    @allure.title("{data.casename}")
    def test_bookworm_find_chapter_steplist(self, xike_client, data, setupdata):
        """根据章节id获取环节列表"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_chapter_steplist(data.chapterId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)

    @allure.title("{data.casename}")
    def test_bookworm_find_chapter_steplist_with_wrong_chapter(self, xike_client, data, setupdata):
        """根据错误章节id获取环节列表"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_chapter_steplist(data.chapterId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)

    @allure.title("{data.casename}")
    def test_bookworm_find_chapter_steplist_with_empty_string(self, xike_client, data, setupdata):
        """章节id为空字符串"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_chapter_steplist(data.chapterId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)

    @allure.title("{data.casename}")
    def test_bookworm_find_chapter_steplist_with_int_stepid(self, xike_client, data, setupdata):
        """章节id为数字"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_chapter_steplist(data.chapterId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)