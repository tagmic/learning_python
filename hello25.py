#IO编程
#读文件，使用python内置的open的函数，传入文件名和标识符
try:
  f=open('test.txt','r')#r表示读
  print(f.read())
finally:
    if f:
        f.close()
#python引入了with语句来自动帮我们close文件读写操作

with open('test.txt','r') as f:
    for line in f.readlines():#每次只读一行
        print(line.strip())#去掉每行的\n符号

#file-like Object
#像open函数返回的这种有个read()方法的对象，在python中统称为file-like Object
#除了file外也可以是内存的字节流，网络流，自定义流等，file-like Object不要求特定类继承，只要写个read()方法就行

#StringIO就是内存中创建的file-like Object 常用作临时缓冲

#二进制文件，一般的文本文件使用open('文件','r')的形式，像图片，音频需要使用二进制的读取方法

with open('test.png','rb') as f:
    for line in f.readlines():
        print(line.strip())
    
#字符编码，要读取非utf-8编码的文本文件，需要给open函数传入encoding参数
with open('test.txt','r',encoding='gbk') as f:
    for line in f.readlines():
        print(line.strip())

#写文件
with open('test.txt','w') as f:
    f.write('hello,java')

