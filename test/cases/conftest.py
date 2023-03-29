# conftest.py文件
# coding:utf-8
from selenium import webdriver
import pytest
import time

driver = None

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     global driver
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     ** 作者：上海-悠悠 QQ交流群：588402570**
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot():
#     '''
#     ** 作者：上海-悠悠 QQ交流群：588402570**
#     截图保存为base64，展示到html中
#     :return:
#     '''
#     return driver.get_screenshot_as_base64()

@pytest.fixture(scope="module")
def login(request):
    name=request.param[0]
    psw=request.param[1]
    global driver
    # option=webdriver.ChromeOptions()
    # option.add_argument('diable-infobars')
    # driver=webdriver.Chrome(chrome_options=option)
    driver = webdriver.Chrome()
    # driver.get("http://managetest.tycredit.com/index.html#/")
    driver.get("http://172.17.45.29:8030/index.html#/")
    # time.sleep(3)
    driver.find_element_by_xpath("//input[@placeholder='账户']").send_keys(name)
    driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(psw)
    driver.find_element_by_xpath("//input[@placeholder='验证码']").send_keys("123456")
    driver.find_element_by_xpath("//button[@class='submit_btn ivu-btn ivu-btn-primary']").click()

    # def end():
    #     print("全部用例执行完后 teardown quit dirver")
    #     time.sleep(5)
    #     driver.quit()
    # request.addfinalizer(end)
    return driver




# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#     return driver


# @pytest.fixture(scope="session")
# def login():
#     print("用例先登录")




