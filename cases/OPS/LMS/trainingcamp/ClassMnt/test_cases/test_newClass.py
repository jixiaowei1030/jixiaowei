# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_newClass:
    """
     新建班级接口
    """

    def test_newClass_success(self, trainingCamp_cli, new_semester, data, del_class,setupdata):
        """
        desc:新建班级成功
        case1：新建备用班成功 classTypeRef: 2
        case2：新建普通班成功 classTypeRef: 1
        """
        semester_id = new_semester
        semesterIds, classIds = del_class
        semesterIds.append(semester_id)
        res = trainingCamp_cli.new_class(req_json=data["req_new_class"], semesterId=str(semester_id),
                                         mobile=setupdata["mobile"],password=setupdata["password"])
        assert res["semesterRef"] == semester_id
        assert res["headTeacher"] == data["assert"]["response"]["headTeacher"]
        assert res["teacherQrCodeUrl"] == data["assert"]["response"]["teacherQrCodeUrl"]
        assert res["studentNum"] == data["assert"]["response"]["studentNum"]
        assert res["studentNumLimit"] == data["assert"]["response"]["studentNumLimit"]
        assert res["teacherId"] == data["assert"]["response"]["teacherId"]
        assert res['className'] == data["assert"]["response"]["className"]
        assert res["teacherMessageUrl"] == data["assert"]["response"]["teacherMessageUrl"]
        assert res['tagDeleteDays'] == data["assert"]["response"]["tagDeleteDays"]
        classIds.append(res["id"])


