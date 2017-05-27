#条件判断if...else if...else
age=input('please inout yout age\n');
if int(age)>18:
    print('你是一个年轻人啊');
elif int(age)>12 and int(age)<18:
    print('同学,好好读书啊');
else:
    print ('你还是太年轻啊');
