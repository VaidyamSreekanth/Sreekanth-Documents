'''
1. Tell is used to find the file handler position
'''

fh = open('names.txt')

# To know File handler position before read any data
print(' Before read :', fh.tell())

# Using readline we can read only one line and return in string format
line  = fh.readline()

# To know File handler position after read a line
print(' After read :', fh.tell())

# To close a file
fh.close()
