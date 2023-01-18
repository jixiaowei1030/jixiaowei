"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestGenClassDiamondRank(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_gen_class_diamond_rank(self, data,setupdata):
        """
        desc:验证接口返回获取订单明细数据
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        response_list = self.ops.gen_class_diamond_rank(
            data.classRefs,
            data.beginDate,
            data.endDate,
            data.opsId,setupdata.mobile ,setupdata.password
        )

        self.assert_equal(response_list["id"], None)
        self.assert_equal(response_list["classRefs"], None)

