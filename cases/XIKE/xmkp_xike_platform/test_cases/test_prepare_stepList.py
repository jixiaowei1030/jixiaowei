from utils.tools.base_test_case import BaseTestCase

class TestPrepareStepList(BaseTestCase):
    """
                        desc:验证获取课前准备内容
                        steps:
                        1、查询获取课前准备内容的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                        """
    def test_prepare_stepList(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_prepare_stepList=xike_client[0].get_prepare_stepList(setupdata.mobile,setupdata.password,data.businessType, data.campld, data.source)
        print(test_prepare_stepList)
        # 第二步：断言
        self.assert_equal(0,test_prepare_stepList.code)
        self.assert_equal("success",test_prepare_stepList.message)



