#大小写转换
s1='HelloWorld'
new_s2=s1.lower()
print(s1,new_s2)

new_s3=s1.upper()
print(s1,new_s3)

#字符串的分隔
e_mail='ysj@126.com'
lst=e_mail.split('@')
print('邮箱名：',lst[0],'邮箱服务域名：',lst[1])

#
print(s1.count('o'))#'o'在字符串中出现了2次

#检索操作
print(s1.find('o'))#'o'在字符串s1中首次出现的位置
print(s1.find('p'))#-1,即没有找到

print(s1.index('o'))
#print(s1.index('p'))#ValueError: substring not found

#判断前缀和后缀
print('demo.py'.endswith('.py'))#True
print('text.txt'.endswith('.txt'))#True
print(s1.startswith('H'))#True,字符串s1是以'H'开头的嘛
print(s1.startswith('P'))#True