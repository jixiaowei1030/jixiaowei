from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("bookworm")
class TestFindBookChapterInfo(BaseTestCase):
    @allure.title("{data.casename}")
    def test_find_book_chapterinfo(self, xike_client, data, setupdata):
        res = xike_client[0].find_book_chapterinfo(setupdata.mobile, setupdata.password, data.chapterId, data.bookId)
        print("011")
        print(res)
        self.assert_equal("success", res.message)


