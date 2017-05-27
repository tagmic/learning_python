#函数调用
#求一个数的绝对值 abs(x)
print ('-10的绝对值是',abs(-10))
#求多个数字中的最大数
lists=[1,3,5,7,12];
print ('lists数组中最大的数是',max(lists));
#数据类型转换  int(x)  str(x)  bool(x)
#函数别名
x=abs;
print(x(-12));

#定义一个函数需要使用def语句，需要依次写出函数名，括号，括号中的参数和冒号；
#使用return做语句的返回值

def my_abs(x):
    #类型检查
    if not isinstance (x,(int,float)):
        raise TypeError('您传入的数据类型异常，请检查代码');
    if x>=0:
        return x;
    else:
        return -x;

#调用自定义的函数
print ('自定义的绝对值函数,计算-20的绝对值',my_abs(-20))
#空函数,pass语句标识什么事都不用做,当然也可以运用到循环语句中，有点类似continue的含义
def nop():
    pass
#输入类型错误的my_abs函数
#print ('my_abs函数输入错误类型参数',my_abs('A'));


#返回多个值的函数
import math;
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
print (move(100,100,50,50));

