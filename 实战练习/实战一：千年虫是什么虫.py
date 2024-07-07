#需求：已知一个列表中存储的员工的出生年份[88,89,90,98,00,99],由于时间比较久，出生的年份均为2位整数，现需要2位年份前加19，如果年份是00，将需要加上200
lst=[88,89,90,98,00,99]
#遍历列表的方式
""" for index in range(len(lst)):
       if str(lst[index])!=0:
             lst[index]='19'+str(lst[index])#拼接年份，再赋值
       else:
             lst[index]='200'+str(lst[index])
print('修改后的年份列表：',lst) """

#使用enumerate()函数
for index,value in enumerate(lst):
      if str(lst[index])!=0:
             lst[index]='19'+str(value)#拼接年份，再赋值
      else:
             lst[index]='200'+str(value)
print('修改后的年份列表：',lst)