#需求：使用input()从键盘获取一个字符串，判断这个字符串在列表中是否存在（函数体不能使用in)，返回结果为True或False
def get_find(s,lst):
       for item in lst:
              if s==item:
                     return True
       return False
lst=['hello','world','python']
s=input('请输入您要判断的字符串：')
result=get_find(s,lst)
print('存在' if result else '不存在')#三元运算符 if...else的简写，if result==True if result利用对象的布尔值