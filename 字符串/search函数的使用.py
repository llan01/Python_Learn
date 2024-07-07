import re
pattern='\d\.\d+'#‘+’限定符.\d 0-9数字出现1次或多次  开始是数字，中间除了\n的任意字符，最后是数字，+匹配前面的数字一次或多次
s='I study Python3.11 every day Python2.7 I love you'
match=re.search(pattern,s)


s2='4.10 Python I study every day'
s3='I study every day'
match2=re.search(pattern,s2)
match3=re.search(pattern,s3)
print(match)
print(match2)
print(match3)

print(match.group())
print(match2.group())
