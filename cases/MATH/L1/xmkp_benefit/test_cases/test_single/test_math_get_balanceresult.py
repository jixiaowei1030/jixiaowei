"""
@author:xiaowei.ji
"""
from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L1")
class TestMathGetBalanceresult(BaseTestCase):

    # @classmethod
    # def setup_class(cls):
    #     cls.client=HttpClientMath()

    @allure.title("{data.case_name}")
    def test_math_get_balanceresult(self,math_client,data,setupdata):
        """L1获取余额结果"""
        get_balanceresult=math_client[0].get_balanceresult(data.albumId,data.lessonId,setupdata.mobile,setupdata.password)
        rewardnum=math_client[1].query("select star_num from goodxs.study_user_lesson_record where user_id='%s' and album_id='%s' and lesson_id='%s' and is_delete=0"%(data.userId,data.albumId,data.lessonId))
        self.assert_equal(0,get_balanceresult.code)
        self.assert_equal("success",get_balanceresult.message)
        self.assert_equal(rewardnum["star_num"],get_balanceresult.data.balanceResultDTO.rewardNum)
        print(get_balanceresult.data.balanceResultDTO.rewardNum)
        print(rewardnum["star_num"])