from utils.tools.base_test_case import BaseTestCase

class TestStepProgessRecord(BaseTestCase):
    """
                        desc:验证环节学习记录
                        steps:
                        1、查询环节学习记录接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                        """
    def test_step_progess_record_01(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_step_progess_record=xike_client[0].step_progress_record(mobile=setupdata["mobile"],password=setupdata["password"],req_json=data["test_step_progess_record_01_01"])
        print(test_step_progess_record)
        # 第二步：断言
        self.assert_equal(0,test_step_progess_record.code)
        self.assert_equal("success",test_step_progess_record.message)





