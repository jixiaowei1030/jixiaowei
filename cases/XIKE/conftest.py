"""
@Time: 2021/9/24 15:52
@author: lhz
"""
import pytest
from api.http_client_xike import HttpClientXike
from utils.log import LOGGER
from utils.common import get_mysql

@pytest.fixture(scope="session")
def xike_client():
    LOGGER.info("----------喜课接口测试开始----------")
    xike = HttpClientXike()
    mysql = get_mysql()
    yield xike, mysql
    LOGGER.info("----------喜课接口测试结束----------")


