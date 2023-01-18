# # -*- coding: utf-8 -*-
# """
# @author:yuanqi
# """
#
#
# class Test_post_add_abtestingConfig:
#     """
#     新增实验配置
#     """
#
#     def test_post_add_abtestingConfig_success(self, abtest_cli, data, setupdata):
#
#         res = abtest_cli.post_add_abtestingConfig(mobile=setupdata["mobile"],password=setupdata["password"])
#         assert res["code"] == data["assert"]["response"]["code"]
#         #assert res["data"] == data["assert"]["response"]["data"][""]