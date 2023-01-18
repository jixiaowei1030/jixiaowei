from utils.http import BaseClient
from utils.http.helper import get_m, post_m


class HttpClientXike(BaseClient):
    """
    desc: 喜课
    """
    # 根据环节id获取内容
    @post_m("/xmkp-qqx-wrapper/bookworm/findStepContent", is_json_req=True)
    def find_step_content(self, stepId, mobile, password):
        """
        @param stepId：环节id
        @return:
        """
    # 根据章节id获取环节列表
    @post_m("/xmkp-qqx-wrapper/bookworm/findChapterStepList", is_json_req=True)
    def find_chapter_steplist(self, chapterId, mobile, password):
        """
        @param chapterId：章节id
        @return:
        """
    # 查看学习报告
    @post_m("/xmkp-qqx-wrapper/bookwormStudy/getUserStudyReport", is_json_req=True)
    def get_user_study_report(self, bookId, chapterId, stepId, mobile, password):
        """
        @param bookId：书本id
        @param chapterId：章节id
        @param stepId：环节id
        @return:
        """
    # 新增环节记录
    @post_m("/xmkp-qqx-wrapper/bookwormStudy/addUserStudyStepLogRecord", is_json_req=True)
    def add_user_study_step_log_record(self, chapterId, stepId, beFinalStep, bookId, mobile, password):
        """
        @param chapterId：章节id
        @param stepId：环节id
        @param beFinalStep：
        @param bookId：书本id
        @return:
        """
    # 新增学习记录
    @post_m("/xmkp-qqx-wrapper/bookwormStudy/addUserStudyLogRecord", is_json_req=True)
    def add_user_study_log_record(self, logType, studyTime, practiceId, stepId, content, contentLength, bookId, result, chapterId, startTime, endTime, selection, beAddPunchCardRecord, mobile, password):
        """
        @param logType：
        @param studyTime：
        @param practiceId：
        @param stepId：环节id
        @param content：
        @param contentLength：
        @param bookId：书本id
        @param result：
        @param chapterId：章节id
        @param startTime：
        @param endTime：
        @param selection：
        @param beAddPunchCardRecord：
        @return:
        """

    @get_m("/xmkp-xike-platform/xkChapter/queryImportantPoint")
    def query_important_point(self, bookId, chapterId, businessType, mobile, password):
        """
        本课重点(知识点汇总)查询
        :param bookId:
        :param chapterId:
        :param businessType:
        :return:
        """

    # 新概念环节反馈
    @get_m("/xmkp-xike-platform/xkStep/feedback", is_json_req=True)
    def get_xkStep_feedback(self, mobile, password, stepId, campId, chapterId, businessType):
        """
        @param stepId：环节id
        @param campId：训练营ID
        @param chapterId：章节id
        @param businessType：类id
        @return:
        """

    # 新概念完课反馈
    @get_m("/xmkp-xike-platform/xkChapter/feedback", is_json_req=True)
    def get_xkChapter_feedback(self, mobile, password, stepId, campId, chapterId, businessType):
        """
        @param stepId：环节id
        @param campId：训练营ID
        @param chapterId：章节id
        @param businessType：类id
        @return:
        """

    # 书虫 环节反馈
    @get_m("/xmkp-xike-platform/xkStep/feedback", is_json_req=True)
    def get_user_xkStep_feedback(self, mobile, password, bookId, campId, chapterId, businessType, stepId):
        """
        @param bookId：书id
        @param campId：训练营ID
        @param chapterId：章节id
        @param businessType：类id
        @param stepId: 环节ID
        @return:
        """

    # 书虫 完课反馈
    @get_m("/xmkp-xike-platform/xkChapter/feedback", is_json_req=True)
    def get_xkChapter_feedback(self, mobile, password, bookId, campId, chapterId, businessType):
        """
        @param bookId：书id
        @param campId：训练营ID
        @param chapterId：章节id
        @param businessType：类id
        @return:
        """


    # 查询用户兜底资源
    @get_m("/xmkp-xike-platform/football/query")
    def get_football_query(self, mobile, password, footBallKey):
        """
        @param footBallKey：xike.user.default.source
        """

    # 获取课前准备内容
    @get_m("/xmkp-xike-platform/prepare/getPrepareStepList")
    def get_prepare_stepList(self, mobile, password, businessType, campld, source ):
        """
        @param businessType：业务类型
        @param campid：训练营ID
        @param source：章节id
        """

    # 课程入口页查询
    @get_m("/xmkp-xike-platform/xkHome/homeInfo")
    def get_xkHome_homeInfo(self, mobile, password):
        """
        """

    # 喜客-首页定位(是否跳转课程页)
    @get_m("/xmkp-xike-platform/xkHome/isGotoLessonPage")
    def get_xkHome_isGotoLessonPage(self, mobile, password):
        """
        """

    # 【课程列表页】- 获取书册级别 下拉列表内容
    @get_m("/xmkp-xike-platform/book/resource/levelInfos")
    def get_resource_levelInfos(self, mobile, password, businessType):
        """
        @param businessType：业务类型(4-书虫 11-新概念)(Integer)
        """

    # 首页弹窗
    @post_m("/xmkp-xike-platform/user/resource/query", is_json_req=True)
    def get_user_resource_query(self, mobile, password, resourceType, platformType, appCode):
        """
        @param resourceType：资源类型(1:首页-banner;2:首页-弹窗;)
        @param platformType：平台类型(1:APP;2:小程序)
        @param appCode：app编码(1:奇奇学英语;2:绘本馆;3:喜课;4:新概念英语小程序)
        @return:
        """
    # 书虫点词查意
    @get_m("/xmkp-xike-platform/word/translate")
    def get_word_translate(self, mobile, password, word):
        """
        @param word:具体单词
        @return:
        """

    # 【级别切换页】- 通过级别查询获取级别及其下资源列表。新概念特殊添加体验营信息
    @get_m("xmkp-xike-platform/book/resource/levelBookResources")
    def get_resource_levelBookResources(self, mobile, password, businessType, levelCode):
        """
        @param businessType：业务类型(4-书虫 11-新概念)
        @param levelCode：级别code(String)
        """

    # 查询书籍章节信息
    @post_m("xmkp-qqx-wrapper/bookworm/findBookChapterInfo", is_json_req=True)
    def find_book_chapterinfo(self, mobile, password, chapterId, bookId):
        """
        查询书籍章节信息
        :param mobile:
        :param password:
        :param chapterId:
        :param bookId:
        :return:
        """

    # cms迁移-课程入口页查询
    @get_m("/xmkp-xike-platform/xkHome/cms/homeInfo")
    def get_xkHome_cms_homeInfo(self, mobile, password):
        """
        """

    # 【课程列表页】- 获取书册级别 下拉列表内容
    @get_m("/xmkp-xike-platform/book/resource/cms/levelInfos")
    def get_resource_cms_levelInfos(self, mobile, password, businessType):
        """
        @param businessType：业务类型(4-书虫 11-新概念)(Integer)
        """

    # 【课程列表页】- 获取书册级别 下拉列表内容 在主业务类型下, 区分子业务类型 当前仅支持 新概念业务类型下${书虫&新概念联合体验课 - 100}
    @post_m("/xmkp-xike-platform/book/resource/listLevelInfoWithSubType", is_json_req=True)
    def get_resource_listLevelInfoWithSubType(self, mobile, password, subBusinessType, businessType):
        """
        @param businessType：业务类型(4-书虫 11-新概念)(Integer)
        subBusinessType	子业务类型:100-书虫&新概念联合体验课
        """

    #【级别切换页】- 按级别获取课程列表 在主业务类型下, 区分子业务类型 当前仅支持 新概念业务类型下${书虫&新概念联合体验课 - 100}
    @post_m("xmkp-xike-platform/book/resource/listLevelResourceWithSubType", is_json_req=True)
    def get_resource_listLevelResourceWithSubType(self, mobile, password, subBusinessType, businessType, levelCode):
        """
        @param businessType：业务类型(4-书虫 11-新概念)(Integer)
        subBusinessType	子业务类型:100-书虫&新概念联合体验课
        levelCode cmslevelid
        """

    # 获取环节学习详情
    @post_m("xmkp-xike-platform/study/nce/step/detail", is_json_req=True)
    def nce_step_detail(self, mobile, password,  **kwargs ):
        """
        @param businessType：campId 训练营id
        requestType	1:App，2：wechat
        startDate 课程开始时间
        stepId
        """


    # 环节学习记录
    @post_m("xmkp-xike-platform/study/nce/step/progress/record", is_json_req=True)
    def step_progress_record(self, mobile, password, **kwargs):
        """
        @param studyStepId：环节id
        status	环节状态
        bpType 断点类型
        breakpoint 视频续学点
        requestType  1:App，2：wechat
        source
        """