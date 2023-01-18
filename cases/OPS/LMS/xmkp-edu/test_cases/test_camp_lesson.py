"""
@author:sunguhua
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestLessonList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_lesson_list(self, data, setupdata):
        """
        desc:验证训练营ID=23下的课程列表字段
        steps:
        1、调接口后获得返回json
        2、查数据库获得查询数据
        3、断言1 2的值是否一致
        """
        lesson_list = self.ops.camp_lesson(data.timeStamp, setupdata.mobile ,setupdata.password)
        for i in range(0, len(lesson_list)):
            lesson_ref = lesson_list[i]["id"]
            edu_lesson = self.mysql.query("select * from xmkp_edu.EDU_LESSON where ID = %s" % lesson_ref)
            edu_lesson_camp_relation = self.mysql.query(
                "select * from xmkp_edu.EDU_LESSON_CAMP_RELATION where camp_ref = 23 AND lesson_ref = %s" % lesson_ref  )
            self.assert_equal(edu_lesson["lesson_title"], lesson_list[i]["lessonTitle"])
            self.assert_equal(edu_lesson_camp_relation["schedule_day"], lesson_list[i]["scheduleDay"])

