from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com')
# print(browser.title)
# browser.maximize_window()
# browser.implicitly_wait(0.5)
#
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.find_element_by_id('kw').clear()
# browser.find_element_by_name('wd').send_keys('selenium')
# browser.find_element_by_id('su').send_keys(Keys.ENTER)
# time.sleep(3)
# browser.quit()


dr = webdriver.Firefox()
file_path = 'file:///'+ os.path.abspath('checkbox.html')
dr.get(file_path)
inputs = dr.find_element_by_tag_name('input')
for i in inputs:
    if i.get_attribute('type') == 'radio':
        print(i.get_attribute('type'))
        i.click()
time.sleep(2)
dr.quit()

# base_url = "http://www.hao123.com"
# driver = webdriver.Firefox()
# driver.get(base_url)
# s = driver.find_elements_by_css_selector("ul.js_bd.site-bd.site-hd0>li>a")
# for i in s:
#     print(i.get_attribute("href"))


# base_url = "https://hao.360.cn"
# driver = webdriver.Firefox()
# driver.get(base_url)
# s = driver.find_elements_by_css_selector("ul.list.last.gclearfix>li>a")
# for i in s:
#     print(i.get_attribute("href"))
# print('ok')

