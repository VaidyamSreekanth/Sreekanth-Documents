'''
1. Using findall we can search all matching pattrens in a string
2. It will return all matching values in list format
'''
import re

s = '345sri89ramsr99y9678i'

v = re.findall('\w\d{3,}', s)
print(v)