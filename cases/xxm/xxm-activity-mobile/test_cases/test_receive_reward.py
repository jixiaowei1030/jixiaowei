from utils.tools.base_test_case import BaseTestCase

class TestReceiveReward(BaseTestCase):
    '''
    desc:验证vip奖励
    steps:
    1、删除奖励记录
    2、调用领取vip奖励接口，获取返回结果
    3、连接数据库，获取领取奖励记录
    4、断言：4.1返回msg为0
           4.2返回ret为0
           4.3返回的success为true
           4.4数据库的奖励记录与请求一致



    '''
    def test_receive_reward(self,xxm_client,data,setupdata):
        # 第一步：删除奖励记录
        xxm_client[1].query("delete from xxm_task.tb_user_reward_record where uid = '%s' and reward_type = %s"% (data.uid,data["test_receive_reward_01"]["rewardType"]))
        # 第二步：调用领取vip奖励接口，获取返回结果
        test_receive_reward = xxm_client[0].reveive_reward(mobile= setupdata.mobile, password= setupdata.password,req_json=data["test_receive_reward_01"])
        print(test_receive_reward)
        # 第三步：查询数据库，获取记录
        receive_reward = xxm_client[1].query("select reward_type from xxm_task.tb_user_reward_record where uid = '%s' and reward_type = %s "% (data.uid,data["test_receive_reward_01"]["rewardType"]) )
        print(receive_reward)
        # 第四步：断言
        self.assert_equal("0",test_receive_reward["msg"])
        self.assert_equal( 0, test_receive_reward["ret"])
        self.assert_equal( True, test_receive_reward["data"]["success"])
        self.assert_equal(data["test_receive_reward_01"]["rewardType"], receive_reward["reward_type"])