s='伟大的中国梦'
#编码str->bytes
scode=s.encode(errors='replace')#默认utf-8，英文占1个字节，中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace')
print(scode_gbk)#gbk，英文占1个字节，中文占2个字节

#编码中的出错问题
s2='耶✌'
scode_error=s2.encode('gbk',errors='replace')#\xd2\xae?,其中符号替换成问好
print(scode)
scodeerror=s2.encode('gbk',errors='ignore')#'\xd2\xae',其中符号不进行编码
print(scode)
#scodeerror=s2.encode('gbk',errors='strict')#报错：UnicodeEncodeError: 'gbk' codec can't encode character '\u270c' in position 1: illegal multibyte sequence
#print(scode)

#解码过程bytes->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))