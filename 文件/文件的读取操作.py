def my_read(filename):
       #(1)打开
       file=open(filename,'w+',encoding='utf-8')
       #(2)操作
       file.write('你好啊')#写入完成，文件指针在最后,'啊'后
       #seek 修改文件指针的位置
       file.seek(0)#文件指针跳到'你'之前
       #读取
       #s=file.read()#读取全部
       #s=file.read(2)#两个字符
       #s=file.readline()#读取一行
       #s=file.readline(2)#读取一行中的两个字符
       #s=file.readlines()#读取所有，一行列表中的一个元素，s是列表类型
       #读取”好啊“
       file.seek(3)#3个字节，一个中文占三个字节，utf-8
       s=file.read()#读取全部
       print(type(s),s)
       #(3)关闭
       file.close()
if __name__=='__main__':
       my_read('d.txt')