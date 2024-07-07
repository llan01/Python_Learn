#随机产生10个元素，存储到列表中，编写函数获取这个列表中元素的最大值（不能使用内置函数max）
import random
def get_max(lst):
       x=lst[0]#存储元素的最大值
       #遍历
       for i in range(1,len(lst)):
              if lst[i]>x:
                     x=lst[i]
       return x

#调用
lst=[ random.randint(1,100) for item in range(10)]
print(lst)
#计算列表元素的最大值
max=get_max(lst)
print(max)
