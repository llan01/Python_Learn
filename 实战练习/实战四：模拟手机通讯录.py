#需求：从键盘录入5位好友的姓名和电话，由于通讯录是无序的，所以可以使用集合来实现
#创建一个空集合
s=set()
for i in range(1,6):
       info=input(f'请输入第{i}位好友的姓名和手机号：')
       s.add(info)
#遍历集合
for item in s:
       print(item)