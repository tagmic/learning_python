#迭代，python的for循环抽象程度高于java的for循环。只要是可迭代对象，无论有没有
#下标，都可以使用python的for循环迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print ('key=',key,'value=',d[key])


#如何判断一个对象是否可以迭代，可以使用collections模块的iterable类型来判读

from collections import Iterable
able=isinstance(d,Iterable)
print ('d对象是否可迭代',able)

#迭代器generator


