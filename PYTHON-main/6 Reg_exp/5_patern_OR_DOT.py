import re

# To do OR operation
name = 'sriram'
mo = re.match('ram|sri', name)
print(mo.group())


# " . " Matches any single character except newline.
name = 'sriram\n123'
mo = re.match('.*', name)
print(mo.group())


# " . " Matches any single character except newline.
mo = re.match('sri\.ram', 'sri.ram')
mo1 = re.match('sri\+ram', 'sri+ram')
print(re.search(r'sri\\ram', r'sri\ram').group())
print(mo.group())



