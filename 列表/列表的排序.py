lst=[4,56,3,78,20,56,89]
print('原列表：',lst)

#排序，默认升序
lst.sort()#排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序：',lst)

#降序
lst.sort(reverse=True)
print('降序：',lst)
print('-'*40)
lst2=['banana','apple','Cat','Orange']
print('原列表：',lst2)
#升序排序，先排大写，再排小写
lst2.sort()
print('升序：',lst2)
#降序排序，先排小写，再排大写
lst2.sort(reverse=True)
print('降序：',lst2)
#忽略大小写进行比较
lst2.sort(key=str.lower)#都转成小写再排序
print(lst2)

print('-'*80)
#内置的sorted对列表进行排序
asc_lst=sorted(lst)
print('升序',asc_lst)
print('原列表',lst)
desc_lst=sorted(lst,reverse=True)
print('降序：',desc_lst)
print('原列表：',lst)

#忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表：',lst2)
print('排序后的列表：',new_lst2)
