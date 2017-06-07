#类和实例
class Student(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def print_data(self):
        print('%s:%s'%(self.__name,self.__age))


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

#实例化实例  __标识属性私有化
s=Student('小明','19')
s.print_data()
print('小明的年龄是:',s.get_age())

#__slots__属性可以设定类都有哪些属性，而不允许添加新的属性，但是__slots__定义的属性只对当前类实例起作用，对继承的子类是不起作用的

class Product(object):
    __solts__=('name','age')#使用tuple定义允许绑定的属性名称


a=Product()
a.name='小红'
a.age='20'
print ('%s:%s'%(a.name,a.age))


