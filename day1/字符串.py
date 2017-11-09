# msg = ['a','b','c','d']
# msg.index(1,'1')
# print(msg)

msg1 = 'my {name} is {john} ---'
print(msg1.index('a'))#用来判断字符串中是否有a
print(msg1.lstrip('m'))#lstrip() 方法用于截掉字符串左边的空格或指定字符。
print(msg1.strip('-'))#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
print(msg1.center(40,'-'))#center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
print(msg1.capitalize())#首字母大写
print(msg1.count('n'))#统计字符串中有多少个n
print(msg1[msg1.find ('n'):5])#使用find找到第一个n的下标，然后在切片
print(msg1.format_map({'name':'name','john':'BO'}))
print('ab23'.isalnum())#是不是阿拉伯文
print('1A'.isidentifier())#判断是否是一个合法的变量名
print('1A'.isspace())#判断是不是空格
print('+'.join(['1','2','3','4']))#列表中每个元素中间加上想要加的字符串
print(msg1.ljust(50,'*'))
print(msg1.rjust(50,'/'))
print('JoHn'.lower())#全部转换为小写
print('jOhN'.upper())#全部转换为大写
print('---#'.strip('-'))#去除--#左右两边的-
p = str.maketrans('abcdef','123456')
print('alex li'.translate(p))
print('alex li'.replace('l','L',1))#替换，数字是替换几个
print('alex li'.rfind('l'))
print('al ex lil'.split('l'))#以l为分隔符，把该字符串分割为列表
print('Alex Li'.swapcase())#大小写互换
print('lex li'.zfill(50))