#调试
#1,断言  assert的使用
def foo(s):
    n=int(s)
    assert n!=0,'n is zore!'
    return 10/n
def main():
    foo('1')
print (main())
#2,logging的打印
import logging
logging.basicConfig(level=logging.INFO)
s='1'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
#logging日志级别 debug,info,error,warning，当我们把level指向info时，debug就不起作用了同理。。。。
#3，pdb，python的调试器，让程序以单步形式运行

import pdb
a='0'
b=int(a)
pdb.set_trace()#运行到此处会暂停
print(10/b)
