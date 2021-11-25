'''
1. List is used to store multiple values and we can do operation on each value based on index.
2. Using square brackets "[]" we can create a list
3. List is a mutable object

            -5        -4     -3       -2   -1
names = ['sriram', 'ramu','ganesh', 999, 98.90]
            0         1       2       3     4

'''
# To create a list
names = ['sri','kumar','balu','ram', 567, 99.9]

# To update a particular value
names[0] = 'sri kumar'

# To delete particular value in list
del names[2]

# To delete a total list
del names

# To print particular value based on index
print(names[4])
print(names[-2])


