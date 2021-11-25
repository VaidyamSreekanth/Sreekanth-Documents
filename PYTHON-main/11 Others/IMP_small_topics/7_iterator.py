'''
1. using iterators we can get sequence of values based on demand by using next() function.
2. We can create iterators by using iter() function.
'''

l = [1,2,3,4,5]

#for i in l:
#    print(i)

iter_obj = iter(l)

print(next(iter_obj))

print(next(iter_obj))


for i in iter_obj:
    print(' For loop ', i)



#print(next(iter_obj))