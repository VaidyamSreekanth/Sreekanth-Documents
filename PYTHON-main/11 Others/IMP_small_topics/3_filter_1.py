'''
1. The filter() method filters the given sequence with the help of a function and retun filter object.
2. filter taks two parameters one is function another one is iterable object
'''

## Filtr with normal function
def add(a):
    if a >= 3 : return a

#fo = filter(add,[1,2,3,4,5])
#print(list(fo))

## Filter with lambda function
fo = filter(lambda a: a > 2,[1,2,6,4,5])
print(list(fo))

