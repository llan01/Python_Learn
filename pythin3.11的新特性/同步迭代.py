fruits={'apple','orange','pear','grape'}#集合是无序的，所以后面输出没有顺序可言
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
       match f,c:
              case 'apple',10:
                     print('10个苹果')
              case 'orange',3:
                     print('3个橘子')
              case 'pear',4:
                     print('4个梨')
              case 'grape',5:
                     print('5个葡萄')

fruits=['apple','orange','pear','grape']#列表是有序的，所以后面按顺序输出
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
       match f,c:
              case 'apple',10:
                     print('10个苹果')
              case 'orange',3:
                     print('3个橘子')
              case 'pear',4:
                     print('4个梨')
              case 'grape',5:
                     print('5个葡萄')