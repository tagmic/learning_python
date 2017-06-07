#错误处理try:except as e: finally:
try:
    print('try......')
    r=10/2
    print('result :',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally......')
print('end')
#python中所有的错误都是从BaseException中派生的，如果错误没有被捕获，它就会向上抛
#最后呗python解释器捕获，打印一个错误日志，然后程序退出


#pathon内置的logging模块可以用来捕获日志

import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
            logging.exception(e)
main()
print('END')
#因为错误是class，所以捕获一个错误就是捕获该一个calss的实例
