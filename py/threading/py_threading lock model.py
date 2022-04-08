#%%1 使用锁实现线程同步：lock
### threading.Lock() / lock.acquire() / lock.release()

import threading
import time
import os
from random import randint
from threading import Thread
from quantframe.utils import tu

threadLock = threading.Lock() # <1>

class MyThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    # tu获取的是三个线程执行任务的总时间，而不是单个线程的时间
    def run(self):

        threadLock.acquire() # <2>

        print(" --> " + self.name + " running, belong to process ID"  + str(os.getpid()) +'\n')
        time.sleep(self.duration)
        print(" --> " + self.name + " over \n")

        threadLock.release() # <3>


def main1():

    start_time = time.time()
    
    t1 = MyThreadClass("Thread#1", 1)
    t2 = MyThreadClass("Thread#2", 1)
    t3 = MyThreadClass("Thread#3", 1)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    
    print("end")

    print("{} seconds".format(time.time() - start_time))

if __name__ == "__main__1":

    main1()



#%%2 锁资源的获取和释放位置对程序的运行影响极大
import threading
import time
import os
from random import randint
from threading import Thread

threadLock = threading.Lock()

class MyThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        threadLock.acquire() 

        print(" --> " + self.name + " running, belong to process ID" + str(os.getpid()) +'\n' )

        threadLock.release() # <1> 在IO操作启动之前把锁资源释放掉
        time.sleep(self.duration)

        print(" --> " + self.name + "over \n")

  

def main2():
    start_time = time.time()
    
    t1 = MyThreadClass("Thread#1", 1)
    t2 = MyThreadClass("Thread#2", 1)
    t3 = MyThreadClass("Thread#3", 1)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("end")

    print("{} seconds".format(time.time() - start_time))

if __name__ == "__main__2":
    main2()


#%%3 重入锁：RLock,可多次获取，相应也要多次释放
### 可以多次acquire的锁，但是每一次获取都需要对应一次release
### 在全部释放之前，不能被其他线程获取
import threading
import time
import random

class Box:

    def __init__(self):
        self.lock = threading.RLock() #<1>
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(box, items):

    print(" N {} items to ADD ".format(items))

    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED one item -> {} item to ADD ".format(items))

def remover(box, items):

    print("N {} items to REMOVE".format(items))

    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item -> {} item to REMOVE ".format(items))

def main3():
    
    items = 10
    box = Box() # <2>
    t1 = threading.Thread(target = adder, args=(box, 10 ) )
    t2 = threading.Thread(target = remover, args=(box, 10 ) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main3()

#%%4 