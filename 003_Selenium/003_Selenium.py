#encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()

driver.get("http://www.douban.com")
time.sleep(1)

driver.find_element_by_name("form_email").send_keys("805249506@qq.com")

time.sleep(10)
driver.quit()