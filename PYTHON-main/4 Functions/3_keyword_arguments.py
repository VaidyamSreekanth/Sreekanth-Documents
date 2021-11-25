'''
1. We can pass values based on parameter name.
2. Keyword arguments should follow positional argument.
'''

def add(a, b, c):
    print(' A value is :', a)
    print(' B value is :', b)
    print(' C value is :', c)

#add(4, 7)

#add(b=7,a=6)

##  Doesn't accept multiple values for single parameter
#add(4,a=78)

add(78, b=8, c=4)


