'''
1. Return keyword used to return value from function.
2. After executiong return keyword function will terminate
3. We can use many return keywords in side a function
'''

def add(a=20,b=30):
    if a > 13: return 'ok'
    print(' Before return')
    return a + b
    print(' After return')
    if a == 20: return 'sriram'

#print(add(15))

ret = add()
print(' return value is :', ret)



