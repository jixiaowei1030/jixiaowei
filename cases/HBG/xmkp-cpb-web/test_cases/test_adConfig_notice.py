"""
@author:song.zhang
"""
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestCampBusinessType(BaseTestCase):

    def test_adConfig_notice(self, cpb_api_scope, setupdata):
        """
        desc:验证绘本馆的公告是否正常获取
        steps:
        1、查询获取绘本馆的公告的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调接口后获得返回json
        notice = cpb_api_scope[0].adConfig_notice(setupdata.mobile, setupdata.password)

        # 第二步：断言断言1里返回的值是否正确1里返回的值是否正确
        self.assert_equal('success', notice.message, "adConfig_notice接口调用失败")
