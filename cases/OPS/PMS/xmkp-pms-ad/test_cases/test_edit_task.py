# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""

class Test_edit_task:
    """
    编辑投放业务
    """
    def test_edit_task_success(self, ad_ser, data,setupdata):
        """
        desc:编辑投放业务成功
        1.调用创建投放业务接口，创建新投放业务
        2.调用修改投放业务接口成功，修改新投放业务
        3.验证返回的状态码为200和返回参数正确
        4.调用删除投放业务接口，删除新投放业务
        """
        re = ad_ser.post_task(data["new"]["taskName"], data["new"]["businessType"],
                               data["new"]["vendorType"], data["new"]["encryptMethod"],
                               data["new"]["userGroupId"], data["new"]["updateFrequency"],
                               data["new"]["remark"],mobile=setupdata["mobile"],password=setupdata["password"])
        res = ad_ser.edit_task(re["data"]["id"], data.taskName, data.businessType,
                               data.vendorType, data.encryptMethod,
                               data.userGroupId, data.updateFrequency,
                               data.remark,mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]
        ad_ser.delete_task(taskId=str(re["data"]["id"]),mobile=setupdata["mobile"],password=setupdata["password"])
