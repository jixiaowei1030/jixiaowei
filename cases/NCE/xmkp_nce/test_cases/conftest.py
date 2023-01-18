"""
@Time ： 2021/5/19 18:15
@Auth ： yanziqiang
"""

from api.http_client_nce import HttpClientNce
from utils.common import get_mysql
import pytest


@pytest.fixture(scope="function")
def xgn_api():
    nce = HttpClientNce()
    mysql = get_mysql()
    yield nce, mysql
