'''
1. Tuple is used to store multiple values and we can do operation on each value based on index.
2. Tuple is a read only object, we can't do update,insert and delete operations.
3. Using parentheses "()" we can create a tuple
4. tuple is a immutable object
5. To store sensitive data we use tuple.
'''

# To create a tuple
names = ('sri','kumar','balu','ram', 567, 99.9)

# Tuple doesn't support for item deltion and update
names[3] = 'ok'
del nmaes[3]

# To delete a total tuple
del names

# To print particular value based on index
print(names[4])
print(names[-2])


