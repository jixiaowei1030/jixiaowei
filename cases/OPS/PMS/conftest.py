from utils.common import get_redis, get_mysql
from api.http_client_ops import XmkpPmsUsergroupWebService, XmkpPmsAdvertisementService, XmkpPmsAbtestService
import pytest
import time
from attrdict.dictionary import AttrDict


@pytest.fixture(scope="session", autouse=True)
def UsergroupWeb_cli():
    yield XmkpPmsUsergroupWebService()


@pytest.fixture(scope="session", autouse=True)
def mysql_cli():
    yield get_mysql()


@pytest.fixture(scope="function")
def new_UserGroup(UsergroupWeb_cli, data, mysql_cli,setupdata):
    """
    新建用户分群；使用完并清除用户分群数据
    return: groupId
    """
    print(setupdata)
    t = str(int(time.time()))
    res = UsergroupWeb_cli.new_userGroup(business=data["business"], groupName=data["groupName"] + t,
                                         rule=data["rule"],mobile=setupdata["mobile"],password=setupdata["password"])
    if not isinstance(res, AttrDict):
        raise TypeError("新增用户分群失败，请检查cookie!")
    groupId = str(mysql_cli.query(data["setup"]["query"] % t)["id"])

    yield groupId, t
    mysql_cli.query(data["teardown"]["query"][0] % groupId)
    mysql_cli.query(data["teardown"]["query"][1] % groupId)


@pytest.fixture(scope="function")
def enable_UserGroup(UsergroupWeb_cli, new_UserGroup,setupdata):
    """
    开启用户分群
    """
    groupId, t = new_UserGroup
    UsergroupWeb_cli.enable_userGroup(mobile=setupdata["mobile"],password=setupdata["password"],extra_url=groupId)
    yield groupId


@pytest.fixture(scope="session", autouse=True)
def ad_ser():
    yield XmkpPmsAdvertisementService()

@pytest.fixture(scope="session", autouse=True)
def abtest_cli():
    yield XmkpPmsAbtestService()

@pytest.fixture(scope="function")
def new_abtest(abtest_cli, data, mysql_cli,setupdata):
    """
    新建ab实验
    使用完清除ab实验配置数据
    return: testingCode
    """
    print(setupdata)
    t = str(int(time.time()))
    res = abtest_cli.new_abtest(businessType=data["businessType"], testingName=data["testingName"] + t,
                                         mobile=setupdata["mobile"],password=setupdata["password"])
    if not isinstance(res, AttrDict):
        raise TypeError("新建ab实验失败，请检查cookie!")
    testingCode = str(mysql_cli.query(data["setup"]["query"] % t)["testing_code"])

    yield testingCode, t
    mysql_cli.query(data["teardown"]["query"][0] % testingCode)
    mysql_cli.query(data["teardown"]["query"][1] % testingCode)