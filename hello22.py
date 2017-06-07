#多重继承
class A(object):
    def run(self):
        print ('A RUN')
class B(object):
    def pop(self):
        print('B POP')
class C(A,B):
    pass
s=C()
s.run()
s.pop()
#定制类
#__str()__的使用
class Student(object):
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return 'Student object(name:%s)'%self._name
    __repr__=__str__
print(Student('小明'))#Student object(name:小明)
a=Student('小花')
print(a)
#如果一个类想被遍历，那就必须实现一个__iter__()的函数，该方法返回一个迭代对象
#然后Python语言的for循环会不断的调用迭代对象的__next__()函数
class Fib(object):
    def __init__(self):
        self.a ,self.b=0,1#初始化两个计数器a和b

    def __iter__(self):
        return self#实例本身就是迭代对象，返回本身

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b#计算下一个值
        if self.a>100000:#退出循环
            raise StopIteration()
        return self.a#返回下一个值
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for x in Fib():
    print ('x=',x)
#如果要该对象表现的像数组那样取元素list[2]还需要实现__getitem__()函数
print(Fib()[7])
#__getitem__()传入的参数可能是一个int，也可能是一个切片slice，多家切片判断

