#列表生成式

#例如生成一个1x1,2x2,3x3...10x10的数组list
a=[x*x for x in range(1,11)]
print (a)
#也可以对要生成的数组list做条件
b=[x*x for x in range(1,11) if x%2==0]
print (b)
#还可以使用双层循环，生成全排列
c=[x+y  for x in range(1,10) for y in range(1,10)]
print (c)
#练习题
L=['hello','world',18,'apple',None]
I=[]
for x in L:
    if isinstance(x,str):
        I.append(x)

print (I)
        
