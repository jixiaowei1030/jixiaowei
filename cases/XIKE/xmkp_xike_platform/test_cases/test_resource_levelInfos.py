from utils.tools.base_test_case import BaseTestCase

class TestResourceLevelInfos(BaseTestCase):
    """
                        desc:验证获取书册级别下拉列表内容
                        steps:
                        1、查询获取书册级别下拉列表内容的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                                   2.3返回的书册条数与数据库一致
                        """
    def test_resource_levelInfos_01(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelInfos=xike_client[0].get_resource_levelInfos(setupdata.mobile,setupdata.password,data.businessType)
        print(test_resource_levelInfos)
        # 第二步：连接数据库查询实际结果
        resource_levelInfos = xike_client[1].query("select count(*) from xmkp_nce.NCE_BOOK where is_deleted = 0"
                                       , False)
        print(resource_levelInfos["count(*)"])
        # 第三步：断言
        self.assert_equal(0,test_resource_levelInfos.code)
        self.assert_equal("success",test_resource_levelInfos.message)
        self.assert_equal(resource_levelInfos["count(*)"],len(test_resource_levelInfos.data))

    def test_resource_levelInfos_02(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelInfos=xike_client[0].get_resource_levelInfos(setupdata.mobile,setupdata.password,data.businessType)
        print(test_resource_levelInfos)
        # 第二步：断言
        self.assert_equal(0,test_resource_levelInfos.code)
        self.assert_equal("success",test_resource_levelInfos.message)
        self.assert_equal(8,len(test_resource_levelInfos.data))

    def test_resource_levelInfos_03(self, xike_client, data, setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelInfos = xike_client[0].get_resource_levelInfos(setupdata.mobile, setupdata.password,
                                                                          data.businessType)
        print(test_resource_levelInfos)
        # 第二步：断言
        self.assert_equal(-100, test_resource_levelInfos.code)
        self.assert_equal("书籍信息获取异常,请检查配置", test_resource_levelInfos.message)




