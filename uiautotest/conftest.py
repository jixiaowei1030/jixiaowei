import pytest
import allure
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

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
    driver_path = '/chromedriver'
    if driver is None:
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
    yield driver
    # 所有用例执行完毕退出浏览器
    time.sleep(5)
    driver.quit()


# def add_shipment(self):
#     element = self.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[1]')
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#     self.click(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[2]/div/ul/li/div/div/ul/li[1]/span')
#     self.click(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]/button')
#     self.click(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div/span/div/button[1]')
