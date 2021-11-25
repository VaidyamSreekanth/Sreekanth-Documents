'''
1. Search is used to find a patran anywhere in the string 
'''
import re

name = 'sriram'
mo = re.search('\w\w\w', name)
print(mo.group())



