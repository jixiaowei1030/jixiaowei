#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午5:22
# @Author  : Tina.du
# @File    : http_client_qqx.py

from utils.http import BaseClient
from utils.http.helper import get_m, post_m


class HttpClientQqx(BaseClient):
    """
    desc:  奇奇学App接口Api
    """

    @get_m("/qqx/user/queryPersonalInfo")
    def personal_info(self, mobile, password):
        """
        desc:个人中心
        @return:
        """

    @post_m("/ort/user/updateUserInfo", is_json_req=True)
    def update_user_info(self, userInfoShow, birthday, userSex, nickname, babyHeaderUrl, mobile, password):
        """

        @param userInfoShow:
        @param birthday: 用户的出生年月
        @param userSex: 性别
        @param nickname: 昵称
        @param babyHeaderUrl: 头像的URL
        @param mobile: 用户的手机号
        @param password: 登录的密码
        @return:
        """

    @get_m("/ort/user/queryUserInfo")
    def query_user_info(self, mobile, password):
        """
        desc:用户信息查询
        @return:
        """

    @get_m("/qqx/user/hasNewUser")
    def has_new_user(self, mobile, password):
        """
        用户-首页判断是否新用户，以及售前页连接
        @return:
        """


    @post_m("/qqx/userSettings/upateQqxUserSettings")
    def update_user_setting(self, campId, isOpen, type, mobile, password):
        """
        用户设置-训练营
        @param mobile: 用户的手机号
        @param password: 密码
        @param campId:训练营的id
        @param isOpen:是否打开，1-开 0-关
        @param type : 开课提醒
        @return:
        """

