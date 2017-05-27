#函数的参数以及默认参数,例如求某个数的n次方,n的默认参数是0，x的默认参数为1
def power(x=1,n=0):
    s=1;
    while n>0:
        n=n-1;
        s*=x;
    return s
#测试2的3次方
print('2的3次方',power(2,3));
print('2的0次方',power());
#默认函数可以降低了函数的调用难度

#规避空数组默认参数的坑,
def add_end (list=None,entity=None):
    if list is None:
        list=[]
    if entity is None:
        entity='None'
    list.append(entity);
    return list
print ('规避默认参数异常的坑',add_end())

#可变参数函数的设定即参数前添加*
#例如计算一组数字a,b,c....请计算a²+b²+c²....的值
def cale(*numbers):
    sum=0;
    for n in numbers:
        sum+=n*n;
    return sum
print ('计算1->4平方和',cale(1,2,3,4),'计算0的平方和',cale());
#当有一个数组需要作为一个参数传递时也可以这样做，在数组前加*
a=[2,4,6,8]
print ('计算数组[2,4,6,8]的平方和',cale(*a));

#关键字参数
#可变参数的函数允许你传入0个或者多个任意参数，这些可变参数在函数调用的时候自动组装成一个tuple
#而关键字参数允许你传入必选参数以外，还可以传入任意个关键字参数
#比如录入学生信息时，提供学生姓名，男女，作为必选参数，居住地，电话号码等可以作为关键字参数
def person(name,age,**kw):
    #kw为关键字参数
    print('name:',name,'age:',age,'others:',kw)
person('小明','18',city='深圳',tel=13534199860);
#关键字参数的检测和使用
def person1(name,age,**kw):
    if 'city' in kw.keys():
        print (name,'所居住的城市是:',kw['city'])
    if 'tel' in kw.keys():
        print (name,'的电话是:',kw['tel'])
    print('name:',name,'age:',age,'others:',kw)
person1('小红','18',city='深圳',tel=13534199860);


#在Python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数，命名关键字参数

