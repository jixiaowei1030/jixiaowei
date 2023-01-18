from utils.tools.base_test_case import BaseTestCase

class TestXkHomeHomeInfo(BaseTestCase):
    """
                        desc:验证课程入口页查询
                        steps:
                        1、查询获取课程入口页查询的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                        """
    def test_xkHome_homeInfo(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_xkHome_homeInfo=xike_client[0].get_xkHome_homeInfo(setupdata.mobile,setupdata.password)
        print(test_xkHome_homeInfo)
        # 第二步：断言
        self.assert_equal(0,test_xkHome_homeInfo.code)
        self.assert_equal("success",test_xkHome_homeInfo.message)
        self.assert_equal(2,len(test_xkHome_homeInfo.data.myLessons))



