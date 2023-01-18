"""
中台交易case共用一个conftest.py
@author:joe.shi@ximalaya.com
"""
import random
import string
import time

import pytest

from api.http_client_rpc import HttpClientRpc
from utils.common import get_mysql


# class级别的fixture,在同一个class中调用多遍,只有第一次调用的时候运行
@pytest.fixture(scope="class")
def rpc_client():
    rpc_client = HttpClientRpc()
    yield rpc_client


@pytest.fixture(scope="class")
def db_client():
    db_client = get_mysql()
    yield db_client


@pytest.fixture
def random_xima_order_id():
    return str(random.randint(1, 9999999999999))


@pytest.fixture
def random_qimiao_order_id():
    return str(random.randint(1, 9999999999999))


@pytest.fixture
def random_string():
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))


@pytest.fixture
def exist_qimiao_order_id():  # 子单
    SQL = """
        SELECT sub_order_id
        FROM xmkp_trade_order.sub_trade_order t1
        WHERE t1.id >= RAND() * ((
            SELECT MAX(id)
            FROM xmkp_trade_order.sub_trade_order
            ) - (
            SELECT MIN(id)
            FROM xmkp_trade_order.sub_trade_order
            )) + (
            SELECT MIN(id)
            FROM xmkp_trade_order.sub_trade_order
        )
        LIMIT 1;
        """
    resp = get_mysql().query(SQL)
    return resp.sub_order_id


@pytest.fixture
def exist_parent_qimiao_order_id():  # 父单
    SQL = """
        SELECT parent_order_id
        FROM xmkp_trade_order.sub_trade_order t1
        WHERE t1.id >= RAND() * ((
            SELECT MAX(id)
            FROM xmkp_trade_order.sub_trade_order
            ) - (
            SELECT MIN(id)
            FROM xmkp_trade_order.sub_trade_order
            )) + (
            SELECT MIN(id)
            FROM xmkp_trade_order.sub_trade_order
        ) and t1.order_status = 0
        LIMIT 1;
"""
    resp = get_mysql().query(SQL)
    return resp.parent_order_id


@pytest.fixture
def exist_xm_order_id():
    SQL = "select xm_order_id from xmkp_trade_order.sub_trade_order where xm_order_id <> '' limit 1"
    resp = get_mysql().query(SQL)
    return resp.xm_order_id


@pytest.fixture
def canceled_parent_qimiao_order_id():
    SQL = "select parent_order_id from xmkp_trade_order.sub_trade_order where order_status = 2  limit 1"
    resp = get_mysql().query(SQL)
    return resp.parent_order_id


@pytest.fixture
def payed_parent_qimiao_order_id():
    SQL = "select order_id from xmkp_trade_order.trade_order where order_status = 1  limit 1"
    resp = get_mysql().query(SQL)
    return resp.order_id


@pytest.fixture
def now_time():
    return int(time.time() * 1000)


@pytest.fixture
def random_uid():
    return int(time.time() * 1000)


@pytest.fixture
def exist_uid_and_type():
    SQL = "select user_id,business_type from xmkp_logistics.DISPATCH_NOTE where user_id <> 0 order by created_time desc limit 1"
    resp = get_mysql().query(SQL)
    return resp


@pytest.fixture
def exist_business_id_and_type():
    SQL = "select business_id,business_type from xmkp_logistics.DISPATCH_NOTE where business_id is not null order by created_time desc limit 1"
    resp = get_mysql().query(SQL)
    return resp


@pytest.fixture
def exist_transport_company_and_transport_note():
    SQL = "select transport_company,transport_note from xmkp_logistics.TRANSPORT_TRACE limit 1"
    resp = get_mysql().query(SQL)
    return resp


@pytest.fixture
def real_person():
    # 所有信息于网上搜集,老赖
    return [
        ("芶宁岗", "532527198402032638"),
        ("王成付", "532123198812092812"),
        ("王绍红", "532228197403122497"),
        ("王应仙", "532226198207240922"),
        ("杨罕霖", "530125198509070013"),
        ("张静曦", "530102197412303328")
    ]
