"""
@Time: 2021/6/16 15:52
@author: xiaowei.ji
"""
import pytest
from api.http_client_math import HttpClientMath
from utils.log import LOGGER
from utils.common import get_mysql

@pytest.fixture(scope="session")
def math_client():
    LOGGER.info("----------数学接口测试开始----------")
    math=HttpClientMath()
    mysql=get_mysql()
    yield math , mysql
    LOGGER.info("----------数学接口测试结束----------")


