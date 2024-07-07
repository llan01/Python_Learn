def happy_birthday(name,age):
       print('祝'+name+'生日快乐')#只能是字符串相互连接
       print(str(age)+'生日快乐')

#调用
happy_birthday('娟子姐','20')

#happy_birthday(18,'娟子姐') #TypeError: can only concatenate str (not "int") to str
happy_birthday('娟子姐',18)