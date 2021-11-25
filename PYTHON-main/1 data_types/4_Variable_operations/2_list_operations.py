l = [1,2,3]
l2 = ['A','B','C']

# To add new value into list it will add in end of the list
l.append(4)

# To add new value based on index
l.insert(2, 99)

# To appends the values of sequence to list
l.extend(l2)
print(l)

# clear is used to remove all the values in a list
l.clear()
print(l)

# copy is used to copy all the values into another varibale
l3 = l2.copy()
print(l3)

# pop used to remove value bases on index if you don't give index it will remove last value
l3.pop(0)
print(l3)

# remove is used to delete values bases on value
l3.remove('B')

# to reverse a total list values
l3.reverse()
print(l3)

#  to sort a list in ascending order
sl = [3,5,9,2,1,7]
sl.sort()
print(sl)

#  to sort a list in descending order
sl = [3,5,9,2,1,7]
sl.sort(reverse=True)
print(sl)














