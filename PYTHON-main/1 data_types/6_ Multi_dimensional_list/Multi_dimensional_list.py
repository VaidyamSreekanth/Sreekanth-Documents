'''
1. multi-dimensional list contains another list.
'''

l = [1,2,['A',{'n':'one',88:99},'B'],'sri',(8,9)]
#    0 1              2                3     4

# Tp print B 
print(l[2][2])

# to print 9 from tuple
print(l[4][1])

# To print 99 value from list inside dictionary
print(l[2][1][88])


