# -*- coding: utf-8 -*-

from abc import ABC
from utils.http.helper import get_m, get_daka, get_ops, post_m, post_daka, post_ops
from utils.http import BaseClient


class HttpClientBck(BaseClient):

    @get_daka("/ort/front/products")
    def products(self,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/businessType/1")
    def camp_businesstype_one(self, timeStamp,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/businessType/2")
    def camp_businesstype_two(self, timeStamp,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/businessType/4")
    def camp_businesstype_four(self, timeStamp,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/23/lesson")
    def camp_lesson(self, timeStamp,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/21/presale")
    def camp_presale(self, timeStamp,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/camp/21/semester/search")
    def camp_semester(self, timeStamp, index, size, campId,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/semester/595/class/search")
    def camp_class(self, timeStamp, page, pageSize, sum, numCondition,mobile, password):
        """"""

    @get_ops("/eduOps/dev/memberInClass/1210/search")
    def camp_member_in_class(self, timeStamp, index, size, numCondition,mobile, password):
        """"""

    @get_ops("/eduOps/api/v1/21/presalePages/new")
    def camp_presale_pages(self, timeStamp,currentPage,pageSize,mobile, password):
        """"""

    @get_m("/ort/front/lesson/1/withFreeCampAndLevel/v3")
    def camp_with_free_camp_and_level(self, pageNum, pageSize, productId,mobile, password):
        """"

        """

    @get_m("/ort/front/app/lesson/spelling/list")
    def spelling_list(self, pageNum, pageSize, productId,mobile, password):
        """"

        """

    #@get_tankhand("/ort/front/antiTheft/lesson/252/report")
    #def study_report(self, device, campRef,productId, lessonId):
        """"

        """

    @get_m("/ort/front/user/current/diamond")
    def diamond(self,mobile, password):
        """"
        钻石

        """

    @get_m("/ort/front/lesson/queryClassScheduledByUid/v1")
    def query_class_scheduled_by_uid(self, pagesize, sort,mobile, password):
        """"

        """

    @get_daka("/ort/cashBack/detail")
    def cash_back_detail(self, semesterRef,mobile, password):
        """"""

    @get_daka("/ort/front/cashBack/query")
    def cash_back_query(self,semesterRef,mobile, password):

        """"""

    @get_daka("/ort/front/cashBack/punch/cardCalendar/activityInfo")
    def bck_card_alendar_activity_info(self, t,mobile, password):
        """"""

    # ######增长接口########
    #
    # @get_growth("/ort/front/products/presalepage/234")
    # def growth_pageinfo(self,mobile, password):
    #     """
    #     查询售前页信息
    #     """
    #
    # @get_growth("/ort/front/api/v1/invite/coupon/status")
    # def growth_couponstatus(self, couponid,mobile, password):
    #     """
    #     查询售前页优惠卷status
    #     """
    #
    # @post_growth("/ort/front/api/v1/invite/coupon")
    # def growth_usecoupon(self, couponid,mobile, password):
    #     """
    #     使用优惠卷
    #     """
    #
    # @get_growth("/trade/prepareorder/info")
    # def growth_tradeinfo(self, domain, businessTypeId, orderItems,mobile, password):
    #     """
    #     查询商业化下单信息
    #     """
    #
    # @get_growth("/xmkp-growth/front/distribution/userGrowthRoleUrl")
    # def growth_usergrowthroleurl(self, time,mobile, password):
    #     """
    #     1元分销--获取分流跳转地址
    #     """
    #
    # @get_growth("/xmkp-growth/front/distribution/userId")
    # def growth_userid(self, time,mobile, password):
    #     """
    #     获取用户id
    #     """
    # @get_growth("/xmkp-growth/front/distribution/config")
    # def growth_config(self, time,mobile, password):
    #     """
    #     获取1元分销阶梯奖项配置信息
    #     """
    # @get_growth("/xmkp-growth/front/distribution/UserDistributionDetail")
    # def growth_userdistribution(self, time, activityId,mobile, password):
    #     """
    #     获取用户阶梯奖励信息
    #     """
    #
    # @get_growth("/ort/front/api/v1/invite/poster")
    # def growth_poster(self, presalePageId,mobile, password):
    #     """
    #     生成海报
    #     """
    #
    # @post_growth("/ort/front/poster/identify")
    # def growth_identify(self, presalePageId,mobile, password):
    #     """
    #     保存海报的id
    #     """
    #
    # @get_growth("/ort/front/api/v1/invite/growth/monthLadderRewardConfig")
    # def growth_monthRewardConfig(self,mobile, password):
    #     """
    #     获取月课实物奖励配置
    #     """

    @get_m("/xmkp-cpb-web/front/adConfig/get/1")
    def adConfig_get_1(self,mobile, password):
        """
        banner页获取(轮播图)
        """

    @get_m("/xmkp-cpb-web/front/adConfig/get/3")
    def adConfig_get_3(self,mobile, password):
        """
        结算页获取(轮播图)
        """

    @get_m("/xmkp-cpb-web/front/user/study/info")
    def user_study_info(self,mobile, password):
        """
        查询绘本馆用户学习信息
        """

    @get_m("/xmkp-cpb-web/front/adConfig/notice")
    def adConfig_notice(self,mobile, password):
        """
        绘本馆公告
        """

    @get_m("/eduOps/api/v1/product/5")
    def m_product(self,mobile, password):
        """
        查询chinastory配置信息
        """

    @get_m("/ort/front/lesson/674/steps")
    def m_steps(self, lessonId, campRef,mobile, password):
        """
        查询课堂环节页信息
        """
    @get_m("/ort/front/products")
    def bck_products(self,mobile, password):
        """
        获取bck首页信息
        """
    @get_m("/ort/front/cocos/banner")
    def bck_banner(self,mobile, password):
        """
        获取首页的banner图
        """
    @get_daka("/ort/front/lesson/248/settlement")
    def daka_settlement(self, campRef,mobile, password):
        """
         星星结算
        """

    @get_m("/ort/front/lesson/coreVocabulary/248")
    def m_coreVocabulary(self,mobile, password):
        """
        获取课程248中的核心单词
        """

    @get_m("/ort/devops/api/v2/lesson/setting")
    def bck_setting(self,mobile, password):
        """
        获取用户强制跟读信息
        """

    @post_daka("/ort/front/step/homework/analysis/record", is_json_req=True)
    def bck_analysis_record(self, lessonRef, stepRef, campRef, analysisRef,mobile, password):
        """
        视频钻石结算
        """

    @post_daka("/ort/front/step/homework/wordRead/record", is_json_req=True)
    def bck_wordRead_record(self, recordType, homeworkRef, tryTimes, score, audioUrl, originAudioUrl, stepTypeStr,
                            text, stepRef, campRef, lessonRef, productRef,mobile, password):
        """
        单词跟读钻石结算
        """

    @post_daka("/ort/front/step/homework/noread/record", is_json_req=True)
    def bck_noRead_record(self, lessonRef, stepRef, campRef,  productRef, homeworkRef, tryTimes, homeworkType,mobile, password):
        """
        非跟读题钻石结算
        """

    @post_daka("/ort/front/step/readBook/record", is_json_req=True)
    def bck_readBook_record(self, stepRef, lessonRef, productRef, campRef, tryTimes, score,
                            audioUrl, duration, originAudioUrl, dialogRef, text,mobile, password):
        """
        绘本跟读钻石结算
        """
    @get_daka("/ort/front/cashBack/punch/cardCalendar/activityInfo?t=1611037540218")
    def bck_card_calendar_activity_info(self, t,mobile, password):
        """
         打卡返回活动日历信息

       """

    @get_daka("/ort/front/cashBack/query/4229")
    def bck_cashBack_detail(self,data,mobile, password):
        """
        打卡返现细节
        """

    @get_daka("/ort/front/cashBack/query/4229")
    def bck_cashback_query(self, semesterRef,mobile, password):
        """
        根据期号查询用户打卡返现状态
        """

    @post_daka("/ort/front/cashBack/confirm/4229", is_json_req=True)
    def bck_cashback_confirm(self, account, aliAccountName,semesterRef,mobile, password):
        """
        用户发起返现
        """
