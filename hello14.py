#函数是面向过程编程的基本单元
#函数式变成也可以归纳到面向过程的程序设计，但其思想更接近于数学计算
#越低级的语言越接近计算机语言，抽象程度低，执行效率高。比如C
#越高级的语言越贴近计算，抽象程度高，执行效率低，比如lisp语言


#函数式编程的特点是：允许把函数本身作为参数传入另一个函数，而且允许返回一个函数。
#高阶函数  ，higher-order function
def add(x,y,f):
    return f(x)+f(y)
#上述f可以为任意的一个函数，xy同理
print ('add(10,-10,abs)=',add(10,-10,abs))


#map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数
#依次作用到序列Iterable的每个元素中，并把结果作为新的Iterable返回


#例如
lists=list(range(1,10))
#将lists中的每个元素都乘以2
def cate(x):
    return x*2
#普通的for循环，
from collections import Iterable
def x(l):
    able=isinstance(l,Iterable)
    if able is True:
        L=[]
        for a in l:
            a=cate(a)
            L.append(a)
    return L
print (x(lists));
#使用map处理以上操作

def x1(l,f):
    able=isinstance (l,Iterable)
    if able is True:
        return   map(f,l)
print (list(x1(lists,cate)))

#下面将一组数字转成字符串
l=list(range(10))
s=map(str,l);
#so easy
print (list(s))





#关于reduce的用法，reduce把一个函数作用在一个序列[x1,x2,x3,x4...]上，这个函数
#必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算，其效果就是:
#redece(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
#例子,对一个序列求和可以用reduce实现
from functools import reduce
def app(x,y):
    return x+y
a=reduce(app,list(range(1,10)))
print ('reduce 序列求和:',a,'使用内建函数sum求和:',sum(list(range(1,10))))
#把[1,2,3,4,5,6,7]转换成数字1234567，
from functools import reduce
def fn(x,y):
    return x*10+y
print ('[1,2,3,4,5,6,7]转成连接的数字：',reduce(fn,range(1,8)))




#经过map函数处理过的结果仍然是一个序列对象，只不过是新序列是原序列的每个项经过函数处理过的结果。
#map函数接收两个参数,1个是函数，1个是Iterable(可迭代对象)

#经过reduce函数处理的结果是一个新的对象，
#reduce函数将Iterable(可迭代对象)中的每一个元素经过传入的函数参数进行累计计算
#(计算规则由传入的参数函数决定)
#以上是map函数和reduce函数的区别
#map函數属于内建函数，可以直接使用map(计算规则函数,可迭代对象Iterable)
#reduce函数需要导入部分代码：from functolls import reduce后才可以使用














