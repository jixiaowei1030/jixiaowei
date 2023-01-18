# # -*- coding: utf-8 -*-
# """
# @author:yuanqi
# """
#
# class Test_get_abtestConfig:
#     """
#     查询实验配置详情
#     """
#
#     def test_get_abtestConfig_success(self, abtest_cli, data, new_abtest, setupdata):
#         """
#         desc:成功获取所属实验配置详情
#         1.调用获取所属实验配置详情接口成功
#         2.验证返回的状态码为200和返回参数正确
#         """
#
#         testingCode,t = new_abtest
#         res = abtest_cli.get_abtestingConfig_detail(testingCode=testingCode,mobile=setupdata["mobile"],password=setupdata["password"])
#         assert res["code"] == data["assert"]["response"]["code"]
#         assert res["data"]["testingName"] == data["assert"]["response"]["data"]["testingName"] % t
#         assert res["data"]["systemName"] == data["assert"]["response"]["data"]["systemName"]
#         assert res["data"]["businessType"] == data["assert"]["response"]["data"]["businessType"]
#         assert res["data"]["testingScope"] == data["assert"]["response"]["data"]["testingScope"]
#         assert res["data"]["mechanismUpdated"] == data["assert"]["response"]["data"]["mechanismUpdated"]
#         #assert res["data"]["abtestGroups"]["isDefault"][0] == true