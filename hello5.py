#循环 for 子元素 in 数组 :格式
#例如 计算1-10之内的整数和
sum=0;
data=[1,2,3,4,5,6,7,8,9];
for d in data:
    sum+=d;

print ('sum=',sum);
#计算100以内的整数和怎么办，使用range(x)函数,可以生成0到x的整数数组
sum100=0;
data100=range(100);
for d100 in data100:
    sum100+=d100;
print ('100以内的整数和=',sum100);


#while循环  只要满足条件就不停的循环，条件不满足就跳出循环
#计算100以内的奇数和
sum1=0;
n=99;
while n>0:
    sum1+=n;
    n=n-2;
print ('100以内的奇数和为',sum1);
