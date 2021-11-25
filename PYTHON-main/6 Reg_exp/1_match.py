'''
1. Match is used to find a patran from starting positopn
'''
import re

name = 'sriram'

mo = re.match('sri', name)
print(mo.group())


