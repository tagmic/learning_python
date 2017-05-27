#python内建函数filter用来过滤序列
#和map类似，filter也需要接收一个函数参数和一个可迭代对象Iterable
#和map的区别是，filter函数会根据传入的函数参数(计算规则函数)作用到Iterable中的每一个元素中去，
#然后根据传入的计算函数的返回值True或者False来决定保留该元素还是丢弃该元素


#例如，过滤调序列中的偶数
l=list(range(10))
def is_odd(x):
    return x%2==1
print ('过滤掉1-10序列中的奇数:',list(filter(is_odd,l)))
#重申，filter函数是将序列的每个元素经过传入的计算规则函数的返回值True/False来决定序列中的每个元素的存留

#例子，将一个序列中的空字符串过滤掉
ls=['小明','','小花','小红','小黑','小小']
def remove(x):
    return  x.strip()
print ('过滤调序列中空字符串：',list(filter(remove,ls)))

#sorted函数，即排序算法（排序算法的核心就是比较两个元素的大小）.
#接收两个参数，一个是函数名为key的计算规则参数，一个是序列，返回一个按照规则参数整理元素后的序列


#例子  ,默认从小到大？可以不用传入计算规则参数
print ('排序[1,2,8,3,-5,9]----',sorted([1,2,8,3,-5,9]))

print ('按照绝对值abs排序[1,2,8,3,-5,9]----',sorted([1,2,8,3,-5,9],key=abs))
#例子，字符串排序,  默认情况下是按照字符串的ASCLL的大小进行比较的，
#由于'Z'<'a'，所以大写的Z会排在小写的a前面
print ('字符串排序:',sorted(['bob', 'about', 'Zoo', 'Credit']));
#忽略字符串的大小写进行排序
print ('字符串排序:',sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower));
#忽略字符串的大小写进行反向排序
print ('字符串反向排序:',sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#练习
#按名字排序
L=[('Bob',75),('adam',92),('Abart',66),('Lisa',88)]
from collections import Iterable
def name(x):
    able=isinstance(x,Iterable)
    if able is True:
        #取出名字,并忽略大小写
        return str.lower(x[0])
print ('按姓名排序',sorted(L,key=name))
#按成绩排序
def fenshu(x):
    able=isinstance(x,Iterable)
    if able is True:
        return x[1]
print('按成绩排序',sorted(L,key=fenshu))
#把成绩最高的放在前面
print('按成绩最高排序',sorted(L,key=fenshu,reverse=True))






