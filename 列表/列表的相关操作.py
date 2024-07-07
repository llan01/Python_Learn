lst=['hello','world','python']
print('原列表：',lst,id(lst))
#增加元素的操作
lst.append('sql')#称之为可变数据类型：元素个数增加后，内存地址没变
print('增加元素之后：',lst,id(lst))

#使用insert(index,x)在指定的index位置上插入元素x
lst.insert(1,100)#在索引为1的地方插入一个元素，其他元素后移
print(lst)

#列表元素的删除
lst.remove('world')
print('删除元素之后的列表：',lst,id(lst))

#使用pop（index）根据索引将元素取出，然后删除
print(lst.pop(1))
print(lst)

#清楚列表中所有的元素clear()
#lst.clear()
#print(lst,id(lst))

#列表的反向输出
lst.reverse()
print(lst)

#列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改
#根据索引进行修改元素
lst[1]='mysql'
print(lst)