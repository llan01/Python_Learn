lst=['hello','world','python','php']
#使用遍历循环for遍历列表元素
for item in lst:
       print(item)

#使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
       print(i,'-->',lst[i])#前面是索引，后面是根据索引获取元素

#第三种遍历方式 enumearte
for index,item in enumerate (lst):
       print(index,item)#index是序号，不是索引
#手动修改序号的起始值
for index,item in enumerate(lst,start=1):
       print(index,item)
for index,item in enumerate(lst,1):#start可以省略不写
       print(index,item)