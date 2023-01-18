"""
@author:xiaowei.ji
"""


from utils.tools.base_test_case import BaseTestCase
import allure


@allure.epic("L3")
class TestMathStudylogReport(BaseTestCase):
    """
                desc:验证学习报告的查询
                steps:
                1、查询获取学习报告的接口,获得返回json
                2、接口断言：2.1返回code为0，
                           2.2msg为成功，
                           2.3返回的img与数据库一致

                """
    @allure.title("{data.case_name}")
    def test_math_studylog_report(self,math_client,data,setupdata):
        """L3学习报告"""
        #第一步：调用接口，获取返回结果
        studylog_report=math_client[0].studylog_report(data.lessonId,setupdata.mobile,setupdata.password)
        #第二步：连接数据库查询预期结果
        img=math_client[1].query("select img from goodxs.annual_lesson  where id = %s"%(data.lessonId), False)
        #第三步：断言
        if data.lessonId <= 340:
            self.assert_equal(0, studylog_report.code)
            self.assert_equal("成功", studylog_report.msg)
            self.assert_equal(img.img,studylog_report.data.lessonImg)
        else:
            self.assert_equal(data.status,studylog_report.status)



