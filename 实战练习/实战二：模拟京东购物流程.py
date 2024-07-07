#需求：从键盘录入5个商品信息（1001手机）添加到商品列表中，展示商品信息，提示用户选择商品，用户选中的商品添加到购物车中（购物车中的商品要逆序），用户选中的商品不存在需要有相应的提示，当用户输入“q“时循环结束，显示购物车中的商品

#创建一个空列表
lst=[]
for i in range(5):
       goods=input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
       lst.append(goods)
#输出所有的商品信息
for item in lst:
       print(item)
#创建一个空列表，用于存储购物车中的商品
cart=[]
while True:
       flag=False #代表没有商品的情况
       num=input('请输入要购买的商品编号：')
       #遍历商品列表，查询一下
       for item in lst:
              if num==item[0:4]:#切片操作，从商品中切除序号
                     flag=True#代表商品已找到
                     cart.append(item)#添加到购物车中
                     print('商品已添加到购物车')
                     break #退出的时是for循环
       if not flag and num!='q': #not flag 等价于flag==False
              print('商品不存在')
              
       if num=='q':
              break #退出的才是while循环
print('-'*50)
print('您的购物车里已选择的商品为：')
cart.reverse()
for item in cart:
       print(item)