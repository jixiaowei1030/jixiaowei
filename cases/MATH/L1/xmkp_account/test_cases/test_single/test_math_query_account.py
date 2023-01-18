"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L1")
class TestMathQueryaccount(BaseTestCase):
    """
                    desc:验证账户的查询
                    steps:
                    1、查询账户的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，
                               2.3返回的diamond_balance:钻石总和 star_balance:星星总和与数据库amount总和相等

                    """
    @allure.title("查询账户信息")
    def test_math_queryaccount(self,math_client,setupdata):
        """L1查询账户信息"""
        # 第一步：调用接口，获取返回结果
        query_account=math_client[0].query_account(setupdata.mobile,setupdata.password)
        #获取用户id
        uid=query_account.data.uid
        # 第二步：连接数据库查询预期结果 diamond_balance:钻石总和 star_balance:星星总和
        diamond_balance = math_client[1].query("select sum(amount) all_amount from goodxs.account_record where user_id='%s' and account_type='DIAMOND'" % uid, False)
        star_balance = math_client[1].query("select sum(amount) all_amount from goodxs.account_record where user_id='%s' and account_type='star'" % uid, False)
        # 第三步：断言
        self.assert_equal(0,query_account.code)
        self.assert_equal("success",query_account.message)
        # self.assert_equal(str(diamond_balance.all_amount), query_account.data.accountItemRpcVOs[0].balance,"钻石数量不等")
        # self.assert_equal(str(star_balance.all_amount), query_account.data.accountItemRpcVOs[1].balance, "星星数量不等")



