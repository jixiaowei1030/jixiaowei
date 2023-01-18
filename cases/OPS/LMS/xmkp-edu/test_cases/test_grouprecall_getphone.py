"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestGroupRecallphone(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_grouprecall_getphone(self, data,setupdata):
            """
            desc:查询用户手机号
            steps:
            1、调接口后获得返回json
            2、24小时内第一次查看，返回手机号
            3、24小时非第一次查看，返回已经查询过
            """
            grouprecall_getphone_list = self.ops.grouprecall_getphone(data.timeStamp, data.studentId,setupdata.mobile ,setupdata.password)

            code=grouprecall_getphone_list.code
            message=grouprecall_getphone_list.message
            data=grouprecall_getphone_list.data
            if code == 1 and data == 15963633636:
                print("pass")
            elif  code == -1 and message == "教师[1]-已经查询过学生[800058]的手机号,无法继续查询":
                print("pass")
            else:
                print(code)






