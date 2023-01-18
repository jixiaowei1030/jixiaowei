"""
@Time: 2021/7/13 19:08
@Auth: duanmuqianqian
@File: conftest.py
@IDE: PyCharm
"""
import pytest


@pytest.fixture(scope="function")
def get_abtesting_list_fixture(abtest_cli,data,setupdata):
    res = abtest_cli.get_abtesting_list(page=str(data["page"]),
                                        pageSize=str(data["pageSize"]), status=str(data["status"]),
                                        mobile=setupdata["mobile"], password=setupdata["password"])
    testingCode = res["data"]["list"][0]["testingCode"]
    yield testingCode
