'''
1. threading.currentThread(): Returns the currentThread object
'''
import threading
import time


def fun1():
    print(' \n Fun1 thread name is :::::', threading.currentThread().getName())

def fun2():
    print(' \n Fun2 thread name is :::::', threading.currentThread().getName())


t1 = threading.Thread(target=fun1, name='add')
t2 = threading.Thread(target=fun2, name='sub')

t1.start()
t2.start()

