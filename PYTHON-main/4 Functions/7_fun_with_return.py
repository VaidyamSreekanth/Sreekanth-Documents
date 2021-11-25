'''
1. Return keyword used to return value from function.
2. After executiong return keyword function will terminate
3. We can use many return keywords in side a function
'''

def add(a=10,b=25):
    print(' Before return')
    if b > 31 : return  'ok'
    print(' After return')

ret = add(20,25)
print(' return value is :', ret)






