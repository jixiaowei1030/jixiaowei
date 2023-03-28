import time


from uiautotest.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class add_shipment(BasePage):


    def login(self):
        self.driver.get("https://dev-sa.link-tech.com/#/")
        self.send_keys(By.XPATH,"//*[@type='text']",word="lizhanquan@126.com")
        self.send_keys(By.XPATH,"//*[@type='password']",word="123456abc")
        self.click(By.XPATH,"//*[@class='lt-button lt-button-primary lt-button-large login-form-btn']")
        time.sleep(3)


    def add_shipment(self):
        element1 = self.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[1]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element1).perform()
        time.sleep(1)
        element2 = self.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[2]/div/ul/li/span[1]')
        actions.move_to_element(element2).perform()
        time.sleep(1)
        self.click(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[2]/div/ul/li/div/div/ul/li[1]/span')
        self.click(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]/button')
        time.sleep(1)
        self.click(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div/span/div/button[1]')



