s='helloworld'
#in的使用
print('e在helloworld中存在吗？',('e' in s))
#not in 的使用
print('e在helloworld中存在吗？',('e' not in s))
#内置函数的使用
print('len()',len(s))
print('max()',max(s))
print('min()',min(s))
#序列对象的方法，使用序列的名称，打点调用
print('s.index()',s.index('o'))#o在s中第一次出现的索引位置4
#print('s.index()',s.index('v'))#ValueError: substring not found,报错，v在字符串中不存在，所以找不到位置
print('s.count()',s.count('o'))#统计o在字符串中出现的次数