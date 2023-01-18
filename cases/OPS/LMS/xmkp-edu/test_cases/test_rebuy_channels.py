"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestRebuyChannels(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_rebuy_channels(self, data,setupdata):
        """
        desc:验证接口返回订单明细数据的渠道名list
        steps:
        1、调接口后获得返回json
        2、验证返回列表有渠道名-- "站内1级"
        """
        rebuy_channels_list = self.ops.rebuy_channels(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.mysql.query(
            "UPDATE  xmkp_edu.EDU_REBUY_ORDER set created_time =now() WHERE id = 2294016")

        # for i in range(0, len(rebuy_channels_list)):
        self.assert_equal((rebuy_channels_list[0]), "站内1级")
