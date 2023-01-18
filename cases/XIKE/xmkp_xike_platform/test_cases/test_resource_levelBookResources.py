from utils.tools.base_test_case import BaseTestCase

class TestResourceLevelBookResources(BaseTestCase):
    """
                        desc:验证【级别切换页】- 通过级别查询获取级别及其下资源列表。新概念特殊添加体验营信息
                        steps:
                        1、查询【级别切换页】- 通过级别查询获取级别及其下资源列表。新概念特殊添加体验营信息的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                                   2.3返回的书册名与数据库一致
                        """
    def test_resource_levelBookResources_01(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelBookResources=xike_client[0].get_resource_levelBookResources(setupdata.mobile,setupdata.password,data.businessType,data.levelCode)
        print(test_resource_levelBookResources)
        # 第二步：连接数据库查询实际结果
        resource_levelBookResources = xike_client[1].query("select title from xmkp_nce.NCE_BOOK where book_type = %s and is_deleted = 0" % data.levelCode
                                                   , False)
        # 第三步：断言
        self.assert_equal(0,test_resource_levelBookResources.code)
        self.assert_equal("success",test_resource_levelBookResources.message)
        self.assert_equal(resource_levelBookResources["title"],test_resource_levelBookResources.data.levelInfo.name)

    def test_resource_levelBookResources_02(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelBookResources=xike_client[0].get_resource_levelBookResources(setupdata.mobile,setupdata.password,data.businessType,data.levelCode)
        print(test_resource_levelBookResources)
        # 第二步：连接数据库查询实际结果
        resource_levelBookResources = xike_client[1].query(
            "select title from xmkp_nce.NCE_BOOK where book_type = %s and is_deleted = 0" % data.levelCode
            , False)
        # 第三步：断言
        self.assert_equal(0,test_resource_levelBookResources.code)
        self.assert_equal("success",test_resource_levelBookResources.message)
        self.assert_equal(resource_levelBookResources["title"],test_resource_levelBookResources.data.levelInfo.name)

    def test_resource_levelBookResources_03(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_levelBookResources=xike_client[0].get_resource_levelBookResources(setupdata.mobile,setupdata.password,data.businessType,data.levelCode)
        print(test_resource_levelBookResources.data.levelInfo)
        # 第二步：断言
        self.assert_equal(0,test_resource_levelBookResources.code)
        self.assert_equal("success",test_resource_levelBookResources.message)
        self.assert_equal(None,test_resource_levelBookResources.data.levelInfo)


