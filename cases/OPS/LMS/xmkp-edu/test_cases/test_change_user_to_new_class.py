"""
@author:sunguhua
"""
import pytest
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestChangeUserToNewClass(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass
#此逻辑有更改
    # @pytest.mark.run(order=1)
    # def test_change_user_to_new_class(self, data,setupdata):
    #     """
    #     desc:验证接口返回的班级数据
    #     steps:
    #     1、调接口后对学员进行调班
    #     2、验证返回中是否347184调入新班级
    #     """
    #     user_info = self.mysql.query(
    #         "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 1093 and user_id = 347184")
    #     if user_info == {}:
    #         self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile ,setupdata.password)
    #         change_user_to_new_class = self.ops.change_user_to_new_class(data.timeStamp)
    #     else:
    #         change_user_to_new_class = self.ops.change_user_to_new_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     self.assert_equal(change_user_to_new_class['code'], 0)
    #     self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 69508 and user_id = 347184")
    #     self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query(
    #         "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 69508 or to_class_ref = 69508 and user_id = 347184")
    #
    # @pytest.mark.run(order=2)
    # def test_change_user_to_same_class(self, data,setupdata):
    #     """
    #     desc:验证接口返回的班级数据
    #     steps:
    #     1、调接口后对学员进行调班，调入同一班级
    #     2、验证返回
    #     """
    #     user_info = self.mysql.query(
    #         "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 69058 and user_id = 347184")
    #     if user_info == {}:
    #         self.ops.add_user_to_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #         change_user_to_new_class = self.ops.change_user_to_new_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     else:
    #         change_user_to_new_class = self.ops.change_user_to_new_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     self.assert_equal((change_user_to_new_class["data"]), '目标班级和所在班级一致')
    #     self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 69508 and user_id = 347184")
    #     self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query(
    #         "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 69508 or to_class_ref = 69508 and user_id = 347184")
    #
    # @pytest.mark.run(order=3)
    # def test_change_user_to_new_class_again(self, data,setupdata):
    #     """
    #     desc:验证接口返回的班级数据
    #     steps:
    #     1、调接口后对学员进行调班，学员已经调整过
    #     2、验证返回
    #     """
    #     user_info = self.mysql.query(
    #         "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 1093 and user_id = 347184")
    #     if user_info == {}:
    #         self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile ,setupdata.password)
    #         self.ops.change_user_to_new_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     else:
    #         self.ops.change_user_to_new_class(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     change_user_to_new_class = self.ops.change_user_to_new_class_1210(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     self.assert_equal((change_user_to_new_class["message"]), "对不起, 该用户(347184)已调整过班级, 无法再次调班")
    #     self.assert_equal(change_user_to_new_class['code'], -1)
    #     self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 69508 and user_id = 347184")
    #     self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 69508 and uid = 347184")
    #     self.mysql.query(
    #         "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 69508 or to_class_ref = 69508 and user_id = 347184")
    #
    # @pytest.mark.run(order=4)
    # def test_change_user_to_new_class_limit(self, data,setupdata):
    #     """
    #     desc:验证接口返回的班级数据
    #     steps:
    #     1、调接口后对学员进行调班，新班级已满
    #     2、验证返回
    #     """
    #     user_info = self.mysql.query(
    #         "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 1093 and user_id = 347184")
    #     if user_info == {}:
    #         self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile ,setupdata.password)
    #         change_user_to_new_class = self.ops.change_user_to_new_class_1210(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     else:
    #         change_user_to_new_class = self.ops.change_user_to_new_class_1210(data.timeStamp,setupdata.mobile ,setupdata.password)
    #     self.assert_equal(change_user_to_new_class['message'], '目标班级(1210)人数已达上限, 请上调班级人数上限后重试')
    #     self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 1210 and user_id = 347184")
    #     self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 1210 and uid = 347184")
    #     self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 1210 and uid = 347184")
    #     self.mysql.query(
    #         "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 1210 or to_class_ref = 1210 and user_id = 347184")
    #
    @pytest.mark.run(order=5)
    def test_change_user_to_new_class_different_semester(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后对学员进行调班,同camp不同semester
        2、验证返回
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 1093 and user_id = 347184")
        if user_info == {}:
            self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile ,setupdata.password)
            change_user_to_new_class = self.ops.change_user_to_new_class_different_semester(data.timeStamp,setupdata.mobile ,setupdata.password)
        else:
            change_user_to_new_class = self.ops.change_user_to_new_class_different_semester(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal(change_user_to_new_class['code'], -1)
        self.assert_equal(change_user_to_new_class['message'], '在 536 期中找不到用户 347184')
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 878 and user_id = 347184")
        self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 878 and uid = 347184")
        self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 69508 and uid = 347184")
        self.mysql.query(
            "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 878 or to_class_ref = 878 and user_id = 347184")

    @pytest.mark.run(order=6)
    def test_change_user_to_new_class_different_camp(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后对学员进行调班,不同camp
        2、验证返回
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where class_ref = 1093 and user_id = 347184")
        if user_info == {}:
            self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile ,setupdata.password)
            change_user_to_new_class = self.ops.change_user_to_new_class_different_camp(data.timeStamp,setupdata.mobile ,setupdata.password)
        else:
            change_user_to_new_class = self.ops.change_user_to_new_class_different_camp(data.timeStamp,setupdata.mobile ,setupdata.password)
        self.assert_equal(change_user_to_new_class['code'], -1)
        self.assert_equal(change_user_to_new_class['message'], '在 773 期中找不到用户 347184')
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE WHERE class_ref = 69508 and user_id = 347184")
        self.mysql.query("delete from xmkp_edu.EDU_GROUP_CODE_RECALL WHERE class_id = 69508 and uid = 347184")
        self.mysql.query("delete from xmkp_edu.PRE_JOIN_CLASS_RECORD WHERE class_id = 69508 and uid = 347184")
        self.mysql.query(
            "delete from xmkp_edu.CHANGE_CLASS_RECORD WHERE from_class_ref = 69508 or to_class_ref = 69508 and user_id = 347184")
