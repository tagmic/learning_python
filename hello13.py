#在python中一边循环一遍计算的机制叫做生成器generator
generator=(x*x for x in range(1,10))
print (generator)
#迭代出generator中的元素
for x in generator:
    print (x)

