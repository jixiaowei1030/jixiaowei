import pytest
from demo_pytest_new.method.org_aggregate_management import Org_aggregate_management
import allure


@allure.epic("业管台-汇总管理")
@allure.feature("测试模块")
class Test_aggregate_management():
    test_user_data = [("biqing", "123123")]

    def setup_class(self):
        Test_aggregate_management.count = 0


    def setup_method(self):
        global driver
        if Test_aggregate_management.count > 0:
            driver.refresh()
        else:
            Test_aggregate_management.count += 1

    # @allure.title("调用量任务管理查询")
    # # @allure.severity("critical")
    @pytest.mark.parametrize("login", test_user_data, indirect=True)
    def test_01(self,login):
        '''调用量任务管理查询'''
        global aggregate_management
        global driver
        driver=login
        aggregate_management = Org_aggregate_management(driver)
        aggregate_management.call_volume_task_management_select()
    #
    # @allure.title("日切账单错误信息管理")
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_02(self,login):
    #     '''日切账单错误信息管理'''
    #     global aggregate_management
    #     global driver
    #     driver = login
    #     aggregate_management = Org_aggregate_management(driver)
    #     aggregate_management.error_information_of_daily_cutting_bill_select()
    #
    # @allure.title("日切账单管理查询，下载")
    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_03(self,login):
    #     '''日切账单管理查询，下载'''
    #     global aggregate_management
    #     global driver
    #     driver = login
    #     start_date="2019-12-23"
    #     end_date="2019-12-24"
    #     aggregate_management = Org_aggregate_management(driver)
    #     aggregate_management.daily_cutting_bill_select()
    #     result=aggregate_management.daily_cutting_bill_download(start_date,end_date)
    #     assert(result),"判断下载文件成功，实际结果：%s" %result
#
# if __name__=="__main__":
#     pytest.main()

