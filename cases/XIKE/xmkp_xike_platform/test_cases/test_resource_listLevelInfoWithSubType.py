from utils.tools.base_test_case import BaseTestCase

class TestResourceListLevelInfoWithSubType(BaseTestCase):
    """
                        desc:验证获取书册级别下拉列表内容
                        steps:
                        1、查询获取书册级别下拉列表内容的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                                   2.3返回的书册条数与数据库一致
                        """
    def test_resource_ListLevelInfoWithSubType_01(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_ListLevelInfoWithSubType=xike_client[0].get_resource_listLevelInfoWithSubType(setupdata.mobile,setupdata.password,data.subBusinessType,data.businessType)
        print(test_resource_ListLevelInfoWithSubType)
        # 第二步：连接数据库查询实际结果
        resource_levelInfos = xike_client[1].query(
            "select count(*) from cms.cms_level where level_id like 'NCE%' and is_delete = 'N'"
            , False)
        print(resource_levelInfos["count(*)"])
        # 第三步：断言
        self.assert_equal(0, test_resource_ListLevelInfoWithSubType.code)
        self.assert_equal("success", test_resource_ListLevelInfoWithSubType.message)
        self.assert_equal(resource_levelInfos["count(*)"], len(test_resource_ListLevelInfoWithSubType.data))

    def test_resource_ListLevelInfoWithSubType_02(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_ListLevelInfoWithSubType=xike_client[0].get_resource_listLevelInfoWithSubType(setupdata.mobile,setupdata.password,data.subBusinessType,data.businessType)
        print(test_resource_ListLevelInfoWithSubType)
        # 第二步：断言
        self.assert_equal(0,test_resource_ListLevelInfoWithSubType.code)
        self.assert_equal("success",test_resource_ListLevelInfoWithSubType.message)
        self.assert_equal(8,len(test_resource_ListLevelInfoWithSubType.data))

    def test_resource_ListLevelInfoWithSubType_03(self, xike_client, data, setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_ListLevelInfoWithSubType = xike_client[0].get_resource_listLevelInfoWithSubType(setupdata.mobile, setupdata.password,data.subBusinessType,
                                                                         data.businessType)
        print(test_resource_ListLevelInfoWithSubType)
        # 第二步：断言
        self.assert_equal(-100, test_resource_ListLevelInfoWithSubType.code)
        self.assert_equal("书籍信息获取异常,请检查配置", test_resource_ListLevelInfoWithSubType.message)

    def test_resource_ListLevelInfoWithSubType_04(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_resource_ListLevelInfoWithSubType=xike_client[0].get_resource_listLevelInfoWithSubType(setupdata.mobile,setupdata.password,data.subBusinessType,data.businessType)
        print(test_resource_ListLevelInfoWithSubType)
        # 第二步：连接数据库查询实际结果
        resource_levelInfos = xike_client[1].query(
            "select count(*) from cms.cms_level where level_id like 'NCE%' and is_delete = 'N'"
            , False)
        print(resource_levelInfos["count(*)"])
        # 第三步：断言
        self.assert_equal(0, test_resource_ListLevelInfoWithSubType.code)
        self.assert_equal("success", test_resource_ListLevelInfoWithSubType.message)
        self.assert_equal(resource_levelInfos["count(*)"], len(test_resource_ListLevelInfoWithSubType.data))



