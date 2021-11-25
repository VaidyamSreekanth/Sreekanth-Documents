'''
1. threading.activeCount(): Returns the number of total Python thread that are active. 

'''

import threading
import time


def fun1():
    time.sleep(1)

def fun2():
    print(' \n Total threads count is :::::', threading.activeCount())


t1 = threading.Thread(target=fun1, name='add')
t2 = threading.Thread(target=fun2, name='sub')

#t1.start()
t2.start()

