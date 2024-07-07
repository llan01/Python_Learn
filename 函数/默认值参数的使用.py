def happy_birthday(name='娟子姐',age=18):
       print('祝'+name+'生日快乐')#只能是字符串相互连接
       print(str(age)+'生日快乐')

#调用
happy_birthday()#不用传参
happy_birthday('陈梅梅')#位置传参
happy_birthday(age=19)#关键字传参，name采用默认值
#happy_birthday(19)#TypeError: can only concatenate str (not "int") to str，由于19被传给了name,报错

def fun(a,b=2):#a作为位置参数，b默认值参数
       pass

#def fun(a=20,b):#SyntaxError: non-default argument follows default argument  语法错误
       #pass     #当位置参数和关键字参数同时存在的时候，位置参数在后面会报错

#当位置参数和关键字参数同时存在的时候，应该遵循位置参数在前，默认值参数在后