"""
@Auth ： shishuaigang
"""
from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
from api.http_client_bck import HttpClientBck
from utils.common import get_mysql
class TestBckGetUserDiamond(BaseTestCase):
    """
    用户钻石接口用例
    """
    @classmethod
    def setup_class(cls):
        cls.bck = HttpClientBck()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")
    @classmethod
    def teardown_class(cls):
        pass
    def test_bck_diamond(self,setupdata):
        """
        desc: 校验用户接口返回的钻石数量是否与db内一致
        """
        #请求接口拿到返回信息
        diamonds = self.bck.diamond(setupdata.mobile,setupdata.password)  # 接口用户钻石的数量
        uid = UserToken.USERTOKEN['Cookie'].split("=")[1].split("&")[0]  # cookie中获取用户uid
        # print(uid)
        sql = f"SELECT balance FROM xmkp_edu.EDU_ACCOUNT WHERE user_id={uid}"
        diamonds_in_db = self.mysql.query(sql=sql, fetch_all=False)
        # print(diamonds_in_db)
        # print(diamonds_in_db.balance)
        # # print (int(diamonds_in_db['balance']))
        self.assert_equal(int(diamonds_in_db.balance), diamonds, "用户钻石数量正确")
