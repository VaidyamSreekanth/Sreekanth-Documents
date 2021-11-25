import re

# Matches 1 or more occurrence of preceding expression.
name = 'sriram'
mo = re.match('\w+', name)
print(mo.group())


# Matches 0 or more occurrence of preceding expression.
name = 'sriram123'
mo = re.match('\d*', name)
print(mo.group())


# Matches 0 or 1 occurrence of preceding expression.
name = 'sriram123'
mo = re.match('\d?', name)
print(mo.group())

