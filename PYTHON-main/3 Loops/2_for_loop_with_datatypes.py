'''
1. We can use all data types in for loop except number.
'''

## string iterate character by characters
s = 'sri ram'
for c in s:
    print(c)

## list iterate value by value 
names = ['sri','ram','kumar','nagesh', 'balu']
for name in names:
   print(name)


# Dictionary iterate based on key
emp_det = {'name':'sri', 'eid':35, 'dname':'IT', 'name':'ram'}
# for k in emp_det:
    # print(k, emp_det[k])

## Number object does not support for iterable
NO =  345
for n in NO: print('OK')
