'''
1. The flags modifies the meaning of the given regex pattern.

'''
import re


## re.I or re.IGNORECASE to match Case sensitive values
#name = 'SRIram'
#mo = re.search('sriram', name, re.I)
#print(mo.group())


## re.S or re.DOTALL Makes a period (dot) match any character
name = 'SRI\nram'
mo = re.search('sri.ram', name, re.I + re.S)
print(mo.group())

