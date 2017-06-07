#序列化，把变量从内存中变成可存储或传输的过程称为序列化，python中叫pickling
#序列化之后，就可以把序列化后的内容写入磁盘或者通过网络传输到别的机器上
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
#python提供了pickle模块来实现序列化
import pickle
d=dict(name='Bob',age=20,score=99)
pickle.dumps(d)#该方法是将任意一个对象序列化成一个bytes，然后可以把该bytes存入文件
#另外一钟方法，pickle.dump()直接把对象序列化后写入file-like Object
f=open('test.txt','wb')
pickle.dump(d,f)
f.close()
#读取磁盘中的内容
f=open('test.txt','rb')
c=pickle.load(f)
f.close()
print(c)


#JSON
import json
d=dict(name='小明',age=20,score=100)
json.dumps(d)
print(d)
#python的dict可以直接序列化为JSON的{}
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
a=Student('小花',18,99)
print(json.dumps(a,default=lambda obj:obj.__dict__))#转成json
