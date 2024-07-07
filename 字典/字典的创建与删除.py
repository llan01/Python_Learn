#(1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)#当我们的键相同时。value值进行了覆盖

#(2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)#输出<zip object at 0x000002CC806FCD00>
print(list(zipobj))#将映射对象转成列表类型：[(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]列表当中的元素是元组类型
d=dict(zipobj)
print(d)#{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}字典类型

#使用参数创建字典
d=dict(cat=10,dog=20)
print(d)


t=(10,20,30)
print({t:10})#t是key,10是value,元组是可以作为字典中的key

""" lst=[10,20,30]
print({lst:10})#TypeError: unhashable type: 'list',列表不能作为key的，因为列表是可变数据类型，所以可变数据类型是不能作为字典中的键 """

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
#字典的删除
#del d
#print(d)# NameError: name 'd' is not defined. Did you mean: 'id'?

