#需求：判断三个变量是否能构成一个三角形，如果不能则抛出异常Exception异常，
# 显示异常信息‘a,b,c不能构成三角形',如果可以构成则显示三角形三个边长
try:
       a=int(input('请输入第一条边长：'))
       b=int(input('请输入第二条边长：'))
       c=int(input('请输入第三条边长：'))
       if a+b>c and a+c>b and b+c>a:
              print('三角形的边长为：a={0},b={1},c={2}'.format(a,b,c))
              print('三角形的边长为：',a,b,c)
              print(f'三角形的边长为：{a},{b},{c}')
       else:
              raise Exception('{0},{1},{2},不能构成三角形'.format(a,b,c))
except Exception as e:
       print(e)