'''
1. Threading is used to run multiple functions/jobs concurrently(at the same time)
2. Using threading module we can achive threading in python.
## target: the function to be executed by thread
## args: the arguments to be passed to the target function
## name: We can specify a name to the thread
## join: Using join function we keep a thread to wait till ending the thread
'''
import threading
import time

def first_fun():
    print(' \n first_thread started')
    time.sleep(3)
    print(' \n first_thread ended')

def second_fun(a,b):
    print(' \n second_thread started')
    time.sleep(7)
    print(' \n second_thread ended')

#first_fun()
#second_fun(3,4)


ft = threading.Thread(target=first_fun)
st = threading.Thread(target=second_fun, args=('sriram','chowdary'))

ft.start()
#ft.join()
st.start()



