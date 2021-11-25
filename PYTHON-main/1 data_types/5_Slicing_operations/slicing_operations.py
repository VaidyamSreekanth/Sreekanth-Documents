'''
1. Using slicing operation we can get range of values from list and sub string from string.
'''

l = [7,89,34,2,5,12,7]

# To get  values 89, 34, 2, 5
print(' \n ', l[1:5])

# To get  values 34, 2, 5, 12
print(' \n ', l[2:6])

# To get  values 89, 34, 2, 5, 12, 7
print(' \n ', l[1:70])

#  To get values from 3rd index to last
print(' \n ', l[3:])

#  To get values from starting to 4th index
print(' \n ', l[:5])

#  To get all the values
print(' \n ', l[:])
 
# To get values one after another one
print(' \n ', l[::2])

# To get list values in reverse order
print(' \n ', l[::-1])


## Slicing operation on string
s = 'sriram'

# To get sri
print(' \n ', s[0:3])

# To get rir
print(' \n ', s[1:4])

# To reverse a string 
print(s[::-1])






