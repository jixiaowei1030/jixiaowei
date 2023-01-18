# -*- coding: utf-8 -*-

from abc import ABC
from utils.http.helper import get_m, get_daka, get_ops, post_m, post_daka, post_ops
from utils.http import BaseClient
import re


class HttpClientCpb(BaseClient):
    """
    desc:绘本馆接口
    """

    @get_m("/xmkp-cpb-web/front/adConfig/get/1")
    def adConfig_get_1(self, mobile, password):
        """
        banner页获取(轮播图)
        """

    @get_m("/xmkp-cpb-web/front/adConfig/get/3")
    def adConfig_get_3(self, mobile, password):
        """
        结算页获取(轮播图)
        """

    @get_m("/xmkp-cpb-web/front/user/study/info")
    def user_study_info(self, mobile, password):
        """
        查询绘本馆用户学习信息
        """

    @get_m("/xmkp-cpb-web/front/adConfig/notice")
    def adConfig_notice(self, mobile, password):
        """
        绘本馆公告
        """

    @get_m("/xmkp-cpb-web/front/week_read/recommend")
    def recommend_list(self, mobile, password):
        """
        绘本馆首页推荐列表
        """

    @get_m("/xmkp-cpb-web/front/user/study/currentDay")
    def study_currentDay(self, mobile, password):
        """
        获取用户当前打卡时间
        """

    @get_m("/xmkp-cpb-web/front/point_analysis/lately_read")
    def lately_read(self, mobile, password, typeId):
        """
        获取最近阅读的绘本列表（0：全部绘本）
        获取最近阅读的绘本列表（1：日常生活）
        获取最近阅读的绘本列表（2：寓言童话）
        获取最近阅读的绘本列表（3：探索发现）
        获取最近阅读的绘本列表（4：自然拼读）
        """

    @get_m("/xmkp-cpb-web/front/point_analysis/read_top/detail")
    def read_top_detail(self, mobile, password, typeId):
        """
        小朋友都在读的绘本列表（0：全部绘本）
        小朋友都在读的绘本列表（1：日常生活）
        小朋友都在读的绘本列表（2：寓言童话）
        小朋友都在读的绘本列表（3：探索发现）
        小朋友都在读的绘本列表（4：自然拼读）
        """

    @get_m("/xmkp-cpb-web/front/vip/preSale")
    def preSale_page(self, mobile, password, typeId):
        """
        获取商品id和价格
        售前页（月卡）:   typeId=1
        售前页（季卡）:   typeId=2
        售前页（年卡）:   typeId=3
        售前页（终身卡）: typeId=4
        """

    @get_m("/xmkp-cpb-web/front/vip/order/parameter/cocos")
    def parameter_cocos(self, mobile, password):
        """
        售前页-商品购买须知
        """

    @get_m("/xmkp-cpb-web/front/vip/expire_date/remain_days")
    def vip_expire_date(self, mobile, password):
        """
        获取vip失效时间
        """

    @get_m("/xmkp-cpb-web/front/user/info")
    def user_info(self, mobile, password):
        """
        获取用户基本信息
        """

    @get_m("/xmkp-cpb-web/front/user/isNewUser")
    def user_isNewUser(self, mobile, password):
        """
        判断是否是新用户
        """

    @get_m("/xmkp-cpb-web/front/wechat/official_account/qr_code?bookId=3018")
    def wechat_account_qr_code(self, mobile, password):
        """
        判断获取学习分享二维码链接接口返回正确
        """

    @get_m("/xmkp-cpb-web/front/user/study/currentDay")
    def user_study_currentDay(self, mobile, password):
        """
        获取用户当天是否是已学习状态
        """

    @get_m("/xmkp-cpb-web/front/user/studyCount/2867/3")
    def user_studyCount(self, mobile, password):
        """
        获取用户练环节学习次数
        """

    @get_m("/xmkp-cpb-web/front/metadata/deviceDecoder")
    def metadata_deviceDecoder(self, mobile, password):
        """
        判断修用户异常设备信息统计是否正确-al
        """

    @get_m("/xmkp-cpb-web/front/audioRecordR/5/listen/win/stars")
    def listen_win_stars(self, mobile, password):
        """
        判断听环节星星数结算是否正确-al
        """

    @get_m("xmkp-cpb-web/front/audioRecordR/5/win/stars")
    def read_win_stars(self, mobile, password):
        """
        判断读环节星星数结算是否正确-al
        """

    @get_m("/xmkp-cpb-web/front/exercise/5/win/stars")
    def exercise_win_stars(self, mobile, password):
        """
        判断练环节星星数结算是否正确-al
        """

    @post_m("/xmkp-cpb-web/front/user/week_read/recommend_plan/", is_json_req=True)
    def week_read_recommend_plan(self, mobile, password, level, bookCount):
        """
        判断修改学习计划是否正确-al
        """

    @post_m("/xmkp-cpb-web/front/point_analysis/point_data", is_json_req=True)
    def cashBack_learnDuration(self, mobile, password, bookId, typeId, level):
        """
        判断修改绘本曝光是否正确-al
        """

    @post_m("/xmkp-cpb-web/front/vip/order/parameter", is_json_req=True)
    def order_paramter(self, mobile, password, timestamp, returnUrl, context, realPrice, linedPrice):
        """
        获取售前页商品信息 （已废弃）
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/listen/star", is_json_req=True)
    def audioRecordR_listen_star(self, mobile, password, retryTime, bookId, pageId, audioRef):
        """
        听环节，上报星星
        """

    @get_m("/xmkp-cpb-web/front/preSale/remain/amount")
    def preSale_remain(self, mobile, password):
        """
        获取售前页剩余人数
        """

    @post_m("/xmkp-cpb-web/front/point_analysis/point_data", is_json_req=True)
    def point_analysis_point_data(self, mobile, password, bookId, typeId, level):
        """
        获取绘本曝光的状态
        """

    @get_m("/xmkp-cpb-web/front/vip/card/list")
    def vip_card_list(self, mobile, password):
        """
        获取用户vip卡列表
        """

    @get_m("/xmkp-cpb-web/front/cashBack/activity")
    def cashBack_activity(self, mobile, password):
        """
        获取用户参与的年卡返现activityType
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/star", is_json_req=True)
    def audioRecordR_star(self, mobile, password, type, score, retryTime, bookId, pageId, audioRef, audioType):
        """
        读环节上报分数后，对应的上报星星是否正确-al
        """

    @get_m("/xmkp-cpb-web/front/user/study/detail/", is_json_req=True)
    def user_study_detail(self, beginDate, endDate, mobile, password):
        """
        判断用户打卡日历是否正确-al
        """

    @get_m("/xmkp-cpb-web/front/bookR/book/star?bookId=3013", is_json_req=True)
    def bookR_book_star(self, mobile, password):
        """
        判断获取绘本已获得星星和总星星数-al
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/audio/record", is_json_req=True)
    def audioRecordR_audio_record(self, mobile, password, bookId, pageId, audioRef, text, duration, audioId, audioUrl, score, detail):
        """
        判断获取绘本已获得星星和总星星数-al
        """

    @get_m("/xmkp-cpb-web/front/share/token")
    def share_token(self, mobile, password, uid, bookId):
        """
        站外分享页获取token
        """

    @get_m("/xmkp-cpb-web/front/share/record")
    def share_record(self, mobile, password, uid, bookId):
        """
        分享录音页获取用户数据
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/exercise/star", is_json_req=True)
    def audioRecordR_exercise_star(self, mobile, password, type, score, retryTime, bookId, exerciseRef, isRead, studyNumber):
        """
        获取练环节，练习题上报分数
        """

    @post_m("/xmkp-cpb-web/front/exercise/audio/record", is_json_req=True)
    def exercise_audio_record(self, mobile, password, bookId, exerciseRef, text, duration, audioId, studyNumber, audioUrl, score, detail):
        """
        获取练环节，跟读题上报录音
        """

    @get_m("/xmkp-cpb-web/front/bookR/books/type/2/level/2")
    def bookR_books(self, mobile, password):
        """
        书架页获取绘本列表
        """

    @get_m("/xmkp-cpb-web/front/exercise/average/score/2867/22")
    def exercise_average_score(self, mobile, password):
        """
        练环节，结算页获取用户的平均得分
        """

    @get_m("/xmkp-cpb-web/front/user/study/isShowDakaTip")
    def is_show_daka_tip(self, mobile, password):
        """
        判断是否提示打卡成功信息或者是否播放打卡成功的动画
        """

    @get_m("/xmkp-cpb-web/front/research_questionnaire/config")
    def research_questionnaire_config(self, mobile, password):
        """
        获取“调查问卷”的链接
        """

    @get_m("/xmkp-cpb-web/front/audioRecordR/audio/2867/top/sentences")
    def top_sentences(self, mobile, password):
        """
        获取用户读环节所有录音
        """

    @get_m("/xmkp-cpb-web/front/audioRecordR/3023/see/win/stars")
    def see_win_stars(self, mobile, password):
        """
        查询用户指定绘本的看环节获取的星星详情列表-al
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/see/star", is_json_req=True)
    def audioRecordR_see_star(self, mobile, password, bookId, pageId, exploreDiscoveryRef):
        """
        看环节上报获取星星数-al
        """

    @get_m("/xmkp-cpb-web/front/football/presale/urls")
    def presale_urls(self, mobile, password, type):
        """
        获取“售前页”的链接
        售前页（月卡）:   type=1
        售前页（季卡）:   type=2
        售前页（年卡）:   type=3
        售前页（终身卡）: type=4
        售前页（无卡片）：type=5
        """

    @post_m("/xmkp-cpb-web/front/audioRecordR/step/finish", is_json_req=True)
    def step_finish(self, mobile, password, bookId, stepType):
        """
        获取练环节，跟读题上报录音
        """

    @get_m("/xmkp-cpb-web/front/audioRecordR/audio/{{book_id}}/lately/sentences")
    def lately_sentences(self, mobile, password, **kwargs):
        """
        读环节，获取用户最新录音列表
        """

    @get_m("/xmkp-cpb-web/front/bookR/books/serial")
    def books_serial(self, mobile, password):
        """
        全部系列，书架页获取指定系列的绘本
        """

    @get_m("/xmkp-cpb-web/front/exercise/3066/win/reading_comprehension/stars", is_json_req=True)
    def reading_comprehension_stars(self, mobile, password):
        """
        阅读理解已获得星星数
        """

    @get_m("/xmkp-cpb-web/antiTheft/book/resource?bookId=3066")
    def book_resource(self, mobile, password):
        """
        进入首页，获取某个绘本资源
        """

    @get_m("/xmkp-cpb-web/front/bookR/books/serial_info/")
    def serial_info(self, mobile, password):
        """
        全部系列tab获取绘本全部系列名称
        """

    @get_m("/xmkp-cpb-web/front/user/study/dakaRule")
    def daka_rule(self, mobile, password):
        """
        个人中心打卡规则提示文案
        """

    @get_m("/xmkp-cpb-web/front/vip/card/upgrade/lifetime")
    def vip_card_upgrade_lifetime(self, mobile, password):
        """
        用户是否可以升级终身卡
        """

    @post_m("/xmkp-cpb-web/front/level_read/level_plan", is_json_req=True)
    def level_plan(self, mobile, password, level):
        """
        分级阅读等级
        """

    @get_m("/xmkp-cpb-web/front/level_read/level_read")
    def level_read(self, mobile, password):
        """
        分级阅读绘本列表
        """

    @get_m("/xmkp-cpb-web/front/level_read/level_guide_board/query")
    def level_guide_board_query(self, mobile, password, type):
        """
        分级牌与路牌信息
        """

    @get_m("/xmkp-cpb-web/front/dict/{{word}}")
    def dict(self, mobile, password, **kwargs):
        """
        听环节，点词查意
        """
