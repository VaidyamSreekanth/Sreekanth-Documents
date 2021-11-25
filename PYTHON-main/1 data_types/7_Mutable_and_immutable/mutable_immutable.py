'''
1. Mutable Objects :- 
    1. Mutable objects are changable.
    2. Memory location will be same after changing value also.
    3. Mutable data types are :- list,Dictionary and set
2. Immutable Objectss :- 
    1. Immutable objects are not changable.
    1. Memory location will be different  after changing value.
    3. Mutable data types are :- Number,String and tuple

    id() ==> Id function is used to find memory location of object.
'''

## For Number
# n = 123
# print(' N address before edit:', id(n))
# n = 222
# print(' N address after edit :', id(n))

## For string
# name = 'sri'
# print(' \n name address before edit :', id(name))
# name = 'ram'
# print(' \n name address after  edit :', id(name))

## For List
# names = ['sri','ram','balu']
# print(' \n names address before edit :', id(names))
# names.append('nagesh')
# print(' \n names address after edit  :', id(names))
# print(' \n names after edit :', names)


## For set
# names = {'sri','ram','balu'}
# print(' \n set address before edit :', id(names))
# names.add('OK')
# print(' \n set address after edit  :', id(names))
# print(' \n names :', names)

## For dictionary
emp_det = {'name':'sri','dname':'IT'}
print(' \n emp_det addredd before edit :', id(emp_det))
emp_det['eid'] = 45
print(' \n emp_det address after edit  :', id(emp_det))
print(' \n emp_det :', emp_det)


