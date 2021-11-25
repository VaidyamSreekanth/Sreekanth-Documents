'''
1. Seek is used to bring the file handler position where ever we required
'''

fh = open('names.txt', 'r')

## reading entire data from file
line  = fh.read()

## If you wnat to bring file handler position to starting
print(' FH position Before seek :', fh.tell())
fh.seek(8)
print(' FH position After seek  :', fh.tell())
print(' 1 : ',fh.readline())

## If you wnat to bring file handler to 8th position
#print(' FH position Before seek :', fh.tell())
#fh.seek(8)
#print(' FH position After seek  :', fh.tell())
#print(fh.readline())

# To close a file
fh.close()
