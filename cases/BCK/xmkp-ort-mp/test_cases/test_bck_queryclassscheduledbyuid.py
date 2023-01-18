"""
@Auth：tiannana
"""
import re

from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckQueryClassScheduledByUid(BaseTestCase):

    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    @classmethod
    def teardown_class(cls):
        LOGGER.info("TestBckSpellingList测试结束")
        pass

    def test_query_class_scheduled_by_uid(self, data,setupdata):
        """
        desc:获取登录用户课表信息
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言
        """

        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        print(user_id)

        list1 = self.bck.query_class_scheduled_by_uid(data.pageSize, data.sort,setupdata.mobile,setupdata.password)
        print(list1)
        list_info = self.mysql.query("SELECT * FROM xmkp_edu.EDU_LESSON WHERE id=244 AND is_deleted=0", True)
        # print(list_info)
        #
        # print(list1.data.list[0].lessons[1].title)
        # print(list_info[0].lesson_title)

        self.assert_equal(list1.data.list[0].lessons[1].title, list_info[0].lesson_title)





