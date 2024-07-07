#format
print(format(3.14,'20'))#数值型默认右对齐
print(format('hello','20'))#字符型默认左对齐
print(format('hello','*<20'))#<表示左对齐，*表示填充符号，20表示显示的宽度
print(format('hello','*>20'))
print(format('hello','*^20'))#居中对齐


print(format(3.1415926,'.2f'))#3.14
print(format(20,'b'))#二进制
print(format(20,'o'))#八进制
print(format(20,'x'))#十六进制
print(format(20,'X'))

print('-'*40)
print(len('helloworld'))#计算长度
print(len([10,20,30,40,50]))


print('-'*40)
print(id(10))#内存地址
print(id('helloworld'))
print(type('hello'),type(10))
print(eval('10+30'))
print(eval('10>30'))

