# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""
import pytest


class Test_classMove:
    """
     班级移动接口
    """

    def test_classMove_success(self, eduOps_cli, new_class, data, setupdata):
        """
        desc:班级成功
        case1:班级向下移动成功
        case2：班级向上移动成功
        """
        class_id, semester_id = new_class
        res = eduOps_cli.move_class(classId=str(class_id), operationId=data["operationId"], mobile=setupdata["mobile"],
                                    password=setupdata["password"])
        print(res)
        assert res == data["assert"]["response"]
