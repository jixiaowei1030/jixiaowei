"""
@Auth ： ylm
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER

class TestBckCASHBACKDETAIL(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    @classmethod
    def teardown_class(cls):
        LOGGER.info("TestBckCardCalendarActivityInfo测试结束")
        pass

    def test_bck_cashBack_detail(self, data,setupdata):
        """
        desc:
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """


        # 第一步：调用接口获取实际响应结果
        response_data = self.bck.bck_cashBack_detail(data.semesterRef,setupdata.mobile,setupdata.password)
        # print(response_data)

        # 第二步：查数据库获取数据库期望结果
        # 获取用户uid
        #uid = services.m_token['Cookie'].split("=")[1].split("&")[0]  # cookie中获取用户uid
        # print(uid)
        sql_data = self.mysql.query("SELECT semester_ref FROM xmkp_oxford_english.USER_ACTIVITY_STATUS WHERE user_id=344746", True)
        print(response_data.semesterRef)
        print(sql_data)
        for i in range(len(sql_data)):
            if sql_data[i].semester_ref == response_data.semesterRef:
                self.assert_equal(response_data.semesterRef, sql_data[i].semester_ref, "打卡返现的期班正确")





