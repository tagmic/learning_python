#返回函数
#高阶函数除了可以接收函数作为参数以外，还可以把函数作为结果值返回


#通常情况下，可变参数的求和函数是这样定义的
def my_sum(*args):
    ax=0
    print (args)
    for x in args:
        ax+=x
    return ax
#计算1-10序列的元素和
print ('1---10之和：',my_sum(1,2,3,4,5,6,7,8,9),'内建函数执行',sum(range(1,10)))

#闭包
