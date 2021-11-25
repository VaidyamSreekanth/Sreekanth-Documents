'''
1. Call by Reference :- it will copy object memory location
2. Call by Value     :- It will copy value

    Python is a call by Reference
    
    id() ==> Id function is used to find memory location of object.
'''

# a = 10
# b = 10
# c = a

# print(' id of a :', id(a))
# print(' id of b :', id(b))
# print(' id of c :', id(c))

l = [1,2,3]

l2 = l

#l2 = l.copy()
l.append(45)

print(' l id is  :', id(l), l)
print(' l2 id is :', id(l2), l2)

