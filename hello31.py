#ThreadLocal本身是一个全局变量，每个线程都可以使用它来保存使用属于每个线程的私有数据
#这些私有变量对于其他线程来说是不可见的，而global语句声明的全局变量对于其他线程是可见可操作的
import threading
#创建全局threadlocal对象
local_school=threading.local()
def process_student():
    #获取当前线程关联的全局变量
    std=local_school.student
    print('%s (in %s)'%(std,threading.current_thread().name)+'\n')
def process_thread(name):
    #把当前线程的变量绑定到全局threadlocal对象上
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('小明',),name='A班')
t2=threading.Thread(target=process_thread,args=('小红',),name='B班')
t1.start()
t2.start()
t1.join()
t2.join()
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库链接，http请求，用户身份信息等

