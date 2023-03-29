import pytest
import allure
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(driver.get_screenshot_as_png(), "异常截图", allure.attachment_type.PNG)


@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is None:
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        driver = webdriver.Chrome()
        # driver.maximize_window()
    yield driver
    # 所有用例执行完毕退出浏览器
    time.sleep(5)
    driver.quit()


@pytest.fixture(scope="session")
def login():
    driver.get("https://dev-sa.link-tech.com/#/")
    driver.find_element(By.XPATH,"//*[@type='text']").send_keys("lizhanquan@126.com")
    driver.find_element(By.XPATH,"//*[@type='password']").send_keys("123456abc")
    driver.find_element(By.XPATH,"//*[@class='lt-button lt-button-primary lt-button-large login-form-btn']").click()
    time.sleep(3)


