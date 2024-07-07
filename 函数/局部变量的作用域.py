def calc(a,b):
       s=a+b
       return s

#print(a,b,s)#NameError: name 'a' is not defined,函数中定义的变量是局部变量
result=calc(10,20)
print(result)
