"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestCacsiPageviewSave(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_cacsi_pageview_save(self, data,setupdata):
        """
        desc:验证接口返回获取订单明细数据
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        response_list = self.ops.cacsi_pageview_save(data.menuId, setupdata.mobile, setupdata.password)
        self.assert_equal(200, response_list["code"])
        self.assert_equal("success", response_list["message"])

    def test_cacsi_pageview_save_417(self, data,setupdata):
        """
        desc:验证接口返回获取订单明细数据
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        response_list = self.ops.cacsi_pageview_save(data.menuId,setupdata.mobile, setupdata.password)
        self.assert_equal(417, response_list["code"])
        self.assert_equal("菜单不存在", response_list["message"])
