"""
作者：shiling
"""

from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
from utils.log import LOGGER


class TestMSteps(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")


    def teardown_class(cls):
        LOGGER.info("TestMSteps测试结束")

    def test_m_steps(self, data,setupdata):
        """
        desc:获取课堂环节页信息
        step1:请求接口拿到返回信息
        step2:查询数据库
        step3:断言1.2
        """
        steps1 = self.bck.m_steps(data.lessonId, data.campRef,setupdata.mobile,setupdata.password)

        step_info = self.mysql.query("SELECT * FROM xmkp_edu.EDU_STEP WHERE lesson_id=674 AND is_deleted=0 ", True)
        self.assert_equal(step_info[3]["step_type"], steps1.steps[3].type, "steps类型为4")
        self.assert_equal(step_info[3]["id"], steps1.steps[3].id, "id")
        self.assert_equal(step_info[0]["step_type"], steps1.steps[0].type, "steps类型3")
        self.assert_equal(step_info[0]["id"], steps1.steps[0].id, "id")
        self.assert_equal(step_info[1]["step_type"], steps1.steps[1].type, "steps类型6")
        self.assert_equal(step_info[1]["id"], steps1.steps[1].id, "id")
        self.assert_equal(step_info[2]["step_type"], steps1.steps[2].type, "steps类型5")
        self.assert_equal(step_info[2]["id"], steps1.steps[2].id, "id")







