#多线程
#python的标准库提供了多线程模块，threading
import time,threading
#新线程执行的代码
def loop():
    print('thread %s is running ...'%threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s >>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended '%threading.current_thread().name)
print('thread %s is running...'%threading.current_thread().name)#主线程
t=threading.Thread(target=loop,name='loopThrad')#子线程运行的函数以及对子线程的名字标记
t.start()#子线程
t.join()#子线程
print('thread %s ended '%threading.current_thread().name)#主线程
#多线程操作同一变量线程锁的问题lock
#多线程共享的变量
score=0
lock=threading.Lock()
def change_it(n):
        global score#global语句，声明变量全局使用
        score+=n
        score-=n
   
def run_thread(n):
    for x in range(100):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1=threading.Thread(target=change_it,args=(5,))
t2=threading.Thread(target=change_it,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('score=',score)
#线程锁的好处是能保证某段关键的代码只有由一个线程从头到尾完整的执行，坏处是阻止了多线程的并发，线程锁的代码只能单线程模式执行
#降低运行效率


#多核CPU
#python不能使用多线程实现多核任务，可以使用多进程实现多核任务【GIL锁机制】
