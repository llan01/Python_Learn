def my_write():
       #(1)(创建)打开文件
       file=open('D:/python_demo/a.txt','w',encoding='utf-8')
       #(2)操作文件
       file.write('伟大的中国梦')
       #(3)关闭
       file.close()
#读取
def my_read():
       #(1)（创建）打开文件
       file=open('D:/python_demo/a.txt','r',encoding='utf-8')
       #（2）操作文件
       s=file.read()
       print(type(s),s)
       #(3)关闭文件
       file.close()
#主程序运行
if __name__=='__main__':
       #my_write()
       my_read()