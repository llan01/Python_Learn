#个数可变的位置参数
def fun(*para):
       print(type(para))
       for item in para:
              print(item)

#调用
fun(10,20,30,40)
fun(10)
fun([11,22,33,44])#将整个列表当作一个参数传递
#在调用是，参数前面加一颗星，将列表进行解包
fun(*[11,22,33,44])

#个数可变的关键字参数
def fun2(**kwpara):
       print(type(kwpara))
       for key,value in kwpara.items():
              print(key,'-----',value)

#调用
fun2(name='娟子姐',age=18,height=170)#关键字参数
d={'name':'娟子姐','age':18,'height':170}
#fun2(d)#TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)