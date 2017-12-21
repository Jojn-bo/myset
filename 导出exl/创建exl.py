import xlwt
import re

# 打开测试文档
with open('测试文档.txt.tet', encoding='utf-8') as f:  # 加encoding的原因是因为测试文档中，有unicode
    msg = f.read()

# 正则搜索关键信息
invoiceCode = re.search('\d{10}', msg)[0]  # 发票代码
# print(invoiceCode)
invoiceNum = re.findall('\d{8}', msg)[1]  # 发票号码
# print(invoiceNum[1])
date = re.search('\d{4}年\d{2}月\d{2}', msg)[0]  # 开票日期
# print(date)
date = date.replace('年', '-')
date = date.replace('月', '-')
str = ' 00:00:00'
date = date + str
# print(date)

# 开始匹配商品
commodity = re.search('(税额([\s\S]*)\n合计)', msg)[0]
# 如果有很多商品
# commodity1 = re.search('(\n.([\s\S]*)\s\n)', commodity)
commodity1 = re.search('(\n.([\s\S]*)\n)', commodity)
commodity1 = commodity1[0].strip('\n')  # 去掉首尾的换行符
# print(commodity1, type(commodity1))
commodity2 = commodity1.split('\n')  # 多个商品用列表存放
# print(commodity2)

# 对单个商品进行处理
def one_comm(args):
    args = args.strip('')
    args1 = args.split(' ')
    for x in args1:
        if x == '':
            args1.remove(x)
    if len(args1) > 8 or len(args1) < 7:
        return ''
    return args1

if len(commodity2) >1:
    # print(len(commodity2))  # 6条
    i = 0
    commodity3 = []
    while i < len(commodity2):
        x = one_comm(commodity2[i])
        if x == '':
            print('商品或规格型号有空格，请手动输入')
            continue
        commodity3.append(x)
        i += 1
    # print(commodity3)
else:
    commodity3 = one_comm(commodity2[0])
    if commodity3[0] == '':
        print('商品或规格型号有空格，请手动输入')
    # print(commodity3)

# 开始匹配备注
remarks = (re.search('注\n([\s\S]*)\n纳', msg))[0]
remarks1 = remarks.split('\n')
for x in remarks1:
    if x == '':
        remarks1.remove(x)
remarks1.remove('注')
remarks1.remove('纳')
remarks = remarks1[0]
# print(remarks)

# 开始购方名称
buyer_name = re.search('(名称([\s\S]*)\n密)', msg)[0]
buyer = buyer_name.strip('')
buyer1 = buyer_name.split('\n')
buyer_name = buyer1[0][4:-1]
# print(buyer_name)

# 开始购方税号、地址、开户行
buyer_msg = re.search('(识别号([\s\S]*)货)', msg)[0]
buyer_msg = buyer_msg.strip('')
buyer_msg1 = buyer_msg.split('\n')
# print(buyer_msg1)
buyer_tax = buyer_msg1[0][5:-1]
buyer_address = buyer_msg1[1][7:-1]
buyer_bank = buyer_msg1[2][8:-1]
# print(buyer_tax, '\n', buyer_address, '\n', buyer_bank)

# 开始销方名称
saler_name = re.search('(售([\s\S]*)\n备)', msg)[0]
saler_name = saler_name.strip('')
saler_name1 = saler_name.split('\n')
saler_name = saler_name1[3][5:]
# print(saler_name)

# 开始销方税号、地址、开户行
saler_msg = re.search('(注([\s\S]*)特)', msg)[0]
saler_msg = saler_msg.strip('')
saler_msg1 = saler_msg.split('\n')
saler_tax = ''
saler_address = ''
saler_bank = ''
# print(saler_msg1)
for x in saler_msg1:
    if '纳税人' in x:
        saler_tax = x[8:]
    if '地址' in x:
        saler_address = x[7:]
    if '开户行' in x:
        saler_bank = x[8:]
# print(saler_tax,saler_address,saler_bank)

# 保存excel


wb = xlwt.Workbook()
sh = wb.add_sheet('TestSheet')

def first():
    sh.write(0, 0, '发票代码')
    sh.write(0, 1, '发票号码')
    sh.write(0, 2, '商品名称')
    sh.write(0, 3, '规格型号')
    sh.write(0, 4, '计量单位')
    sh.write(0, 5, '单价')
    sh.write(0, 6, '数量')
    sh.write(0, 7, '金额')
    sh.write(0, 8, '税率')
    sh.write(0, 9, '税额')
    sh.write(0, 10, '发票种类')
    # sh.write(1, 10, '专用发票')
    sh.write(0, 11, '备注')
    sh.write(0, 12, '购方名称')
    sh.write(0, 13, '购方税号')
    sh.write(0, 14, '购方银行账号')
    sh.write(0, 15, '购方地址电话')
    sh.write(0, 16, '销方税号')
    sh.write(0, 17, '销方名称')
    sh.write(0, 18, '销方地址电话')
    sh.write(0, 19, '销方银行账号')
    sh.write(0, 20, '开票日期')
    sh.write(0, 21, '作废标志')
    # sh.write(1, 21, 'N')
    sh.write(0, 22, '是否报销')
    # sh.write(1, 22, '否'

def w_message(line, row, str):
    sh.write(line, row, str)

first()
x = 1
while x <= len(commodity2):
    w_message(x, 0, invoiceCode)
    w_message(x, 1, invoiceNum)
    if (len(commodity2)) > 1:
        if len(commodity3[x-1]) == 7:
            w_message(x, 2, commodity3[x-1][0])
            w_message(x, 3, ' ')
            w_message(x, 4, commodity3[x-1][1])
            w_message(x, 5, commodity3[x-1][2])
            w_message(x, 6, commodity3[x-1][3])
            w_message(x, 7, commodity3[x-1][4])
            w_message(x, 8, commodity3[x-1][5][0:-1])
            w_message(x, 9, commodity3[x-1][6])
        elif len(commodity3[x-1]) == 8:
            w_message(x, 2, commodity3[x-1][0])
            w_message(x, 3, commodity3[x-1][1])
            w_message(x, 4, commodity3[x-1][2])
            w_message(x, 5, commodity3[x-1][3])
            w_message(x, 6, commodity3[x-1][4])
            w_message(x, 7, commodity3[x-1][5])
            w_message(x, 8, commodity3[x-1][6][0:-1])
            w_message(x, 9, commodity3[x-1][7])
        else:
            print('商品或规格型号存在空格1')
    elif (len(commodity2)) == 1:
        if len(commodity3) == 7:
            w_message(x, 2, commodity3[0])
            w_message(x, 3, ' ')
            w_message(x, 4, commodity3[1])
            w_message(x, 5, commodity3[2])
            w_message(x, 6, commodity3[3])
            w_message(x, 7, commodity3[4])
            w_message(x, 8, commodity3[5][0:-1])
            w_message(x, 9, commodity3[6])
        elif len(commodity3) == 8:
            w_message(x, 2, commodity3[0])
            w_message(x, 3, commodity3[1])
            w_message(x, 4, commodity3[2])
            w_message(x, 5, commodity3[3])
            w_message(x, 6, commodity3[4])
            w_message(x, 7, commodity3[5])
            w_message(x, 8, commodity3[6][0:-1])
            w_message(x, 9, commodity3[7])
        else:
            print(commodity3)
            print('商品或规格型号存在空格2')
    else:
        print('校验代码')

    w_message(x, 10, '专用发票')
    w_message(x, 11, remarks)
    w_message(x, 12, buyer_name)
    w_message(x, 13, buyer_tax)
    w_message(x, 14, buyer_bank)
    w_message(x, 15, buyer_address)
    w_message(x, 16, saler_tax)
    w_message(x, 17, saler_name)
    w_message(x, 18, saler_address)
    w_message(x, 19, saler_bank)
    w_message(x, 20, date)
    w_message(x, 21, 'N')
    w_message(x, 22, '否')

    x += 1

wb.save('example.xls')