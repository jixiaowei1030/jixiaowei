# -*- coding: utf-8 -*-
# @Time        : 2021/12/20
# @Author      : syr

import pytest
import allure
from utils.tools.base_test_case import BaseTestCase


@allure.story("喜课")
class TestXkStepFeedback(BaseTestCase):
    @allure.title("{data.casename}")
    def test_xkStep_feedback_01(self, xike_client, data, setupdata):
        """"新概念环节反馈知识点非空"""

        res = xike_client[0].get_xkStep_feedback(setupdata.mobile, setupdata.password, data.campId, data.chapterId, data.stepId, data.businessType)
        print(res)
        self.assert_equal("success", res.message, res)

    @allure.title("{data.casename}")
    def test_xkStep_feedback_02(self, xike_client, setupdata, data):
        """新概念环节反馈知识点为空"""

        res = xike_client[0].get_xkStep_feedback(setupdata.mobile, setupdata.password, data.campId, data.chapterId,
                                                  data.stepId, data.businessType)
        print(res)
        self.assert_equal("success", res.message, res)


if __name__ == 'main':
        pytest.main(["vs", "test_xkStep_feedbac.py"])