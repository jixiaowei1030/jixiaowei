# -*- coding: utf-8 -*-


# class Apollo:
#     '''apollo常量'''
#     APP_ID = 'config'
#     CONFIG_SERVER = 'http://192.168.60.10:8080'
#     NAMESPACE = 'application'
#     CLUSTER = 'default'
#     CONFIGS = 'configs'


class Framework:
    '''框架常量'''
    CASE_DIR = "cases"


class Env:
    '''环境常量'''
    # ENV = "release"  # 正式环境
    # ENV = "uat"  # uat
    ENV = "test"  # 测试环境


class RespCode:
    '''返回码常量'''
    SUCCESS = 0  # 请求成功
    ERROR = -400  # 请求错误

class UserToken:
    '''用户token常量'''
    USERTOKEN = {}

class LoginToken:
    '''登陆后获得的token常量'''
    XMLYTOKEN = {}
    OPSTOKEN = {}
    HQGTOKEN = {}

class RedisConfig:
    '''用户Redis常量'''
    REDIS = {
        "host": "192.168.60.48",
        "port": 19120,
        "password": "xmly123456",
        "db": 0
    }

class MysqlConfig:
    '''用户mysql常量'''
    MYSQL = {
        "host": "192.168.1.161",
        "port": 3307,
        "user": "naliworld",
        "password": "password!"
    }
