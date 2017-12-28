#coding utf-8

from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='百度测试报告',
                            description='用例测试情况')
    runner.run(testunit)
    fp.close()
