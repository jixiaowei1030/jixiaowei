from utils.tools.base_test_case import BaseTestCase

class TestFootballQuery(BaseTestCase):
    """
                        desc:验证查询用户兜底资源
                        steps:
                        1、查询用户兜底资源的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2success为true，
                                   2.3返回的兜底资源条数有2条
                        """
    def test_football_query(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_football_query=xike_client[0].get_football_query(setupdata.mobile,setupdata.password,data.footBallKey)
        print(test_football_query)
        print(len(test_football_query.data.userSources))
        # 第二步：断言
        self.assert_equal(0,test_football_query.code)
        self.assert_equal("success",test_football_query.message)
        self.assert_equal(2,len(test_football_query.data.userSources))



