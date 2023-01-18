from utils.tools.base_test_case import BaseTestCase

class TestTaskReceiveReward(BaseTestCase):
    '''
    desc:验证领取活跃度
    steps:
    1、修改任务状态为已完成未领取
    2、查询当前活跃度
    3、获取任务活跃度
    4、调用活跃度接口，获取返回结果
    5、查询领取后的活跃度
    3、断言：3.1返回msg为0
           3.2返回ret为0
           3.3返回的success为true
           3.4领取的活跃度与配置一致



    '''
    def test_task_receive_reward(self,xxm_client,data,setupdata):
        #第一步：修改任务状态为已完成未领取
        xxm_client[1].query("update xxm_task.tb_user_task set status = 2  where uid = '%s' and task_id = '%s'"% (data.uid,data["test_task_receive_reward_01"]["taskId"]))
        #第二步：查询当前活跃度
        ponits_before =xxm_client[1].query("select points from  xxm_task.tb_user_points where uid = '%s'"% data.uid )
        print(ponits_before["points"])
        #第三步：获取任务活跃度
        point_task = xxm_client[1].query("select reward_value from  xxm_task.tb_task_config where id = %s" % data["test_task_receive_reward_01"]["taskId"])
        # 第四步：调用领取活跃度接口，获取返回结果
        test_task_receive_reward = xxm_client[0].task_receive_reward(mobile= setupdata.mobile, password= setupdata.password,req_json=data["test_task_receive_reward_01"])
        print(test_task_receive_reward)
        # 第五步：查询领取后的活跃度
        ponits_after =xxm_client[1].query("select points from  xxm_task.tb_user_points where uid = '%s'"% data.uid )
        print(ponits_after["points"])
        # 第六步：断言
        self.assert_equal("0",test_task_receive_reward["msg"])
        self.assert_equal( 0, test_task_receive_reward["ret"])
        self.assert_equal( True, test_task_receive_reward["data"]["success"])
        self.assert_equal(int(point_task["reward_value"]), ponits_after["points"]-ponits_before["points"])