# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""
from utils.tools.base_test_case import BaseTestCase

class Test_delete_task(BaseTestCase):
    """
    删除投放业务
    """

    # @classmethod
    # def setup_class(cls):
    #     cls.setup_data = getattr(cls, "setup_data")

    def test_delete_task_success(self, ad_ser, data, setupdata):

        """
        desc:删除投放业务成功
        steps:
        1、调新增投放业务接口成功
        2、调用删除投放业务接口，删除新增投放业务
        3、验证返回的状态码为200和返回参数正确
        """
        # print(setupdata["mobile"])
        re = ad_ser.post_task(data.taskName, data.businessType,
                              data.vendorType, data.encryptMethod,
                              data.userGroupId, data.updateFrequency,
                              data.remark,mobile=setupdata["mobile"],password=setupdata["password"])
        res = ad_ser.delete_task(taskId=str(re["data"]["id"]))
        assert res == data["assert"]["response"]
