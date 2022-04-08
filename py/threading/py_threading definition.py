

#%%1 定义一个线程: 线程接受一个目标函数作为启动函数，就像主线程在main中运行一样。
import threading
import time

def my_func(thread_number): #<1>
    return print('my_func called by thread N{}'.format(thread_number))

def main1():
    for i in range(10):
        t = threading.Thread(target = my_func, args=(i,)) #<2>
        t.start()
        t.join()


if __name__ == "__main__1":
    main1()


#%%2  确定当前线程 thrading.currentThread().getName() 
# 获取当前线程 thrading.currentThread()
def function_A():
    print(threading.currentThread().getName() + str('-> starting \n'))
    time.sleep(3)
    print(threading.currentThread().getName() + str('-> exiting \n'))

def function_B():
    print(threading.currentThread().getName() + str('-> starting \n'))
    time.sleep(2)
    print(threading.currentThread().getName() + str('-> exiting \n'))

def function_C():
    print(threading.currentThread().getName() + str('-> starting \n'))
    time.sleep(1)
    print(threading.currentThread().getName() + str('-> exiting \n'))

if __name__=="__main__2":
    t1 = threading.Thread(name='function_A named by user', target=function_A)
    t2 = threading.Thread(name='function_B named by user', target=function_B)
    t3 = threading.Thread(name='function_C named by user', target=function_C)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

#%%3 定义线程子类:class newclass（Thread):
import time
import os
from random import randint
from threading import Thread

class MyThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print(" --> " + self.name + " running, belong to process ID" + str(os.getpid()) +'\n')
        time.sleep(self.duration)
        print(" --> " + self.name + "over \n")

def main3():
    start_time = time.time()
    
    t1 = MyThreadClass("Thread#1", randint(1,10))
    t2 = MyThreadClass("Thread#2", randint(1,10))
    t3 = MyThreadClass("Thread#3", randint(1,10))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("end")

    print("{} seconds".format(time.time() - start_time))

if __name__ == "__main__":
    main3()


# %%4
