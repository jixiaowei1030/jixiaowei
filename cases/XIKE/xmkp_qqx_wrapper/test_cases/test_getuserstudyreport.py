"""
@author:lhz
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time


@allure.epic("bookworm")
class TestBookWormGetUserStudyReport(BaseTestCase):
    """
                    desc:根据环节id获取内容
                    steps:
                    1、查询环节id的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，

                    """
    @allure.title("{data.casename}")
    def test_bookworm_get_user_study_report(self, xike_client, data, setupdata):
        """根据环节id获取内容"""
        # 第一步：调用接口，获取返回结果
        get_userstudyreport = xike_client[0].get_user_study_report(data.bookId, data.chapterId, data.stepId, setupdata.mobile, setupdata.password)
        #print(get_userstudyreport)
        # 第二步：断言
        self.assert_equal(0, get_userstudyreport.code)
        self.assert_equal("success", get_userstudyreport.message)




