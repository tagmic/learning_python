#数组集合部分
classlists=['小明','小红','小花']
#遍历数组
print ('classlists=',classlists);
#查看数组的长度
print('lenght=',len(classlists));
#访问数组中的元素
for name in classlists :
    print('元素-',name);
#向数组中第2个位置插入数据
classlists.insert(2,'小刚');
#向数组的末尾添加数据
classlists.append('小黑');
print (classlists);
#删除末尾的一条数据
classlists.pop();
print (classlists);
#删除下标对应的数据
classlists.pop(1);
print (classlists);
#替换下标对应的数据
classlists[1]='小太阳';
print (classlists);
#数组中包含数组
towlists=['python','java',['sql','web']]
print ('数组',towlists,'长度',len(towlists));
