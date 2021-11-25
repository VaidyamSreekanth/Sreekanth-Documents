import re

# Matches from beginning of line.
name = 'sriram'
mo = re.match('^sri', name)
print(mo.group())


# Matches from end of line.
name = 'sriram123'
mo = re.match('rm123$', name)
print(mo.group())


