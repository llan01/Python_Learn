def happy_birthday(name,age):
       print('祝'+name+'生日快乐')#只能是字符串相互连接
       print(str(age)+'生日快乐')

#关键字传参
happy_birthday(age=18,name='娟子姐')

happy_birthday('韩梅梅',age=18)#一个函数的参数传递中既可以使用位置传参，也可以使用关键字传参

#happy_birthday(name='韩梅梅',18)#SyntaxError: positional argument follows keyword argument

#位置传参在前，关键字传参再后，否则报错
