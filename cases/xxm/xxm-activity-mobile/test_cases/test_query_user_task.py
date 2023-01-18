from utils.tools.base_test_case import BaseTestCase

class TestQueryUserTask(BaseTestCase):
    '''
    desc:验证新手活动入口
    steps:
    1、查询新手活动结果
    2、连接数据库，查询活动数据
    3、断言：3.1返回msg为0
           3.2返回ret为0
           3.3返回的活动数量与数据库一致



    '''
    def test_receive_reward(self,xxm_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_query_user_task = xxm_client[0].query_user_task(setupdata.mobile,setupdata.password)
        print(test_query_user_task)
        # 第二步：连接数据库，查询实际结果
        query_user_task = xxm_client[1].query("select count(*) from xxm_task.tb_user_task where uid = '%s'"% data.uid)
        # 第三步：断言
        self.assert_equal("0",test_query_user_task["msg"])
        self.assert_equal( 0, test_query_user_task["ret"])
        self.assert_equal(query_user_task["count(*)"], len(test_query_user_task["data"]["userTaskInfos"]))
