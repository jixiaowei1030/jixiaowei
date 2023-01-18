"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L1")
class TestMathStudylogRecord(BaseTestCase):
    """
                    desc:验证学习记录的查询
                    steps:
                    1、查询获取学习记录的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为成功，
                               2.3数据库添加一条记录

                    """
    @allure.title("{data.case_name}")
    def test_math_studylog_record(self,math_client,setupdata,data):
        """L1用户学习日志记录"""
        if data.result:
            result=1
        else:
            result=0
        record_count_before=math_client[1].query("select count(*) from goodxs.study_user_study_log_record where user_id= '%s' and practice_id='%s' and album_id='%s' and result='%s' and album_type='%s'"%(data.userId,data.practiceId,data.albumId,result,data.albumType),False)
        studylog_record=math_client[0].studylog_record(data.albumId,data.userId,data.albumType,data.lessonId
                                                       ,data.practiceId,data.practiceSeq,data.startTime,data.endTime
                                                       ,data.studyTime,data.result,data.beBalance,data.beFinalPracticeSeq
                                                       ,data.beFinalPractice,data.uniqueNo,setupdata.mobile,setupdata.password)
        record_count_after = math_client[1].query("select count(*) from goodxs.study_user_study_log_record where user_id= '%s' and practice_id='%s' and album_id='%s' and result='%s' and album_type='%s'" % (data.userId, data.practiceId, data.albumId, result, data.albumType), False)
        self.assert_equal(0,studylog_record.code)
        self.assert_equal("success",studylog_record.message)
        self.assert_equal(1,record_count_after["count(*)"]-record_count_before["count(*)"])
