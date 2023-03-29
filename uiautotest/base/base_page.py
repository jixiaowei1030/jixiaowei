import os.path
import time

from selenium.common.exceptions import NoSuchElementException
from uiautotest.utils.logs import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        log.info(f"wait for {seconds} seconds")

    def clear(self, *selector):
        el = self.find_element(*selector)
        try:
            el.clear()
            log.info("Clear text in input box before typing.")
        except NameError as e:
            log.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            log.error(f"Failed to take screenshot! , because {e}")
            self.get_windows_img()

    def find_element(self, *selector):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(lambda x: x.find_element(*selector))
            log.info(f"The element looked up is {selector}")
            return element
        except NoSuchElementException as e:
            log.error(f"NoSuchElement:{selector}")
            self.get_windows_img()

    def send_keys(self,*selector,text):
        el = self.find_element(*selector)
        el.clear()
        try:
            el.send_keys(text)
            log.info(f"Had type ## {text} ## in inputBox")
        except NameError as e:
            log.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def click(self, *selector):
        el = self.find_element(*selector)
        try:
            self.driver.execute_script("arguments[0].click();", el)
            log.info(f"The element ##{el}## was clicked")
        except NameError as e:
            log.error("Failed to click the element with %s" % e)

    def is_element_exit(self,*selector):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(selector))
            return True
        except :
            return False







