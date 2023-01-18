# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_voiceComments:
    """
     开启语音点评接口
    """

    def test_enable_voiceComments(self, eduOps_cli, new_semester, data, setupdata):
        """
        启用语音点评成功
        case1:启用学期语音点评成功
        case2：重复启用语音点评成功
        """
        semester_id = new_semester
        res = eduOps_cli.enable_voiceComments(semesterId=str(semester_id),
                                              mobile=setupdata["mobile"], password=setupdata["password"])
        print(res)
        assert res == data["assert"]["response"]

    def test_enable_voiceComments_repeat(self, eduOps_cli, new_semester, data,setupdata):
        """
        启用语音点评成功
        case1:启用学期语音点评成功
        case2：重复启用语音点评成功
        """
        semester_id = new_semester
        res = eduOps_cli.enable_voiceComments(semesterId=str(semester_id),
                                              mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]
        res = eduOps_cli.enable_voiceComments(semesterId=str(semester_id),
                                              mobile=setupdata["mobile"],password=setupdata["password"])
        print(res)
        assert res == data["assert"]["response"]

    def test_voiceComments_verify_params(self, eduOps_cli, data,setupdata):
        """
        启用语音点评成功
        case:验证参数是否必填
        """
        res = eduOps_cli.enable_voiceComments(semesterId=data["param"],
                                              mobile=setupdata["mobile"],password=setupdata["password"])
        print(res)
        assert res == data["assert"]["response"]
