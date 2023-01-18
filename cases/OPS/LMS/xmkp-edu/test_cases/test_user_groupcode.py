"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestUserGroupCode(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_user_list_by_mobile(self, data,setupdata):
        """
        desc:通过手机号获取学员信息
        steps:
        1、调接口后获得返回json
        2、验证返回中是否包含347184
        """
        user_list = self.ops.user_groupcode(data.timeStamp, data.mobile,setupdata.mobile ,setupdata.password)
        data_from_classmate = self.mysql.query(
            "SELECT * FROM xmkp_edu.EDU_CLASSMATE WHERE user_id = 347184 and class_ref = 1503", True)
        for i in range(0, len(user_list["groupCodeInfo"])):
            if user_list["groupCodeInfo"][i]["tradeOrderNo"] == str(data_from_classmate["order_no"]):
                self.assert_equal((user_list["groupCodeInfo"][i]["uid"]), data_from_classmate["user_id"])

    def test_user_list_by_uid(self, data,setupdata):
        """
        desc:通过uid获取学员信息
        steps:
        1、调接口后获得返回json
        2、验证返回中是否包含347184
        """
        user_list = self.ops.user_groupcode(data.timeStamp, data.uid,setupdata.mobile ,setupdata.password)
        data_from_classmate = self.mysql.query(
            "SELECT * FROM xmkp_edu.EDU_CLASSMATE WHERE user_id = 347184 and class_ref = 1503", True)
        for i in range(0, len(user_list["groupCodeInfo"])):
            if user_list["groupCodeInfo"][i]["tradeOrderNo"] == str(data_from_classmate["order_no"]):
                self.assert_equal((user_list["groupCodeInfo"][i]["uid"]), data_from_classmate["user_id"])


    def test_user_list_by_order_no(self, data,setupdata):
        """
        desc:通过订单号获取学员信息
        steps:
        1、调接口后获得返回json
        2、验证返回中是否包含347184
        """
        user_list = self.ops.user_groupcode(data.timeStamp, data.tradeOrderNo,setupdata.mobile ,setupdata.password)
        data_from_classmate = self.mysql.query(
            "SELECT * FROM xmkp_edu.EDU_CLASSMATE WHERE user_id = 347184 and class_ref = 1503", True)
        for i in range(0, len(user_list["groupCodeInfo"])):
            if user_list["groupCodeInfo"][i]["tradeOrderNo"] == str(data_from_classmate["order_no"]):
                self.assert_equal((user_list["groupCodeInfo"][i]["uid"]), data_from_classmate["user_id"])
