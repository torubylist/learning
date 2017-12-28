from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

first_url = 'http://www.baidu.com'
print("access the %s" %(first_url))
driver.get(first_url)

second_url = 'http://news.baidu.com'
print("access the %s" %(second_url))
driver.get(second_url)

time.sleep(2)

print("back to %s" %(first_url))
driver.back()

print("forward to %s" %(second_url))
driver.forward()

driver.quit()
print("test successfully")
