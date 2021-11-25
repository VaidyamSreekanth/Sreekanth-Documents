s1 = {2,4,5,6}
s2 = {9,12,4,2}

# add is used to add new value to the set
s1.add(7)
print(s1)

# remove is used to remove given value in set
s1.remove(5)
print(s1)

# discard removes the element from the set. If the element is not present  then no error or exception is raised and the original set is printed.
s1.discard(55)
print(s1)

# update used to concordinate two sets
s1 = {2,4,5,6}
s2 = {9,12,4,2}
s1.update(s2)
print(s1)

# Union is used to get all of the elements that are in at least one of the two set
print(s1.union(s2))

# intersection used to get all elements of set one and also belongs to the set two.
print(s1.intersection(s2))

# clear is used to remove all values in a set
s2.clear()
print(s2)


