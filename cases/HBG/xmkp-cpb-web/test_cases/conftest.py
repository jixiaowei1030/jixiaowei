"""
@Time ： 2021/1/26 22:15
@Auth ： wangtao
@File ：conftest.py
@IDE ：PyCharm

"""

from api.http_client_cpb import HttpClientCpb
from utils.common import get_mysql
import pytest
from utils.log import LOGGER
from utils.common import get_redis
from common.getlogintoken import LoginGetToken
import re
from common.const import RedisConfig

@pytest.fixture(scope="class")
def cpb_api_scope():
    LOGGER.info("----------绘本馆单接口测试开始-----------")
    # 获取接口
    cpb = HttpClientCpb()
    # 获取mysql
    mysql = get_mysql()
    # 获取redis
    redis = get_redis()
    # 获取用户的uid
    token = LoginGetToken("17602163851", "asdf3.14", "test").Gettoken()
    user_id = re.search("(.*?)&", token).group(1)
    # 将以上获取到的数据返回出去
    yield cpb, mysql, redis, user_id
    LOGGER.info("----------绘本馆单接口测试结束-----------")


if __name__ == '__main__':
    a = get_redis()