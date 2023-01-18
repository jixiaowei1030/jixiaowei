from utils.tools.base_test_case import BaseTestCase

class TestXkHomeIsGotoLessonPage(BaseTestCase):
    """
                        desc:验证喜客-首页定位(是否跳转课程页)
                        steps:
                        1、喜客-首页定位(是否跳转课程页)的接口,获得返回json
                        2、接口断言：2.1返回code为0，
                                   2.2message为success
                        """
    def test_xkHome_isGotoLessonPage(self,xike_client,data,setupdata):
        # 第一步：调用接口，获取返回结果
        test_xkHome_isGotoLessonPage=xike_client[0].get_xkHome_isGotoLessonPage(setupdata.mobile,setupdata.password)
        print(test_xkHome_isGotoLessonPage)
        # 第二步：断言
        self.assert_equal(0,test_xkHome_isGotoLessonPage.code)
        self.assert_equal("success",test_xkHome_isGotoLessonPage.message)
        self.assert_equal(True,test_xkHome_isGotoLessonPage.data.jumpLesson)



