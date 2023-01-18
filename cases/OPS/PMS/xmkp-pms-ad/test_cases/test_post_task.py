# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""

class Test_post_task:
    """
    新增投放业务
    """

    def test_post_task_success(self, ad_ser, data,setupdata):
        """
        desc:新增投放业务成功
        steps:
        1、调新增投放业务接口成功
        2、验证返回的状态码为200和返回参数正确
        3、调用删除投放业务接口，删除新增投放业务
        """
        res = ad_ser.post_task(data.taskName, data.businessType,
                               data.vendorType, data.encryptMethod,
                               data.userGroupId, data.updateFrequency,
                               data.remark,mobile=setupdata["mobile"],password=setupdata["password"])
        assert res["success"] == data["assert"]["response"]["success"]
        assert res["code"] == data["assert"]["response"]["code"]
        assert res["message"] == data["assert"]["response"]["message"]
        assert res["data"]["businessType"] == data["assert"]["response"]["data"]["businessType"]
        assert res["data"]["taskName"] == data["assert"]["response"]["data"]["taskName"]
        assert res["data"]["vendorType"] == data["assert"]["response"]["data"]["vendorType"]
        assert res["data"]["encryptMethod"] == data["assert"]["response"]["data"]["encryptMethod"]
        assert res["data"]["userGroupId"] == data["assert"]["response"]["data"]["userGroupId"]
        assert res["data"]["vendorGroupId"] == data["assert"]["response"]["data"]["vendorGroupId"]
        assert res["data"]["updateFrequency"] == data["assert"]["response"]["data"]["updateFrequency"]
        assert res["data"]["taskStatus"] == data["assert"]["response"]["data"]["taskStatus"]
        assert res["data"]["remark"] == data["assert"]["response"]["data"]["remark"]
        assert res["data"]["isDeleted"] == data["assert"]["response"]["data"]["isDeleted"]
        assert res["data"]["creatorId"] == data["assert"]["response"]["data"]["creatorId"]
        assert res["data"]["creator"] == data["assert"]["response"]["data"]["creator"]
        ad_ser.delete_task(taskId=str(res["data"]["id"]),mobile=setupdata["mobile"],password=setupdata["password"])