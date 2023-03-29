import time


from uiautotest.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Shipment(BasePage):

    operation = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[1]')

    forwarding = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[2]/div/ul/li/span[1]')

    shipment = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/span[2]/div/ul/li/div/div/ul/li[1]/span')

    new = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]/button')

    transport_click = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/input')

    transport_select = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[1]/div/div/div/div[2]/ul/div/li[1]/div')

    save = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div/span/div/button[1]')

    # def login(self):
    #     self.driver.get("https://dev-sa.link-tech.com/#/")
    #     self.send_keys(By.XPATH,"//*[@type='text']",word="lizhanquan@126.com")
    #     self.send_keys(By.XPATH,"//*[@type='password']",word="123456abc")
    #     self.click(By.XPATH,"//*[@class='lt-button lt-button-primary lt-button-large login-form-btn']")
    #     time.sleep(3)


    def move_shipment(self):    #移动到shipment
        element_operation = self.find_element(*self.operation)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_operation).perform()
        element_forwarding = self.find_element(*self.forwarding)
        actions.move_to_element(element_forwarding).perform()


    def click_shipment(self):   #点击shipment
        self.click(*self.shipment)
        time.sleep(1)

    def add_Shipment(self):    #新建shipment
        self.click(*self.new)
        time.sleep(1)

    def input_content(self):    #填写文本
        self.click(*self.transport_click)
        self.click(*self.transport_select)

    def save_content(self):    #保存
        self.click(*self.save)
