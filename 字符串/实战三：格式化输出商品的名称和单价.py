#需求：使用列表存储一些商品数据，使用循环遍历输出商品信息，要求对商品的编号进行格式化为6位，单价保留2位小数，并在前面添加人名币符号输出
lst=[
       ['01','电风扇','美的',500],
       ['02','洗衣机','TCL',1000],
       ['03','微波炉','老板',400]
]
print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
       for i in item:
              print(i,end='\t\t')
       print()

#格式化
for item in lst:
       item[0]='0000'+item[0]
       item[3]='￥{0:.2f}'.format(item[3])
print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
       for i in item:
              print(i,end='\t\t')
       print()
