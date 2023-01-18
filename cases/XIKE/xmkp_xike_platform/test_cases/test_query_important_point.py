from utils.tools.base_test_case import BaseTestCase
import allure

@allure.epic("喜课")
class TestQueryImportantPoint(BaseTestCase):

    @allure.title("{data.casename}")
    def test_query_important_point(self, xike_client, data, setupdata):
        res = xike_client[0].query_important_point(data.bookId, data.chapterId, data.businessType, setupdata.mobile, setupdata.password)
        print(res)
        self.assert_equal(data.code, res.code)
        if data.empty:
            self.assert_equal(data.chapterImportantPoint, res.data.chapterImportantPoint)
        else:
            self.assert_in(data.chapterImportantPoint, res.data.chapterImportantPoint)




