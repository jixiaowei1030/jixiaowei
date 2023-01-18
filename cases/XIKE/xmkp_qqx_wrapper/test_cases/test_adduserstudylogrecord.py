"""
@author:lhz
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time
import pytest

@pytest.mark.Ji
@allure.epic("bookworm")
class TestBookWormAddUserStudyLogReport(BaseTestCase):
    """
                    desc:新增学习记录
                    steps:
                    1、查询环节id的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，

                    """
    @allure.title("{data.casename}")
    def test_bookworm_add_user_study_log_record(self, xike_client, data, setupdata):
        """新增学习记录"""
        # 第一步：调用接口，获取返回结果
        get_userstudyreport = xike_client[0].add_user_study_log_record(data.logType, data.studyTime, data.practiceId, data.stepId, data.content, data.contentLength, data.bookId, data.result, data.chapterId, data.startTime, data.endTime, data.selection, data.beAddPunchCardRecord, setupdata.mobile, setupdata.password)
        # print(get_userstudyreport)
        # 第二步：断言
        self.assert_equal(0, get_userstudyreport.code)
        self.assert_equal("success", get_userstudyreport.message)

    @allure.title("{data.casename}")
    def test_bookworm_add_user_study_log_record_with_wrong_bookid(self, xike_client, data, setupdata):
        """根据错误bookid上传学习记录"""
        # 第一步：调用接口，获取返回结果
        get_userstudyreport = xike_client[0].add_user_study_log_record(data.logType, data.studyTime, data.practiceId, data.stepId, data.content, data.contentLength, data.bookId, data.result, data.chapterId, data.startTime, data.endTime, data.selection, data.beAddPunchCardRecord, setupdata.mobile, setupdata.password)
        print(get_userstudyreport)
        # 第二步：断言
        self.assert_equal(0, get_userstudyreport.code)
        self.assert_equal("success", get_userstudyreport.message)


