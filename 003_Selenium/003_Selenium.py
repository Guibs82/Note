#encoding:utf-8

import unittest
import time

from selenium import webdriver

class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.Safari()

    # 具体测试用例方法, 一定要以 test 开头
    def testDB(self):
        self.driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")
        # 向下滚动10000 像素
        js = "document.body.scrollTop=10000"
        time.sleep(3)
        self.driver.save_screenshot('douban.png')

        self.driver.execute_script(js)
        time.sleep(15)

        self.driver.save_screenshot('newdouban.png')

    # 退出时清理方法
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main