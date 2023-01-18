from utils.tools.base_test_case import BaseTestCase

class TestLoadPageContent(BaseTestCase):
    '''
    desc:验证频道页
    steps:
    1、调用频道接口，获取返回结果
    2、断言：2.1返回msg为0
           2.2返回ret为0
           2.4返回频道页与请求一致



    '''
    def test_load_page_content(self,xxm_client,data,setupdata):
        # 第一步：调用频道接口，获取返回结果
        test_load_page_content = xxm_client[0].load_page_content(mobile= setupdata.mobile, password= setupdata.password,req_json=data["test_load_page_content_01"])
        print(test_load_page_content)
        # 第二步：断言
        self.assert_equal("0",test_load_page_content["msg"])
        self.assert_equal( 0, test_load_page_content["ret"])
        self.assert_equal(data["test_load_page_content_01"]["pageTitle"], test_load_page_content["data"]["pageTitle"])
