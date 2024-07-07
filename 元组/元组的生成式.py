#生成式
t=(i for i in range(1,4))
print(t)
""" t=tuple(t)
print(t) """
#遍历
#for item in t:
       #print(item)
#遍历过一遍之后不能再次遍历
print(t.__next__())#只能用于生成式，且一次只能遍历一个
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)#输出为空，用next()方法后，元组中的已经没有元素了
