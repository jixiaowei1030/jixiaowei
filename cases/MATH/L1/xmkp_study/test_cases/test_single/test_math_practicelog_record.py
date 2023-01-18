"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L1")
class TestMathPracticelogRecord(BaseTestCase):
    """
                        desc:验证阶段练习日志记录的查询
                        steps:
                        1、查询获取学习记录的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2msg为success，
                                   2.3数据库添加一条记录

                        """
    @allure.title("{data.case_name}")
    def test_math_practicelog_record(self,math_client,setupdata,data):
        """L1用户阶段学习日志记录"""
        record_count_before=math_client[1].query("select count(*) from goodxs.study_practice_log_record where user_id='%s' and album_id='%s' and lesson_id='%s' and practice_id='%s' and unique_no='%s'"%(data.userId,data.albumId,data.lessonId,data.practiceId,data.uniqueNo),False)
        practicelog_record=math_client[0].practicelog_record(data.userId,data.albumId,data.lessonId,data.practiceId,data.uniqueNo,setupdata.mobile,setupdata.password)
        record_count_after = math_client[1].query(
            "select count(*) from goodxs.study_practice_log_record where user_id='%s' and album_id='%s' and lesson_id='%s' and practice_id='%s' and unique_no='%s'" % (
            data.userId, data.albumId, data.lessonId, data.practiceId, data.uniqueNo), False)
        self.assert_equal(0,practicelog_record.code)
        self.assert_equal("success",practicelog_record.message)
        self.assert_equal(1,record_count_after["count(*)"]-record_count_before["count(*)"])
