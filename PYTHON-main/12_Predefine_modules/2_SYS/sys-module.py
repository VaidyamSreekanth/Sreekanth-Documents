'''
1. This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
'''
import sys

## To get command line arguments
#first_com_arg = sys.argv[1]
#print(' first_com_arg is :', first_com_arg)


## to appen path
#sys.path.append('C:\\Users\\sriram\\Desktop\\akr')

## To exit from execution
# print('Before exit')
# sys.exit()
# print('after exit')

try:
    #import kk
    'we' + 123
except:
    print(' Try block got failed due to : ', sys.exc_info()[1])
