# @Time        : 2021/01/13
# @Author      : syr


import pytest
import allure
from utils.tools.base_test_case import BaseTestCase


@allure.story("喜课")
class TestUserResourceQuery(BaseTestCase):

    @pytest.mark.dev
    @allure.title("{data.casename}")
    def test_user_resource_query(self, xike_client, data, setupdata):
        """首页弹窗资源查询"""
        res = xike_client[0].get_user_resource_query(setupdata.mobile, setupdata.password, data.resourceType, data.platformType, data.appCode)
        self.assert_equal("success", res.message, res)

    if __name__ == 'main':
        pytest.main(["vs", "test_xkStep_feedbac.py"])