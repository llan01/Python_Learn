lst=[54,56,77,4,567,34]
#(1)排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表：',lst)
print('升序：',asc_lst)
print('降序：',desc_lst)

#(2)reversed 反向
new_lst=reversed(lst)
print(type(new_lst))#<class 'list_reverseiterator'>
print(list(new_lst))

#(3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
#print(type(zipobj))#<class 'zip'>
#print(list(zipobj))

#(4)enumerate 枚举对象，生成索引
enum=enumerate(y,start=1)
print(type(enum))#<class 'enumerate'>
print(tuple(enum))#((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))
print(list(enum))

#(5)all
lst2=[10,20,'',30]
print(all(lst2))#False 有空字符串，布尔值为false
print(all(lst))#ture

#（6）any
print(any(lst2))#Ture

#(7)next 获取元素
print(next(zipobj))#('a', 10)
print(next(zipobj))#('b', 20)

def fun(num):
       return num%2==1 #可能是true,可能是false

obj=filter(fun,range(10))#将range(10)，0-9的整数都执行一次fun操作
print(list(obj))#[1, 3, 5, 7, 9]


def upper(x):
       return x.upper()#转成大写字母
new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))

