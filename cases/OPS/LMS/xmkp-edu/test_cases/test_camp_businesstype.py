"""
@author:sunguhua
"""
import time
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestCampList(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_camp_businesstype_one(self, data,setupdata):
        """
        desc:验证牛津树训练营列表字段
        steps:
        1、查询牛津树训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_one(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 1 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["period"], camp_list[i]["period"], "学时（天）")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_two(self, data,setupdata):
        """
        desc:验证通用训练营列表字段
        steps:
        1、通用训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_two(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 2 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_four(self, data,setupdata):
        """
        desc:验证书虫训练营列表字段
        steps:
        1、书虫训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_four(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 4 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_six(self, data, setupdata):
        """
        desc:验证自然拼读训练营列表字段
        steps:
        1、自然拼读训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_six(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 6 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_eight(self, data,setupdata):
        """
        desc:验证何秋光数学训练营列表字段
        steps:
        1、何秋光数学训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_eight(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 8 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_nine(self, data,setupdata):
        """
        desc:验证亲子儿童训练营列表字段
        steps:
        1、亲子儿童训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_nine(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 9 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_ten(self, data,setupdata):
        """
        desc:验证喜马大学训练营列表字段
        steps:
        1、喜马大学训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_ten(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 10 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")

    def test_camp_businesstype_eleven(self, data,setupdata):
        """
        desc:验证新概念训练营列表字段
        steps:
        1、新概念训练营列表接口,获得返回json
        2、查数据库获得查询数据
        3、断言页面显示的字段与数据库的值是否一致
        """
        camp_list = self.ops.camp_businesstype_eleven(data.timeStamp,setupdata.mobile ,setupdata.password)
        edu_camp = self.mysql.query(
            "SELECT * from xmkp_edu.EDU_CAMP where business_type = 11 and is_deleted = 0 order by id", True)
        for i in range(0, len(edu_camp)):
            self.assert_equal(edu_camp[i]["id"], camp_list[i]["id"], "训练营ID")
            self.assert_equal(edu_camp[i]["identity"], camp_list[i]["identity"], "专辑ID/商品ID")
            self.assert_equal(edu_camp[i]["description"], camp_list[i]["description"], "备注")
