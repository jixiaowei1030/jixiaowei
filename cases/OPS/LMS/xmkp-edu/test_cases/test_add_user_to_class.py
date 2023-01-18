"""
@author:niefang
"""
from utils.common import get_redis, get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_ops import HttpClientOps
from utils.tools.wait_for_condition import wait_for_condition
from utils.util import gen_rand_str


class TestAddUserToClass(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.ops = HttpClientOps()
        cls.mysql = get_mysql()
        cls.setup_data = getattr(cls, "setup_data")

    def teardown_class(cls):
        pass

    def test_add_user_to_class(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级是否成功
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((add_user_to_class["data"]),
                          "成功把用户uid [347184] 加入到CampID [21], 期ID [595], 的班级ID (69508)")

        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")

    def test_add_user_to_class_repeat(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级
        3、重复347184添加进69508班级
        4、验证返回中用户已经在这一期中
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        test_add_user_to_class_repeat = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)

        self.assert_equal((test_add_user_to_class_repeat["data"]), "用户已经在这一期中")

        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")

    def test_add_user_to_class_same(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级
        3、重复347184添加进同期学员
        4、验证返回中用户已经在这一期中
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        add_user_to_class_same = self.ops.add_user_to_class_same(data.timeStamp,setupdata.mobile, setupdata.password)

        self.assert_equal((add_user_to_class_same["data"]), "用户已经在这一期中")

        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")

    def test_add_user_to_class_different_same(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级
        3、重复347184添加进同canp不同期学员
        4、验证返回中用户已经在这一期中
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((test_add_user_to_class["data"]),
                          "成功把用户uid [347184] 加入到CampID [21], 期ID [595], 的班级ID (69508)")
        add_user_to_class_different_same = self.ops.add_user_to_class_different_same(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((add_user_to_class_different_same["data"]), "用户已经在这一期中")
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")

    def test_add_user_to_class_different_camp(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级
        3、重复347184添加不同canp学员同business_type
        4、验证添加成功
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((test_add_user_to_class["data"]),
                          "成功把用户uid [347184] 加入到CampID [21], 期ID [595], 的班级ID (69508)")
        add_user_to_class_different_camp = self.ops.add_user_to_class_different_camp(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((add_user_to_class_different_camp["data"]),
                          "成功把用户uid [347184] 加入到CampID [23], 期ID [773], 的班级ID (69220)")
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69220 and user_id =347184")
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")

    def test_add__class_different_business_type(self, data,setupdata):
        """
        desc:验证接口返回的班级数据
        steps:
        1、调接口后添加学员成功
        2、验证返回中是否347184添加进69508班级
        3、重复347184添加学员为不同business_type学员
        4、验证添加成功
        """
        user_info = self.mysql.query(
            "select * from xmkp_edu.EDU_CLASSMATE where semester_ref = 595 and user_id = 347184")
        if user_info == {}:
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        else:
            self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE semester_ref = 595 and user_id =347184")
            test_add_user_to_class = self.ops.add_user_to_class(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((test_add_user_to_class["data"]),
                          "成功把用户uid [347184] 加入到CampID [21], 期ID [595], 的班级ID (69508)")
        add_class_different_business_type = self.ops.add_class_different_business_type(data.timeStamp,setupdata.mobile, setupdata.password)
        self.assert_equal((add_class_different_business_type["data"]),
                          "成功把用户uid [347184] 加入到CampID [105], 期ID [2226], 的班级ID (70065)")
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 70065 and user_id =347184")
        self.mysql.query("delete from xmkp_edu.EDU_CLASSMATE  WHERE class_ref = 69508 and user_id =347184")