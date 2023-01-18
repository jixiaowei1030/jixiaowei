# -*- coding: utf-8 -*-
# @Time        : 2022/01/21
# @Author      : syr

import pytest
from utils.tools.base_test_case import BaseTestCase

class TestWordTranslate(BaseTestCase):
    def test_word_translate(self, xike_client, setupdata, data):
        response = xike_client[0].get_word_translate(setupdata.mobile, setupdata.password, data.word)
        print(response)
        self.assert_equal("success", response.message, response)



    if __name__ == 'main':
        pytest.main(["vs", "test_word_translat3e.py"])

