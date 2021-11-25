'''
1. Using compile we can create a pattern object.
2. We can avoid resuing pattern again and again using compile.
'''

import re
pan = 'ABCDE1234F'

po = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

v = po.search(pan)
print('compile is :',  v.group())



