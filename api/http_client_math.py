from utils.http.helper import get_math,post_m,get_m,post_math
from utils.http import BaseClient
import random


class HttpClientMath(BaseClient):

    @get_math('/xmkp-math-thinking/api/v5/entrance/annual')
    def annual(self,mobile,password):
        '''
        课程 AI年课首页
        '''

    @get_math('/xmkp-math-thinking/api/annual/userRecord/info')
    def user_record(self, type,mobile,password):
        '''
        获取用户记录
        '''

    @get_math('/xmkp-math-thinking/api/annual/lesson/missLessons')
    def miss_lessons(self,type,mobile,password):
        '''
        用户缺课
        '''

    @get_math('/xmkp-math-thinking/api/annual/lesson/info')
    def lesson_info(self,id,mobile,password):
        '''
        课程信息
        id: 课程id
        '''

    @get_math('/xmkp-math-thinking/api/annual/lesson/quarterLessons')
    def quarter_lessons(self,quarterId,mobile,password):
        '''
        季度课程列表
        '''


    @get_math('xmkp-math-thinking/api/annual/studyLog/report')
    def studylog_report(self, lessonId,mobile,password):
        '''
        学习报告
        '''

    @get_math('/xmkp-math-thinking/api/index/newStudy')
    def new_study(self,mobile,password):
        '''
        亲讲课
        '''

    @get_math('/xmkp-math-thinking/api/specialTraining/getInformation')
    def get_information(self,specialType,mobile,password):
        '''
        专项训练
        '''

    @get_m('/qqx/lesson/queryLessonPracticeList')
    def lesson_practicelist(self, albumId,lessonId,mobile,password):
        '''
        课程练习列表
        '''

    @get_m('/qqx/lessonStudy/queryAccount')
    def query_account(self,mobile,password):
        '''
        查询账户信息
        '''

    @get_m('/qqx/lessonStudy/getBalanceResult')
    def get_balanceresult(self,albumId,lessonId,mobile,password):
        '''
        获取结果
        '''

    @post_m('/qqx/lessonStudy/addUserStudyLogRecord',is_json_req=True)
    def studylog_record(self,albumId,userId,albumType,lessonId,practiceId,practiceSeq,startTime,endTime,
                        studyTime,result,beBalance,beFinalPracticeSeq,beFinalPractice,uniqueNo,mobile,password):
        '''
        用户学习日志记录
        '''

    @post_m('/qqx/lessonStudy/getDiamondNum', is_json_req=True)
    def get_diamondnum(self, albumId, lessonId, practiceId, practiceSeq, uniqueNo,mobile,password):
        '''
        获取钻石数量
        '''

    @post_m('/qqx/lessonStudy/addUserPracticeLogRecord', is_json_req=True)
    def practicelog_record(self, userId, albumId, lessonId, practiceId, uniqueNo,mobile,password):
        '''
        用户阶段练习日志记录
        '''


    @get_math('/xmkp-math-thinking/api/annual/lesson/quarterList')
    def quarter_list(self,mobile,password):
        '''
        所有季度课程列表
        '''

    @get_math('/xmkp-math-thinking/api/annual/lesson/weekList')
    def lesson_weeklist(self,type,mobile,password):
        '''所有周的课程列表'''

    @get_math('/xmkp-math-thinking/api/annual/phase/getReportList')
    def phase_get_report_list(self,mobile,password):
        '''阶段报告列表'''

    @get_math('/xmkp-math-thinking/api/annual/phase/getReport')
    def phase_get_report(self,qNum,mobile,password):
        '''阶段报告详情'''

    @get_math('/xmkp-math-thinking/api/annual/lesson/process')
    def lesson_process(self,type,mobile,password):
        '''当前课程'''

    @post_math('/xmkp-math-thinking/api/baby/addbabyDocument',is_json_req=True)
    def add_baby_document(self,birthday,sex,name,mobile,password):
        '''添加宝贝信息'''


if __name__ == '__main__':
    h=HttpClientMath()
    print('annual',h.user_record(3))