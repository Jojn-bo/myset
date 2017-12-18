import re
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver=webdriver.Firefox()
# driver.get('http://192.9.103.142:8088')
# driver.find_element_by_id('txtUser_ID').send_keys('admin')
# driver.find_element_by_id('txtPassword').send_keys('-0')
# driver.find_element_by_id('btnLogin').click()

# 打开测试文档
with open('测试文档', encoding='utf-8') as f:#加encoding的原因是因为测试文档中，有unicode
    msg = f.read()

# 正则搜索关键信息
invoiceCode = re.search('\d{10}', msg)[0]  # 发票代码
# print(invoiceCode)
invoiceNum = re.findall('\d{8}', msg)  # 发票号码
# print(invoiceNum[1])
date = re.search('\d{4}年\d{2}月\d{2}', msg)[0]  # 开票日期
# print(date)
date = date.replace('年', '-')
date = date.replace('月', '-')
str=' 00:00:00'
date = date + str
# print(date)
# 开始匹配商品
commodity = re.search('(税额([\s\S]*)\n合计)', msg)[0]
# 如果有很多商品
commodity1 = re.findall('(\n([\s\S]*)\n)?', commodity)[3]
print(commodity1[3])

# 把相关信息放入excel


# 保存excel