import re
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver=webdriver.Firefox()
# driver.get('http://192.9.103.142:8088')
# driver.find_element_by_id('txtUser_ID').send_keys('admin')
# driver.find_element_by_id('txtPassword').send_keys('-0')
# driver.find_element_by_id('btnLogin').click()


with open('测试文档', encoding='utf-8') as f:#加encoding的原因是因为测试文档中，有unicode
    msg = f.read()

# print(type(msg))
space = re.findall('\s*', msg) #找到所有的空格
# print(type(space))
space=''.join(space)
msg1 = msg.replace(space, '') #把所有的空格用去除
print(msg1)
# invoice_code = re.search('\d{10}', msg1)
# print(invoice_code[0])
# invoice_num = re.findall('\d{8}', msg1)
# print(invoice_num[1])