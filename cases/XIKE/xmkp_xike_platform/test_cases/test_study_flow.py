from utils.tools.base_test_case import BaseTestCase

class TestStudyFlow(BaseTestCase):
    """
                        desc:验证学习流程
                        steps:
                        1、调用学习流程接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                                   2.3返回的campid与请求一致
                                   2.4返回的环节名称与数据库一致
                        """
    def test_study_flow_01(self,xike_client,data,setupdata):
        # 第一步：调用预习环节接口，获取返回结果
        test_nce_step_detail=xike_client[0].nce_step_detail(mobile=setupdata["mobile"],password=setupdata["password"],req_json=data["test_study_flow_01_01"])
        print(test_nce_step_detail)
        # 第二步：连接数据库查询实际结果
        nce_step_detail = xike_client[1].query("select name from cms.step where step_id = '%s'" % data["test_study_flow_01_01"]["stepId"], False)
        # 第三步：断言
        self.assert_equal(0,test_nce_step_detail.code)
        self.assert_equal("success",test_nce_step_detail.message)
        self.assert_equal(data["test_study_flow_01_01"]["campId"],test_nce_step_detail.data.campId)
        self.assert_equal(nce_step_detail.name, test_nce_step_detail.data.stepTitle)




