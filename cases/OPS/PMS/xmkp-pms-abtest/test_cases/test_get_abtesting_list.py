"""
@Time: 2021/7/13 15:38
@Auth: duanmuqianqian
@File: test_get_abtesting_list.py
@IDE: PyCharm
"""

class Test_get_abtesting_list:
    """
    查询AB实验列表数据
    """

    def test_get_abTesting_by_page(self, abtest_cli, data, setupdata):
        """
        desc:条件查询ab实验列表
        steps:
        1.查询进行中的实验
        2.查询暂停中的实验
        3.查询已结束的实验
        4.查询待开始的实验
        """
        res = abtest_cli.get_abtesting_list(page=str(data["page"]),
                                            pageSize=str(data["pageSize"]), status=str(data["status"]),
                                            mobile=setupdata["mobile"], password=setupdata["password"])
        assert res["message"] == data["response"]["message"]
        # testingCode = res["data"]["list"][0]["testingCode"]
        # m = dict()
        # m["a"] = testingCode
        # print(testingCode)
        # print(m)
