'''
1. Using square brackets "[]" Matches any single character in
'''
import re

# To match s is capital or samll letter in in [] position
name = 'Sriram'
mo = re.match('[sS]riram', name)
print(mo.group())

# To match "a to z" any small letter in [] position
mo = re.match('[a-z]riram', 'kumar')
print(mo.group())

# To match "A to E" any capital letter in [] position
mo = re.match('[A-E]riram', 'E34ok')
print(mo.group())

# To match any one character in "akd43$." in [] position
mo = re.match('sri[akd43$.]', 'sri$')
print(mo.group())

# To match any one character a to z , A to Z, 0-9 in [] position
mo = re.match('s[a-zA-Z0-9]i', 'sri')
print(mo.group())

# To match any one character except a to z in [] position
# if you use caret(^) symbol inside [] it will match anything except given charecters
mo = re.match('s[^a-z]i', 's8i')
print(mo.group())

# To match any one character except r and a in [] position
mo = re.match('s[ra]i', 's8i')
print(mo.group())
