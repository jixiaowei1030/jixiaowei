from uiautotest.base.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class login(BasePage):
    def login(self):
        self.driver.get("https://dev-sa.link-tech.com/#/")
        self.send_keys(By.XPATH,"//*[@type='text']",text="lizhanquan@126.com")
        self.send_keys(By.XPATH,"//*[@type='password']",text="123456abc")
        self.click(By.XPATH,"//*[@class='lt-button lt-button-primary lt-button-large login-form-btn']")
        time.sleep(3)
        # element = self.driver.find_element(By.XPATH,"//*[@type='text']")
        # element.send_keys("lizhanquan@126.com")




