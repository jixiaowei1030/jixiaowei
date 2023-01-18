# -*- coding: utf-8 -*-
# @Time        : 2021/12/26
# @Author      : syr

import pytest
import allure
from utils.tools.base_test_case import BaseTestCase

@allure.story("喜课")

class TestXkChapteFeedback(BaseTestCase):

    def test_xkChapte_feedback_01(self, xike_client, data, setupdata):
        """新概念 完课反馈"""
        res = xike_client[0].get_xkChapter_feedback(setupdata.mobile, setupdata.password, data.campId, data.chapterId, data.stepId, data.businessType)
        print(res)
        self.assert_equal("success", res.message, res)

    def test_xkChapte_feedback_02(self, xike_client, data, setupdata):
        """书虫 完课反馈"""
        res = xike_client[0].get_xkChapter_feedback(setupdata.mobile, setupdata.password, data.campId, data.chapterId,
                                                     data.bookId, data.businessType)
        print(res)
        self.assert_equal("success", res.message, res)

    if __name__ == 'main':
        pytest.main(["vs", "test_xkChapte_feedback.py"])

