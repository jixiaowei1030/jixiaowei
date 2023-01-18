# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_delClass:
    """
     删除班级接口
    """

    def test_delClass_success(self, eduOps_cli, new_class, data,setupdata):
        """
        删除班级成功
        case1:删除备用班级成功
        case2:删除普通班级成功
        """
        class_id, semester_id = new_class
        res = eduOps_cli.del_class(semesterId=str(semester_id), classId=str(class_id),mobile=setupdata["mobile"],
                                    password=setupdata["password"])
        assert res == data["assert"]["response"]

    def test_delClass_not_exist_ClassId(self, eduOps_cli, new_semester, data,setupdata):
        """
        case1:删除不存在的班级ID
        """
        semester_id = new_semester
        res = eduOps_cli.del_class(semesterId=str(semester_id), classId=data["classId"],mobile=setupdata["mobile"],
                                    password=setupdata["password"])
        print(res)
        assert res == data["assert"]["response"]
