#StringIO和BytesIO
#很多时候数据读写不一定是文件，也有可能在内存中读写，例如StringIO和BytesIO

#样例，把字符串写入StringIO，需要先创建一个StringIO，像文件一样写入即可
from io import StringIO
f=StringIO()
f.write('hello world')#写入即可
print (f.getvalue())#getvalue()函数用于获得写入后的字符串
#读取StringIO可以用一个字符串初始化该IO，然后类似读文件
s=StringIO('一支穿云箭，千军万马来相见')
while True:
    a=s.readline()
    if a=='':
        break
    print(a.strip())


#BytesIO，操作二进制的数据的IO
from io import BytesIO
b=BytesIO()
b.write('中文'.encode('utf-8'))#此处写入的不是字符串，而是该字符串经过utf8编码的二进制字节Byte
print(b.getvalue())
#BytesIO的读取方式和StringIO的读取方式一样
print(b.read())

