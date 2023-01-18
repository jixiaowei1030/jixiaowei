
"""
@Time ： 2021/5/14 16:30
@Auth ： liulian
@File ：test_audioRecordR_see_star.py
@IDE ：PyCharm
"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase



@pytest.mark.usefixture("cpb_api_scope")
class TestAudioRecordRSeetar(BaseTestCase):
    def test_audioRecordR_see_star_1(self, cpb_api_scope, setupdata, data):
        """
        desc:上报看环节学习内页获取星星数（看环节由于还在重构目前代码已屏蔽，后续追加判断）
        steps：
        1.获取用户的response
        2.assert1接口是否请求成功'
        3.assert2绘本等级是否正确
        4.assert3绘本数量是否正确
        """
        # 第1步：请求接口，断言响应
        print(data)
        actual_res = cpb_api_scope[0].audioRecordR_see_star(setupdata.mobile, setupdata.password, data.bookId, data.pageId, data.exploreDiscoveryRef)
        print(actual_res)
        # 第2步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        print(user_id)
        self.assert_response(actual_res)
        # # 第4步：查询mysql该用户看环节星星级记录并判断
        # expect_res = cpb_api_scope[1].query(
        #         "SELECT * FROM xmkp_child_picture_book.CPB_USER WHERE user_id ={}".format(user_id), True)
        # self.assert_equal(expect_res[0].data, actual_res.data., "绘本数等级修改失败")
        # 第5步：接口响应成功
        self.assert_equal(0, actual_res.code, "接口响应异常")
        self.assert_equal(0, actual_res.data, "接口响应异常")
        if type(actual_res.code) is int:
            print('audioRecordR_see_star接口测试通过')
        else:
            print('audioRecordR_see_star接口测试不通过')
        # a = str(actual_res.data)
        # print(str.isdigit(a))

