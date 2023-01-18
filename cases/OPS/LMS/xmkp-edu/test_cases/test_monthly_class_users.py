"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestMonthlyClassUsers(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_monthly_class_users(self, data,setupdata):
        """
        desc:验证接口返回获取订单明细数据
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        response_list = self.ops.monthly_class_users(
            data.classId,
            data.currentPage,
            data.pageSize,
            data.searchContent,
            data.hasFugou,
            data.notDakaDay,
            data.studyDay,
            data.studyStatus,setupdata.mobile ,setupdata.password
        )

        self.assert_equal(response_list["success"], 0)
        self.assert_equal(response_list["code"], 0)
        self.assert_equal(response_list["message"], "操作成功")

