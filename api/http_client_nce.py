
from utils.http import BaseClient
from utils.http.helper import get_m, post_m

"""
新概念接口
"""
class HttpClientNce(BaseClient):

    @get_m("/xmkp-nce/lesson/info")
    def lesson_info(self, id, campRef, mobile, password):
        """
        获取课程详情
        """

    @post_m("/xmkp-nce/wechat/nceuser/info")
    def nceuser_info(self, mobile, password):
        """

        获取用户信息
        """

    @get_m("/xmkp-nce/step/list")
    def step_list(self, lessonRef, campRef, mobile, password):
        """
        获取环节列表信息（废弃）
        """

    @post_m("/xmkp-nce/lesson/list", is_json_req=True)
    def lesson_list(self, pageNum, pageSize, mobile, password):
        """
        获取课程列表（废弃）
        """

    @get_m("/xmkp-nce/step/info")
    def step_info(self, lessonRef, stepType, id, campRef, mobile, password):
        """
        获取环节信息（废弃）
        """

    @post_m("/xmkp-nce/nceUser/update2", is_json_req=True)
    def nceuser_update2(self, nickName, sex, id, birthDate, userId, mobile, password):
        """
        更新用户信息
        """

    @get_m("/xmkp-nce/wechat/course/list")
    def course_list(self,mobile,password):
        """
        获取用户训练营列表数据
        """

    # 接口已废弃
    # @post_m("/xmkp-nce/nceUser/update", is_json_req=True)
    # def nceuser_relogin(self, loginType, mobile, password):
    #     """
    #
    #     用户登陆后信息更新
    #     """

    @post_m("/xmkp-nce/wechat/course/lesson/page", is_json_req=True)
    def lesson_page(self, pageNum, pageSize, mobile, password):
        """
        课程列表页
        """

    @post_m("/xmkp-nce/wechat/course/lesson/step/list", is_json_req=True)
    def lesson_step_list(self, campId, lessonId, mobile, password):
        """
        课程环节列表
        """

    @post_m("/xmkp-nce/wechat/study/lesson/step/detail", is_json_req=True)
    def lesson_step_detail(self, stepId, campId,startDate, mobile, password):
        """
        学习环节详情
        """

    @post_m("/xmkp-nce/wechat/course/lesson/query", is_json_req=True)
    def lesson_query(self, campId, lessonId, mobile, password):
        """
        课程进度查询接口
        """

    #ok
    @post_m("/xmkp-nce/wechat/study/lesson/exercises/record", is_json_req=True)
    def exercises_record(self, campRef, lessonRef, stepRef, exercisesRef, originAudioUrl, type, text, isCorrrect,
                         score, audioUrl, duration, tryTimes, doTimes, isCompleted, answerContent, mobile, password):
        """
        用户学习环节做题记录
        """

    @post_m("/xmkp-nce/wechat/study/lesson/formative/detail", is_json_req=True)
    def formative_detail(self, lessonId, campId, startDate, mobile, password):
        """
        进入阶段测试课程详情
        """

    @post_m("/xmkp-nce/wechat/study/lesson/formative/report", is_json_req=True)
    def formative_report(self, lessonId, campId, startDate, mobile, password):
        """
        阶段测试报告页
        """

    # ok
    @post_m("/xmkp-nce/wechat/study/lesson/formative/doexer/list", is_json_req=True)
    def doexer_list(self, batchId, mobile, password):
        """
        阶段测试答题列表
        """

    @get_m("/xmkp-nce/guidance/showguide")
    def showguide(self, guideType, mobile, password):
        """
        新手引导
        """

    @post_m("/xmkp-nce/wechat/study/lesson/step/progress/record", is_json_req=True)
    def progress_record(self, studyStepId, bpType, status, breakpoint, mobile, password, bpExerciseId=None, batchId=None):
        """
        课程进度断点记录接口
        """

    @post_m("/xmkp-nce/wechat/study/lesson/step/duration/record", is_json_req=True)
    def exercises_duration_record(self, studyStepId, duration, mobile, password):
        """
        课程学习环节学习时长手动记录
        """

    @post_m("/xmkp-nce/wechat/study/lesson/step/card/record", is_json_req=True)
    def step_card_record(self, studyStepId, cardId, stepId, mobile, password):
        """
        学习环节卡片状态记录
        """

    @post_m("/xmkp-nce/wechat/nceuser/book/list", is_json_req=True)
    def nceuser_book_list(self, mobile, password):
        """
        获取用户书册列表信息
        """

    @post_m("/xmkp-nce/wechat/nceuser/view/white/open", is_json_req=True)
    def view_white_open(self, mobile, password):
        """
        判断白名单功能是否开启
        """

    @post_m("/xmkp-nce/wechat/nceuser/view/iswhite", is_json_req=True)
    def view_iswhite(self, mobile, password):
        """
        判断是否是白名单用户
        """

    @post_m("/xmkp-nce/wechat/nceuser/edit", is_json_req=True)
    def nceuser_edit(self, grade, mobile, password):
        """
        编辑用户班级基础信息，如某个年级
        """

    @post_m("/xmkp-nce/wechat/camp/experience/lesson/list", is_json_req=True)
    def experience_lesson_list(self, campId, bookType, mobile, password):
        """
        获取某册书课程列表，训练营id，书册号
        """

    @post_m("/xmkp-nce/wechat/camp/last/study/lesson", is_json_req=True)
    def last_study_lesson(self, campId, bookType, mobile, password):
        """
        获取上次学习的正式课程
        """

    @post_m("/xmkp-nce/wechat/camp/formal/lesson/page", is_json_req=True)
    def formal_lesson_page(self, campId, bookType, pageNum, pageSize, mobile, password):
        """
        获取锚定课程列表信息
        """

    @post_m("/xmkp-nce/wechat/camp/lesson/step/list", is_json_req=True)
    def lesson_step_list(self, campId, lessonId, mobile, password):
        """
        获取课程环节页
        """

    # ok
    @post_m("/xmkp-nce/wechat/study/lesson/exercises/batch/record", is_json_req=True)
    def exercises_batch_record(self, batchId, exerId, exerIndex, isAnswered, isCorrect, isCompleted, score, doTimes,
                         tryTimes, answerContent, mobile, password):
        """
        提交阶段测试题
        """
