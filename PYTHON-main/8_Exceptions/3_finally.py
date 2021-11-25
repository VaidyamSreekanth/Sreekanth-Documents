'''
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do cleanup process.
'''
try:
    a = '10'    #--> open('test_data.txt')
    b = 20
    print(c) 
    c = a + b   #  fail
   # fh.close()
except:
    print(' Try block got failed')
else:
    print(' Else block ')
finally:
    print(' Finally block ')
