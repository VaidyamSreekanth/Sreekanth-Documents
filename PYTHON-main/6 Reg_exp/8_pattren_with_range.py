'''
1. Using curly brace "{}" Matches exactly n number of occurrences of preceding expression.
'''
import re

# To match exact 3 charecters
name = 'Sriram'
mo = re.match('\w{3}', name)
print( ' Pattren \w{3} ' ,mo.group())

# To match minimum 3 charecters maximum 6 charecters
name = 'Sriram'
mo = re.match('\w{3,6}', name)
print( ' Pattren \w{3,6} ' ,mo.group())

# To match minimum 0 charecters maximum 6 charecters
name = 'Sriram'
mo = re.match('\w{,6}', name)
print( ' Pattren \w{,6} ' ,mo.group())

# To match minimum 3 charecters maximum more charecters
name = 'Sriram'
mo = re.match('\w{3,}', name)
print( ' Pattren \w{3,} ' ,mo.group())
