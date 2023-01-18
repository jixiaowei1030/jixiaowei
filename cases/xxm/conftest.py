"""
@Time: 2022/7/26 17:20
@author: jxw
"""

import pytest
from api.http_client_xxm import HttpClientXxm
from utils.log import LOGGER
from utils.common import get_mysql


@pytest.fixture(scope="session")
def xxm_client():
    LOGGER.info("----------喜马拉雅儿童接口测试开始----------")
    xxm = HttpClientXxm()
    mysql_login_info = {
        "host": "192.168.3.161",
        "port": 3306,
        "user": "naliworld",
        "password": "password!"
    }
    mysql = get_mysql(mysql_login_info)
    yield xxm,mysql
    LOGGER.info("----------喜马拉雅儿童接口测试结束----------")


