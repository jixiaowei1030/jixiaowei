"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestRebuy(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_rebuy_channel(self, data,setupdata):
        """
        desc:验证接口返回获取订单明细数据
        steps:
        1、调接口后获得返回json
        2、验证返回
        """
        rebuy_list = self.ops.rebuy(data.timeStamp, data.pageSize, data.page, data.channel, "",setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_edu.EDU_REBUY_ORDER set created_time =now() WHERE id = 2294016")
        edu_rebuy_list =self.mysql.query(
            "select * from xmkp_edu.EDU_REBUY_ORDER  WHERE id = 2294016")

        for i in range(0, len(rebuy_list.data)):
            self.assert_equal((edu_rebuy_list["id"]), rebuy_list.data[i]["id"])
            self.assert_equal(edu_rebuy_list["user_id"], rebuy_list.data[i]["userId"])
            self.assert_equal(edu_rebuy_list["order_no"], rebuy_list.data[i]["orderNo"])


