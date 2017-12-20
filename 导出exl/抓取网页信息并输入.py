from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie()
driver.get('https://inv-veri.chinatax.gov.cn/index.html')
assert '国家税务总局全国增值税发票查验平台' in driver.title
invoiceCode = driver.find_element_by_id('fpdm')
invoiceNum = driver.find_element_by_id('fphm')
date = driver.find_element_by_id('kprq')
money = driver.find_element_by_id('kjje')
vCode = driver.find_element_by_id('yzm')
# invoiceCode.clear()
# invoiceNum.clear()
# date.clear()
# money.clear()
# vCode.clear()
invoiceCode.send_keys('3200162160')
invoiceNum.send_keys('09376679')
date.send_keys('20171215')
money.send_keys('55042.74')
vCode.send_keys('3200162160')
