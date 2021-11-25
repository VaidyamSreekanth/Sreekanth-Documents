'''
1. using args(*) we can takes N number of arguments
2. it will atke 0 to many values in tuple format
'''
def add(b=5, a, *c):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)

add(3, 67, 7,54,'sri')


add(7, 8, 4,6,3)


