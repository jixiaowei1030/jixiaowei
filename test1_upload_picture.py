from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://account.cnblogs.com/signin?ReturnUrl=https://home.cnblogs.com/set/profile/")
driver.find_element_by_xpath("//input[@placeholder='登录用户名 / 邮箱']").send_keys("莫伊失忆")
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("Jxw1994abc#")
driver.find_element_by_id("submitBtn").click()
time.sleep(5)
driver.find_element_by_link_text("上传头像").click()
#input 标签
driver.find_element_by_name('file').send_keys("C:\\Users\\Administrator\\Desktop\\index.jpg")
