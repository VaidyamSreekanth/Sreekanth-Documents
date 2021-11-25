fh = open('names.txt', 'r')

## Using read we can read entire file data and return in string format
#fdata = fh.read()
#print(fdata)

## To read the first five characters
#fdata = fh.read(8)
#print(fdata)

## Using readline we can read only one line and return in string format
#line  = fh.readline()
#print(' 1 ', line)

#line  = fh.readline(3)
#print(' 1 ', line)

# To close a file
fh.close()
