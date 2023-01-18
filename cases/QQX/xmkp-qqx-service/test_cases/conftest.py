#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午5:17
# @Author  : Tina.du
# @File    : conftest.py


from api.http_client_qqx import HttpClientQqx
from utils.common import get_mysql
import pytest
from utils.log import LOGGER
from utils.common import get_redis
# from common.apollo import services


@pytest.fixture(scope="class")
def qqx_api_scope():
    LOGGER.info("----------奇奇学单接口测试开始-----------")
    qqx = HttpClientQqx()
    mysql = get_mysql()
    redis = get_redis()
    yield qqx, mysql, redis
    LOGGER.info("----------奇奇学单接口测试结束-----------")
