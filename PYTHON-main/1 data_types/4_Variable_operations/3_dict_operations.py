d = {99:88, 45:'sriram', 7:9}

# To remove all the values in a dictionary
d.clear()

# to copy dictionary to another variable
d2 = d.copy()

# keys is used to get all keys in a dictionary in list format
print(d.keys())

# values is used to get all values in a dictionary in list format
print(d.values())

# items is used to get keya and values 
print(d.items())

# get is used to get values based on key 
# using get we can provide default value also if key is not present it will return default value
print(d.get(45, 'kumar'))

# pop used remove key and value based on key
d.pop(45)

# update used to concordinate two dictionaries
d2 = {'name':'sriram'}
d.update(d2)
print(d)

