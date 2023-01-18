"""
@Auth ： ylm
"""

import re

from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestBckCardCalendarActivityInfo(BaseTestCase):

    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    @classmethod
    def teardown_class(cls):
        LOGGER.info("TestBckCardCalendarActivityInfo测试结束")
        pass

    def test_card_calendar_activity_info(self, data,setupdata):
        """
        desc:
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """

        # 第一步：调用接口获取实际响应结果
        list1 = self.bck.bck_card_calendar_activity_info(data.t,setupdata.mobile,setupdata.password)
        # print(list1)
        data_semesterRef = list1.entitiesList[0].semesterRef

        # 第二步：查数据库获取数据库期望结果
        # 获取用户id
        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        # print(user_id)

        #查找数据库
        list_info = self.mysql.query("SELECT * FROM xmkp_oxford_english.USER_ACTIVITY_STATUS WHERE user_id=344746 LIMIT 0,1000", True)
        data_sql_semesterRef = list_info[0].semester_ref

        #第三步断言
        self.assert_equal(data_semesterRef, data_sql_semesterRef, "打卡返现期班正确")

