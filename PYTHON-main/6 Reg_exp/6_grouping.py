'''
1. Using parentheses we can create groups
'''
import re

name = 'M Sriram Chowdary'
mo = re.match('(\w)\s(\w+)\s(\w+)', name)

# to print all groups
print(' All groups are  :', mo.groups())

# to print first group
print(' Surname is      :', mo.group(1))

# to print second group
print(' first name  is  :', mo.group(2))

# to print third group
print(' Second name  is :', mo.group(3))

