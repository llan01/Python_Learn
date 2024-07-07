#需求：使用input()获取一个字符串，编写并传参，使用isdigit()方法提取字符串中所有的数字，并对提取的数字进行求和计算，最后将存储数字的列表和累加和返回

def get_digit(x):
       s=0#存储累加和
       lst=[]#存储提取出来的数字
       for item in x:
              if item.isdigit():#如果是数字
                     lst.append(int(item))
       #求和
       s=sum(lst)
       return lst,s

#调用
s=input('请输入一个字符串：')
lst,x=get_digit(s)
print('提取的数字列表为：',lst)
print('累加和为：',x)