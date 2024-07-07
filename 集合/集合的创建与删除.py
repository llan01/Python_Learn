#{}直接创建集合
s={10,20,30,40}
print(s)
#集合中只能存储不可变类型
""" s={[10,20],[30,20]}#列表是可变类型
print(s)#报错：TypeError: unhashable type: 'list' """
#使用set()创建集合
s=set()#创建了一个空集合,空集合的布尔值是False
print(s)
s={}#创建的是集合还是字典呢？
print(s)
print(s,type(s))#{} <class 'dict'>

s=set('helloworld')#集合是无序的，而且是不重复的
print(s)

s2=set([10,20,30])#序列
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列当中的一种
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合当中存在嘛？',9 in s3)
print('9在集合当中存在嘛？',9 not in s3)

#集合的删除
del s3
print(s3)#NameError: name 's3' is not defined. Did you mean: 's'?