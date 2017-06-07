#线程vs进程

#多进程的优点是稳定性高，因为一个进程崩溃了不会影响到主进程和其他子进程的工作
#多线程若是其中一个线程崩溃，可能导致主进程崩溃

#计算密集型任务：需要进行大量计算的任务，要高效的利用CPU，计算密集性的任务同时进行的数量应等于CPU的核心数
#IO密集行任务：涉及到网络，磁盘IO的任务都是IO密集型任务，CPU消耗少，对于IO密集型
#任务，任务越多，CPU效率就越高。常见的有web应用

#协程

#分布式进程，在thread和Process中，应当优先选择process，因为process更稳定，而且，process可以分布到
#多台机器上，而thread最多只能分布到同一台机器的多个CPU上

#python的multiProcessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上
#一个服务进程作为调度进程，将任务分配到其他进程中，依靠网络通信。managers对这块有很好的支持
#原有的queue可以继续使用，服务进程负责启动queue，把queue注册到网络上，然后在queue里面写入任务

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分布式: master
import random, queue
# managers子模块支持把多进程分布到多台机器上
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BashManager继承
class QueueManager(BaseManager):
    pass

# 1. 把两个Queue都注册到网络上, callable关联queue对象
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def test():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 2. 绑定端口, 设置验证码
    manager = QueueManager(address=('127.0.0.1', 5008), authkey=b'abc')
    # 3. 启动Queue
    manager.start()

    # 4. 通过网络获得Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 5. 放置任务
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)
    # 6. 获取结果
    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 7. Close
    manager.shutdown()
    print('********* Master exit *********')

if __name__  == '__main__':
    test()
