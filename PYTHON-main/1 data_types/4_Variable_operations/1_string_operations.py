s = 'sriram chowadary'

print(dir(s))

# To convert all characters into upper letters
print(s.upper())

# To convert all characters into lower letters
print(s.lower())

# TO verify given staring is lower or not.
# It will return True if string is lower else False
print(s.islower())

# TO verify given staring is upper or not.
# It will return True if string is upper else False
print(s.isupper())


# split() method returns a list of strings after breaking the given string by the specified separator.
v = 'sriram,kumar,balu'
print(v.split(','))
print(v.split('a'))
print(v.split('ma'))
print(v.split())

# replace() is used to replace a value  with another value.
name = 'sriramsri sri'
print(name.replace('sri','SAI'))
print(name.replace('sri','SAI', 1))

# count is used to get repeated count of given value in a string
s = 'sriram sri'
print(s.count('r'))
print(s.count('sri'))


# The join() method provides a flexible way to concatenate string. It concatenates each element of an iterable (such as list, string and tuple) to the string and returns the concatenated string
j = '='
print(j.join(['sri','ram','kumar']))


