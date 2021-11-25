'''
1. Identiti opertions are is and is not
2. Using identity operators we can check memory location of objects.
'''

a = 10
b = 10
c = a

# print(' A ID is :', id(a))
# print(' B ID is :', id(b))
# print(' C ID is :', id(c))

#if a is c : print(' IS ')


l = [1,2,3]
l2 = l.copy()
print(' L id is  : ', id(l))
print(' L2 id is : ', id(l2))

if l is not l2 : print(' OK ')

