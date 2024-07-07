a=100

def calc(x,y):
       return a+x+y
print(a)
print(calc(10,20))
print('-'*30)

def calc2(x,y):
       a=200 #局部变量  局部变量和全局变量的名称相同
       return a+x+y #当全局变量和局部变量的名称相同时，局部变量的优先级高
print(calc2(10,20))#使用的是局部变量a
print(a)

def calc3(x,y):
       global s #全局变量
       s=300  #声明和赋值必须分开执行
       return s+x+y

print(calc3(10,20))
print(s)