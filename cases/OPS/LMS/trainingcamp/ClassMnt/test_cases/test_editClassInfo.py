# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""
import pytest


class Test_editClassInfo:
    """
     编辑班级信息
    """

    def test_editClassInfo_success(self, trainingCamp_cli, new_class, data, setupdata):
        """
        desc:编辑班级信息成功
        case1: 编辑名称成功
        case2：修改成备用班成功 classTypeRef: 2
        case3：修改成普通班成功 classTypeRef: 1
        case4：修改人数上线成功 studentNumLimit
        case5：修改老师信息成功
        case6: 修改老师手机号和办公地点成功
        """
        class_id, semester_id = new_class
        res = trainingCamp_cli.edit_classInfo(semesterId=str(semester_id), classId=str(class_id),
                                              req_json=data["req_edit_class"],mobile=setupdata["mobile"],
                                                password=setupdata["password"])
        print(res)
        if "className" in data["assert"]["response"]:
            assert res["className"] == data["assert"]["response"]["className"]
        if "classTypeRef" in data["assert"]["response"]:
            assert res["classTypeRef"] == data["assert"]["response"]["classTypeRef"]
        if "studentNumLimit" in data["assert"]["response"]:
            assert res["studentNumLimit"] == data["assert"]["response"]["studentNumLimit"]
        if "teacherId" in data["assert"]["response"]:
            assert res["teacherId"] == data["assert"]["response"]["teacherId"]
            assert res["headTeacher"] == data["assert"]["response"]["headTeacher"]
            assert res["teacherQrCodeUrl"] == data["assert"]["response"]["teacherQrCodeUrl"]
        if "location" in data["assert"]["response"]:
            assert res["location"] == data["assert"]["response"]["location"]
            assert res["teacherMobile"] == data["assert"]["response"]["teacherMobile"]


