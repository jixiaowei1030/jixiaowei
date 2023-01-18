"""
@Auth：tiannana
"""
import re

from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckSpellingList(BaseTestCase):

    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    @classmethod
    def teardown_class(cls):
        LOGGER.info("TestBckSpellingList测试结束")
        pass

    def test_spelling_list(self, data,setupdata):
        """
        desc:获取登录用户spelling体验课列表信息
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """

        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        print(user_id)

        list1 = self.bck.spelling_list(data.pageNum, data.pageSize, data.productId,setupdata.mobile,setupdata.password)
        print(list1)
        list_info = self.mysql.query("SELECT * FROM xmkp_edu.EDU_CLASSMATE WHERE user_id=344746 AND is_deleted=0", True)
        print(list_info)
        print(list1.data.courses[0].productRef)
        print(list_info[0].product_ref)

        self.assert_equal(list1.data.courses[0].productRef, list_info[0].product_ref,"product_ref")





