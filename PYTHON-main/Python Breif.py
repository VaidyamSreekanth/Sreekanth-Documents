## What are the data types available in python ?
Python supports 6 types of data types.
    1. Number
    2. String
    3. List
    4. Tuple
    5. Dictionary
    6. Set


## What is variable and use of variables ?
1. varables are used to store data and we can reuse.
2. Using variable we can provide value with descriptive name so it can understood more clearly by the reader and ourselves.
3. if you share a value across program through varable, it is easy to update value.


'''
1. Number data type is used to store integer values(0-9).
2. Number is a immutable object
    Example :-  N = 123

    1. 'N' is a Variable
    2. '=' is a assignment operator
    3. '123' is a value
    4. 'N' Data type is number

3. type() function is used to know type of object.
'''

# To Create a variable with Number data type
n = 123

# To Print on console
print(n)

# To Update and Append
n = 555

# To delete a Varable
del n

# To Know varable Data type
print(type(n))


'''
1. Using string we can store any value but it should be in single quotes or double quotes.
2. String is a immutable object

'''

# To define a string variable
name = 'sri123$#%'

# If string contains single quote 
name1 = " I don't know sriram"

# If string contains double quote 
name2 = ' I know "sriram"'

# If string contains single quote and double quote 
name3 = ''' I don't know "sriram"'''


# To update
name = 'kumar'
print(name)

# To Delete 
del name 

# To Print on console
print(' Name is : ', name)

'''
1. List is used to store multiple values and we can do operation on each value based on index.
2. Using square brackets "[]" we can create a list
3. List is a mutable object

            -5        -4     -3       -2   -1
names = ['sriram', 'ramu','ganesh', 999, 98.90]
            0         1       2       3     4

'''
# To create a list
names = ['sri','kumar','balu','ram', 567, 99.9]

# To update a particular value
names[0] = 'sri kumar'

# To delete particular value in list
del names[2]

# To delete a total list
del names

# To print particular value based on index
print(names[4])
print(names[-2])

'''
1. Tuple is used to store multiple values and we can do operation on each value based on index.
2. Tuple is a read only object, we can't do update,insert and delete operations.
3. Using parentheses "()" we can create a tuple
4. tuple is a immutable object
5. To store sensitive data we use tuple.
'''

# To create a tuple
names = ('sri','kumar','balu','ram', 567, 99.9)

# Tuple doesn't support for item deltion and update
names[3] = 'ok'
del nmaes[3]

# To delete a total tuple
del names

# To print particular value based on index
print(names[4])
print(names[-2])

'''
1. Dictionary is a collection of key value pairs.
2. Using dictionary we can represent data meningfully.
3. Based on key we can do operation on each value.
4. Using curly brackets "{}" we can create a dictionary
5. dictionary is a mutable object
'''

# To create a dictionary
emp_det = {'ename':'sri', 'eid':36, 'dname':'IT', 'did':45, 'age':33}

# emp = {'ename':'sri', True:36, None:'IT', 99:45, 88.90:33}

# To update 
emp_det['dname'] = 'SALES'

# To Delete particular key value pair
del emp_det['eid']

# To delete total dictionary
del emp_det

# To print particular key value pair 
print(emp_det['age'])

# To print total dictionary 
print(emp_det)

'''
1. Set is used to store unique values it doesn't contains duplicate values.
2. Using set we can do set operations
3. Using curly brackets "{}" we can create a set
4. Set doesn't support indexing 
5. Set is a mutable object
'''

# To create a set
eids = {45,33,45,23,33}

# To print a set
print(' Emp ids are ==> ',eids )

# To  Delete a set
del eids

# Assignment operators on Number
n = 9

#n += 2  # n = n + 2
#n -= 2
#n *= 2
#n /= 2
#n //= 2
#n %= 2

print(n)

'''
1. Using int() function we can convert object into integer.
'''

n = 12
n2 = '65'

print(type(int(n2)))
print(int(n) + int(n2))

print(float(n))


'''

1. Using float() function we can convert int object into float.

'''
amount = 12

print(float(amount))

amount = 12.09

print(int(amount))

'''
1. Using str() function we can convert object into string data type 
'''

v = 'sri'
v2 = 234

print(v + str(v2))

'''
1. Using list() function we can convert iterable objects into list

'''

t = (1,3,4,5,6)
st = {11,33,44,55,66}
s = 'sri ram'

print(' Tuple is : ', list(t))
print(' Set is   : ', list(st))
print(' String is: ', list(s))

# To create a empty list
ml = list()
print(' ML is    :', ml)

'''

1. Using tuple() function we can convert iterable objects into tuple

'''


l = [1,3,4,5,6]
st = {11,33,44,55,66}
s = 'sri ram'

print(' List is  : ', tuple(l))
print(' Set is   : ', tuple(st))
print(' String is: ', tuple(s))

'''
1. Using dict() function we can create a dictionary with key values.
2. Using dict() function we can create a empty dictionary 
'''

#d = dict([('A',1),('B', 2)])
#print(d)

# To create a empty list
md = str()
print(md)
print(type(md))

'''
1. Using set() function we can convert iterable objects into set

'''
'''

1. Using tuple() function we can convert iterable objects into tuple

'''


l = [1,3,4,5,3,6]
t = (11,33,44,55,66)
s = 'sri ram'

print(' List is  : ', set(l))
print(' Set is   : ', set(t))
print(' String is: ', set(s))

s = 'sriram chowadary'

print(dir(s))

# To convert all characters into upper letters
print(s.upper())

# To convert all characters into lower letters
print(s.lower())

# TO verify given staring is lower or not.
# It will return True if string is lower else False
print(s.islower())

# TO verify given string is upper or not.
# It will return True if string is upper else False
print(s.isupper())


# split() method returns a list of strings after breaking the given string by the specified separator.
v = 'sriram,kumar,balu'
print(v.split(','))
print(v.split('a'))
print(v.split('ma'))
print(v.split())

# replace() is used to replace a value  with another value.
name = 'sriramsri sri'
print(name.replace('sri','SAI'))
print(name.replace('sri','SAI', 1))

# count is used to get repeated count of given value in a string
s = 'sriram sri'
print(s.count('r'))
print(s.count('sri'))


# The join() method provides a flexible way to concatenate string. It concatenates each element of an iterable
(such as list, string and tuple) to the string and returns the concatenated string
j = '='
print(j.join(['sri','ram','kumar']))


l = [1,2,3]
l2 = ['A','B','C']

# To add new value into list it will add in end of the list
l.append(4)

# To add new value based on index
l.insert(2, 99)

# To appends the values of sequence to list
l.extend(l2)
print(l)

# clear is used to remove all the values in a list
l.clear()
print(l)

# copy is used to copy all the values into another varibale
l3 = l2.copy()
print(l3)

# pop used to remove value bases on index if you don't give index it will remove last value
l3.pop(0)
print(l3)

# remove is used to delete values bases on value
l3.remove('B')

# to reverse a total list values
l3.reverse()
print(l3)

#  to sort a list in ascending order
sl = [3,5,9,2,1,7]
sl.sort()
print(sl)

#  to sort a list in descending order
sl = [3,5,9,2,1,7]
sl.sort(reverse=True)
print(sl)


d = {99:88, 45:'sriram', 7:9}

# To remove all the values in a dictionary
d.clear()

# to copy dictionary to another variable
d2 = d.copy()

# keys is used to get all keys in a dictionary in list format
print(d.keys())

# values is used to get all values in a dictionary in list format
print(d.values())

# items is used to get keya and values 
print(d.items())

# get is used to get values based on key 
# using get we can provide default value also if key is not present it will return default value
print(d.get(45, 'kumar'))

# pop used remove key and value based on key
d.pop(45)

# update used to concordinate two dictionaries
d2 = {'name':'sriram'}
d.update(d2)
print(d)

s1 = {2,4,5,6}
s2 = {9,12,4,2}

# add is used to add new value to the set
s1.add(7)
print(s1)

# remove is used to remove given value in set
s1.remove(5)
print(s1)

# discard removes the element from the set. If the element is not present  then no error or exception is raised and the original set
is printed.
s1.discard(55)
print(s1)

# update used to concordinate two sets
s1 = {2,4,5,6}
s2 = {9,12,4,2}
s1.update(s2)
print(s1)

# Union is used to get all of the elements that are in at least one of the two set
print(s1.union(s2))

# intersection used to get all elements of set one and also belongs to the set two.
print(s1.intersection(s2))

# clear is used to remove all values in a set
s2.clear()
print(s2)

'''
1. Using slicing operation we can get range of values from list and sub string from string.
'''

l = [7,89,34,2,5,12,7]

# To get  values 89, 34, 2, 5
print(' \n ', l[1:5])

# To get  values 34, 2, 5, 12
print(' \n ', l[2:6])

# To get  values 89, 34, 2, 5, 12, 7
print(' \n ', l[1:70])

#  To get values from 3rd index to last
print(' \n ', l[3:])

#  To get values from starting to 4th index
print(' \n ', l[:5])

#  To get all the values
print(' \n ', l[:])
 
# To get values one after another one
print(' \n ', l[::2])

# To get list values in reverse order
print(' \n ', l[::-1])


## Slicing operation on string
s = 'sriram'

# To get sri
print(' \n ', s[0:3])

# To get rir
print(' \n ', s[1:4])

# To reverse a string 
print(s[::-1])

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

'''
1. Call by Reference :- it will copy object memory location
2. Call by Value     :- It will copy value

    Python is a call by Reference
    
    id() ==> Id function is used to find memory location of object.
'''

# a = 10
# b = 10
# c = a

# print(' id of a :', id(a))
# print(' id of b :', id(b))
# print(' id of c :', id(c))

l = [1,2,3]

l2 = l

#l2 = l.copy()
l.append(45)

print(' l id is  :', id(l), l)
print(' l2 id is :', id(l2), l2)

'''
1. Mutable Objects :- 
    1. Mutable objects are changable.
    2. Memory location will be same after changing value also.
    3. Mutable data types are :- list,Dictionary and set
2. Immutable Objectss :- 
    1. Immutable objects are not changable.
    1. Memory location will be different  after changing value.
    3. Mutable data types are :- Number,String and tuple

    id() ==> Id function is used to find memory location of object.
'''

## For Number
# n = 123
# print(' N address before edit:', id(n))
# n = 222
# print(' N address after edit :', id(n))

## For string
# name = 'sri'
# print(' \n name address before edit :', id(name))
# name = 'ram'
# print(' \n name address after  edit :', id(name))

## For List
# names = ['sri','ram','balu']
# print(' \n names address before edit :', id(names))
# names.append('nagesh')
# print(' \n names address after edit  :', id(names))
# print(' \n names after edit :', names)


## For set
# names = {'sri','ram','balu'}
# print(' \n set address before edit :', id(names))
# names.add('OK')
# print(' \n set address after edit  :', id(names))
# print(' \n names :', names)

## For dictionary
emp_det = {'name':'sri','dname':'IT'}
print(' \n emp_det addredd before edit :', id(emp_det))
emp_det['eid'] = 45
print(' \n emp_det address after edit  :', id(emp_det))
print(' \n emp_det :', emp_det)

1. Using if, elif and else we can perform conditional operations
2. Using conditioanl operations we can execute a block of code based on condition

# Below are the python operators 
    1. Arthmetic operatiors(+,-,*,%,/,//)
        1. Uesd to do addition and substraction operations
    2. Assignment operators(=,+=,-=,*=,%=,/+,//+)
        1. Used to assign value to variable
    3. Comparison operators(==,!=,>,>=,<,<=)
        1. These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
    4. Logical operators(and,or,not)
        1. Using logical operations we can execute a block of code based on multiple condition.
    5. Member ship operators(in,not in)
        1. Using member ship operations we can fing a value in list and sub string in a string
    6. Identity operators(is,is not)
        1. Using identity operators we can check memory location of objects

name = 'sriram'

if name == 'sriram':
    print('ok')
    a = 10
a =10

sal = 501

if sal == 500:
   sal += 100
   print(' Sal is :', sal)
else:
    print(sal + 50)


n = 460
if n == 45:
    print(' If block ')
elif n != 48:
    print(' First elif ')
elif n > 55:
    print('Second elif')
elif n >= 555:
    print('Third elif')
elif n < 2:
    print(' Forth elif')
else:
    print(' Else block')


'''
  1. Logical opertions are and, or and not 
  2. Using logical operations we can execute a block of code based on multiple condition.
'''

sal  = 50
dname = 'IT'

#if sal >= 50000 and dname == 'IT':
#    print(sal + 2500)

#if sal >= 50000 or dname == 'IT' :
    #print(sal + 2500)

if not dname == 'IT': print('  NOT  ')

'''
1. Membership operations are "in" and "not in"
2. Using member ship operations we can find a value in list and sub string in a string
3. We can't perform membership opertion on number data type.
'''

#name = 'sriram'
#if 'ra' in name: print('IN')

#if 's' not in name: print('NOT IN')

#names = ['sriram','ganesh','kumar','balu']
#t = ('sriram','ganesh','kumar','balu')
#s = {'sriram','ganesh','kumar','balu'}
#if 'kumar' in names: print(names)

#d = {'name':3, 'eid':56, 99:89, '55':33}
#if 99 in d: print(' Dictionary')


#n = 8976
#if 97 in n: print(n)


'''
1. Identiti opertions are is and is not
2. Using identity operators we can check memory location of objects.
'''

a = 10
b = 10
c = a

# print(' A ID is :', id(a))
# print(' B ID is :', id(b))
# print(' C ID is :', id(c))

#if a is c : print(' IS ')


l = [1,2,3]
l2 = l.copy()
print(' L id is  : ', id(l))
print(' L2 id is : ', id(l2))

if l is not l2 : print(' OK ')

'''
Below are the False scenarios in python
    1. Zero(0)
    2. Any empty data type
    3. None
    4. False
'''

n = -123
name = 'sri'
l = [1,2,3]
v = None
F = False

if name: print(' OK ')


print( 2 != 2)


1. Using loops we can execute a block of code repeatedly

2. Python support 3 types of loops
    1. For loop    ==> for loop Iterate based on range
    2. While loop  ==> while loop Iterate based on condition
    3. nested loop ==> If a loop contains another loop that is called nested loop

3. Loop statements 
    1. break     ==> break used to terminates the loop
    2. continue  ==> continue used to skipe the current iteration 
    3. pass      ==> 
        1. pass will do nothing 
        2. we use pass when statement is require to aviod syntax issues.
        
'''
1. Range() function used to craete a range of values
'''

#for n in range(5):        # 0 to n-1
#   print(n)

# for n in range(3, 36):     # n to n-1
    # print(n)

# for n in range(-3, -7):     # n to n-1
    # print(n)
    
#for n in range(1, 15, 3):  # n to n-1 , step
#    print(n)


'''
1. We can use all data types in for loop except number.
'''

## string iterate character by characters
s = 'sri ram'
for c in s:
    print(c)

## list iterate value by value 
names = ['sri','ram','kumar','nagesh', 'balu']
for name in names:
   print(name)


# Dictionary iterate based on key
emp_det = {'name':'sri', 'eid':35, 'dname':'IT', 'name':'ram'}
# for k in emp_det:
    # print(k, emp_det[k])

## Number object does not support for iterable
NO =  345
for n in NO: print('OK')


'''
1. While loop Iterate based on condition
'''
n = 6
# while n > 3:
    # n -= 2
    # print(n)

# while n:
    # print(n)
    # n -= 2

sal = 500
while sal >= 300:
    print(sal)
    sal -= 50
'''
3. Loop statements 
    1. break     ==> break used to terminates the loop
    2. continue  ==> continue used to skipe the current iteration 
    3. pass      ==> 
        1. pass will do nothing 
        2. we use pass when statement is require to aviod syntax issues.
'''

for i in range(4, 8):
   print(i)
   if i > 4 : break


for i in range(4):
    if i : continue
    print(i)

for i in range(6):
    if i >= 4 : continue
    print(i)
    if i == 2 : break

for i in range(5):
    pass

if 2 == 2: break

for x in [1,2,3,4]:
    print('----', x)
    for c in 'SRC':
        print('++++++++++++', c)


for x in [1,2,3]:
    print('----', x)
    for y in 'AB':
        print('=======>', y)
        for z in {'n':'sri',88:99}:
            print('++++++++++', z)

1. Using functions we can give a name to the block of code.
2. Using functions we can re use the code.
3. Using def keyword we can create a function.

# Use of Parameters 
1. Using parameters we can make a function dynamic
2. Using parameters we can pass values to the function
3. python function support 4 types of parameters
    1. Required or positional arguments
    2. Keyword arguments
    3. Default arguments
    4. Variable length arguments


def add():
    print( 3 + 6 )

add()


'''
1. We should give values to the required arguments.
2. The given values pass in correct positional order.
'''

def add(a,b):
    print(' A value is :', a)
    print(' B value is :', b)

add(4, 6)
#add(5, 8)
#add(42, 98)



'''
1. We can pass values based on parameter name.
2. Keyword arguments should follow positional argument.
'''

def add(a, b, c):
    print(' A value is :', a)
    print(' B value is :', b)
    print(' C value is :', c)

#add(4, 7)

#add(b=7,a=6)

##  Doesn't accept multiple values for single parameter
#add(4,a=78)

add(78, b=8, c=4)


'''
1. Using default arguments we can give default value to the parameter.
2. Default arguments should follow the positional argument.
'''

def add(a, b, c=9):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)

add(7, 8)


'''
1. using args(*) we can takes N number of arguments
2. it will atke 0 to many values in tuple format
'''
def add(b=5, a, *c):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)

add(3, 67, 7,54,'sri')


add(7, 8, 4,6,3)

'''
1. using kwargs(**) we can take values in dictionary format
'''
def add(a, b=5,*c, **d):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)
    print(' D value is : ', d)

add(6,7,3,67,9, name='sriram', eid=56)


'''
1. Return keyword used to return value from function.
2. After executiong return keyword function will terminate
3. We can use many return keywords in side a function
'''

def add(a=10,b=25):
    print(' Before return')
    if b > 31 : return  'ok'
    print(' After return')

ret = add(20,25)
print(' return value is :', ret)

'''
1. Return keyword used to return value from function.
2. After executiong return keyword function will terminate
3. We can use many return keywords in side a function
'''

def add(a=20,b=30):
    if a > 13: return 'ok'
    print(' Before return')
    return a + b
    print(' After return')
    if a == 20: return 'sriram'

#print(add(15))

ret = add()
print(' return value is :', ret)


'''
1. A recursive function is a function that calls itself during its execution.
'''

def add(a):
   print('A value is ', a)
   a += 5
   if a > 20: return
   add(a)

add(5)


1. Using file handling we can do file operations

# How to open a file in python ?
1. We can open a file two ways in python 
    1. open()
    2. With open()

# OPEN
1. Using open we can open only one file at a time and we have to close a file explicity

# WITH OPEN 
1. Using with open we can open multiple files at a time and no need to close files explicity

# File Open Modes In Python

r    ==>     It opens a file for read only.

w    ==>     It allows write-level access to a file. If the file already exists, then it’ll get overwritten. It’ll create a new file if the same doesn’t exist.

a    ==>     It opens the file in append mode.

a+   ==>     It opens a file FOR append AND read

rb   ==>     It opens a binary file for read


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


'''
1. To do write operation on file we have to open a file with 'w' mode
2. If you open a file with write mode if file is not exist it will crate a new file, if file is exist it will remove old data and write new data.

'''

fw = open('write_names.txt', 'w')

# To write data into file
fw.write('Hi Kumar\n')
fw.write('How are you')

# To close a file
fw.close()

'''
1. To do append operation on file we have to open a file with 'a' mode
2. If you open a file with append mode if file is not exist it will crate file, if file is exist it will add new data after old data.

'''

fw = open('append_names.txt', 'a')

# To write data into file
fw.write('\nHi Sriram\n')
fw.write('How are you\n ')

# To close a file
fw.close()


# reading names.txt and writing into names_write.txt

with open('names.txt') as fr, open('names_write.txt', 'w') as fw:
    fw.write('OK\n')
    fw.write('OK222')

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


1. Using regular expressions we can find a string based on pattern.
2. Using re module we can do regular expression operations

# Regular Expression Patterns
'\d  ==>  Match a digit   : [0-9]
'\D  ==>  Match a nondigit: [^0-9]
'\s  ==>  Match a whitespace character
'\S  ==>  Match a nonwhitespace character
'\w  ==>  Match a single character : [A-Za-z0-9_]
'\W  ==>  Match a single nonword character: [^A-Za-z0-9_]
'\n  ==>  Match a new line character


+   ==>  Matches 1 or more occurrence of preceding expression.
*   ==>  Matches 0 or more occurrence of preceding expression.
?   ==>  Matches 0 or 1 occurrence of preceding expression.
^   ==>  Matches beginning of line.
'$   ==>  Matches end of line.
|   ==>  To do OR operation
.   ==>  Matches any single character except newline.
'\'   ==>  Used to escape any special character and interpret it literal

()  ==>  Using parentheses we can create a groups
[]  ==>  Using square brackets "[]" Matches any single character in brackets.
{}  ==>  Matches exactly n number of occurrences of preceding expression.

'''
1. Match is used to find a patran from starting positopn
'''
import re

name = 'sriram'

mo = re.match('sri', name)
print(mo.group())


'''
1. Search is used to find a patran anywhere in the string 
'''
import re

name = 'sriram'
mo = re.search('\w\w\w', name)
print(mo.group())

import re

# Matches 1 or more occurrence of preceding expression.
name = 'sriram'
mo = re.match('\w+', name)
print(mo.group())


# Matches 0 or more occurrence of preceding expression.
name = 'sriram123'
mo = re.match('\d*', name)
print(mo.group())


# Matches 0 or 1 occurrence of preceding expression.
name = 'sriram123'
mo = re.match('\d?', name)
print(mo.group())


import re

# Matches from beginning of line.
name = 'sriram'
mo = re.match('^sri', name)
print(mo.group())


# Matches from end of line.
name = 'sriram123'
mo = re.match('rm123$', name)
print(mo.group())


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


'''
1. Using parentheses we can create groups
'''
import re

name = 'M Sriram Chowdary'
mo = re.match('(\w)\s(\w+)\s(\w+)', name)

# to print all groups
print(' All groups are  :', mo.groups())

# to print first group
print(' Surname is      :', mo.group(1))

# to print second group
print(' first name  is  :', mo.group(2))

# to print third group
print(' Second name  is :', mo.group(3))

'''
1. Using square brackets "[]" Matches any single character in
'''
import re

# To match s is capital or samll letter in in [] position
name = 'Sriram'
mo = re.match('[sS]riram', name)
print(mo.group())

# To match "a to z" any small letter in [] position
mo = re.match('[a-z]riram', 'kumar')
print(mo.group())

# To match "A to E" any capital letter in [] position
mo = re.match('[A-E]riram', 'E34ok')
print(mo.group())

# To match any one character in "akd43$." in [] position
mo = re.match('sri[akd43$.]', 'sri$')
print(mo.group())

# To match any one character a to z , A to Z, 0-9 in [] position
mo = re.match('s[a-zA-Z0-9]i', 'sri')
print(mo.group())

# To match any one character except a to z in [] position
# if you use caret(^) symbol inside [] it will match anything except given charecters
mo = re.match('s[^a-z]i', 's8i')
print(mo.group())

# To match any one character except r and a in [] position
mo = re.match('s[ra]i', 's8i')
print(mo.group())


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

'''
1. The flags modifies the meaning of the given regex pattern.

'''
import re


## re.I or re.IGNORECASE to match Case sensitive values
#name = 'SRIram'
#mo = re.search('sriram', name, re.I)
#print(mo.group())


## re.S or re.DOTALL Makes a period (dot) match any character
name = 'SRI\nram'
mo = re.search('sri.ram', name, re.I + re.S)
print(mo.group())


'''
1. Using compile we can create a pattern object.
2. We can avoid resuing pattern again and again using compile.
'''

import re
pan = 'ABCDE1234F'

po = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

v = po.search(pan)
print('compile is :',  v.group())

'''
1. Using findall we can search all matching pattrens in a string
2. It will return all matching values in list format
'''
import re

s = '345sri89ramsr99y9678i'

v = re.findall('\w\d{3,}', s)
print(v)


1. Any .py file is a module in python
2. Using module we can re use the code

# How to import a module ?
1. using import and from import we can import module

# Difference between import and from import 

1. Using import we can import entire module and we have to use module name as prefix for each module attribute.
2. Using from import we can import required attribute from module and no need to give prefix as module name to use module attribute.

'''
1. we can import a module using import keyword
'''

import base_module


# Print a variable from base_module
#print(base_module.names)


## call a add function from base_module
base_module.add()

## call a sum function from base_module
r = base_module.sum(20,50)
print(' Sum value is :', r)

'''
1. Import module attributes using "from" keyword
'''

## to import only names variable
#from base_module import *
import base_module

## to import only name variable and add function 
#from base_module import names, add

## to import all module attributes
#from base_module import *

## Print a variable from base_module
print(base_module.name)


## call a add function from base_module
#add()

## call a sum function from base_module
#r = sum(20,50)
#print(' Sum value is :', r)


'''
1. To import module from another path we should add module path to sys.path list
2. sys is a python pre define module
'''
import sys

sys.path.append(r'C:\ON-LINE\COURSES\1_PYTHON\7 modules\ONE')

import module2

module2.fun1()


1. An exception is an event, which occurs during the execution of a program.
2. Using try,except,else and finally block we can handle exception.
3. Using exceptions we can handle run time errors.

# else
1. else block will execute when the try block executed successfully with out any errors.

# Finally ***
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do the cleanup process.

import sys
try:
    'we' + '123'
    sys.ok()
    import re
    open('2_else.py')
except ModuleNotFoundError:
    print(' Module is not defined')
except NameError:
    print(' name is not defined please define')
except TypeError:
    print(' TYPE ERROR')
except FileNotFoundError as e:
    print(' Please define file', e)
except:
    print(' Try block got failed')

'''
1. else block will execute when the try block executed successfully with out any errors.
'''
try:
    a = 10
    b = 20
    c = a + b
    print('ok')
except:
    print('Try block got failed')
else:
    print('Else block is')


'''
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do cleanup process.
'''
try:
    a = '10'    #--> open('test_data.txt')
    b = 20
    print(c) 
    c = a + b   #  fail
   # fh.close()
except:
    print(' Try block got failed')
else:
    print(' Else block ')
finally:
    print(' Finally block ')

# Using raise keyword we can raise exception manually.

num = 15

if num <= 15 : raise AssertionError(' Number should be more than 15')


print(' END ')


# Core OOPS(Object-oriented programming) concepts are:-

1) Inheritance
2) Polymorphism
3) Abstraction
4) Encapsulation

Using class we can achive all this concepts.

# Craete a class with varable amd methods
class One():
    name = 'sriram'

    def add(self):
        print(' addition is :', 5 + 7)

    def sum(self, a, b):
        return a + b

# To create a instance to the class
inst = One()

# To print class variable name
print(' Name is :', inst.name)

# To call add method
inst.add()

# To call sum method
r = inst.sum(4,6)
print(' Sum is :', r)

'''
1. self is used to reffer the instance of the class to the method.
2. Based on self only the method will get to know for which instace it has to responce.
3. We can give any name in place of self.
'''

class One():
    def add(self):
       print(' \n ID of self is  : ',id(self))

    def sub(name, a, b):
        #print(' \n ID of r is     : ',id(name))
        print(' A value is :', a)
        print(' A value is :', b)


ins1 = One()

ins2 = One()

#print(' \n ID of ins1 is  : ',id(ins1))
#ins1.add()

ins1.sub(10,5)

ins2.sub(100,200)

class One:
    def __init__(self, a):
        self.a = a
    
    def add(self):
        print(self.a)


inst = One(34)
inst.add()

## WITHOUT constructor 
class One():
    def add(self, uname, password):
       print(uname , password)

    def sub(self, uname, password, hostname, port):
        print(uname, password )

    def mul(self, uname, password):
        print(uname, password )

inst = One()

inst.add('admin','admin123')
inst.sub('admin','admin123','12.45.67.8', 23)
inst.mul('admin','admin123')


## Using constructor we can create instance varables.
## Using __init__ we can create constructor
class One():
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        #print('__INIT__')

    def add(self):
       print(' Add method ', self.uname , self.password)
       
    def sub(self, hostname, port):
        print(' Sub method ', self.uname, self.password)

    def mul(self):
        print(' Mul method ',  self.password )

inst = One('Admin', 'Admin123')

inst.add()
inst.sub('2.3.4.5', 23)
inst.mul()

'''
1. Using @staticmethod decorator we can create static method.
2. For Static method self argument doesn't required.
3. Using staticmethod we can provide same behavior to the all the instances of class.
4. staticmethod we can call through instance or without instance.
'''

class One():
    @staticmethod
    def add():
        print(' Static Method')

#ins = One()
#ins.add()
One.add()

'''
1. Using @classmethod decorator we can create Class method.
2. For class method we have to give cls argument.
3. Using classmethod we can change class attributes.
4. classmethod we can call through instance or without intance.
'''

class One():
    name = 'sriram'

    @classmethods
    def sub(cls, n):
        print(' id of One : ', id(One))
        print('\n id of cls : ', id(cls))
        cls.name = n
        print(' \n class variable is :: ', One.name)

ins = One()
ins.sub('kumar')
#One.sub('Nagesh')

'''
1. Using inheritance we can get parent class properties into child class.
'''
class One():
    name = 'sriram'      # Class variable

    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class Two(One):
    pass


inst = Two()
print(dir(inst))

#inst.add(3,5)
#print(inst.name)

'''
1. If you inheritance more than one class that is called multi inheritance
'''
class One():
    name = 'sriram'
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class Two():
    def colour(self):
        print('Blue')

class Three(One,Two):
    pass

ins = Three()
#print(dir(ins))
ins.colour()
ins.add(5,6)

'''
1. We can inherit a derived class from another derived class, this process is known as multilevel inheritance
2. Example :- We have three classes A, B and C, If you inheritance class A into class B and class B into class C 
This is called Multi level inheritance.
'''

class A():
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class B(A):
    def colour(self):
        print('Blue')

class C(B):
    pass

ins = C()
print(dir(ins))
#ins.colour()

'''
1. If you have same method names in class A and class B, then if you Inheritence class A into class B then Class A method
 will override with class B method.
'''
class A():
    def add(self):
        print('\n A ADD ')

class B():
    def add(self):
        print('\n B ADD ')

class C(A, B):
    def add(self):
        print(' \n C ADD ')

inst = C()
inst.add()

'''
POLYMORPHISM:-
1. An object behavior will get change during run time.
2. By using inheritence and overriding we can achive it.
'''

class Car:
    def colour(self):
        print('red')

    def music_system(self):
        print('philips')

    def airbags(self):
        print(4)

class Swift(Car):
    def colour(self):
        print('white')

class Varna(Car):
    def colour(self):
        print('block')
    
    def music_system(self):
        print('sony')
    
    def airbags(self):
        print(6)

car_ins = Car()
swift_ins = Swift()
varna_ins = Varna()

car_ins.colour()
swift_ins.colour()
varna_ins.colour()

'''
1. Encapsulation is wrapping data(methods) together into single uint.

2. Using encapsulation we can give protection to the class members. Using access specifiers/modifiers.
'''

class One():
    name = 'sriam'
    def __init__(self, a):
        self.a = a

    def add(self):
        print('sum is ')

    def sub(self):
        print('sub is:')
        cls._add()

ins = One(3)

print('\n ', ins.name)


'''
1. All name variables and methods are public by default in Python

2. Protected variable we can define By prefixing the name of your variable or method with a single underscore, you’re 
telling others “don’t touch this, unless you’re a subclass”

3. private variable we can define By prefixing the name of your variable with a double underscore,
4. By declaring your data member private you mean, that nobody should be able to access it from outside the class.

'''
class One():
    name   = 'public'     # public
    _name  = 'protect'    # protect
    __name = 'Pravate'    # pravate
    def sum(self):
        self.__sub()
        print(' \n Public ' )

    def _add(self):
        print(' \n Protect ' )

    def __sub(self):
        print(' \n Pravate ')

ins = One()
ins.sum()
#print(ins.__name)


'''
1. An abstract method is a method that is declared, but contains no implementation.
2. By defining an abstract base class, you can define a common API for a set of subclasses.
3. By using abc module we can define abstract class.
'''
from abc import ABCMeta,abstractmethod

class One(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        print(' One Add ')

    @abstractmethod
    def sub(self):
        pass

#a = One()
#a.add()

## If you inheritence an abstaruact class you should impliment that all those methods which are abstract ,methods
class Two(One):
    def add(self):
        print(' TWO ADD')

    def sub(self):
        pass

ins = Two()
ins.add()

'''with init file'''

# To import all attrbutes from one package
from one import *


## To print name which exist in  windows module
print(windows.name)


## To call os function which exsit in  mac module
os()

## To call vmware function which exist in vmware module
vmware.vmware()


## To call sub function which exist in linux module
linux.sub()

'''With Out INIT file'''

# To import linux module from one package
from one import linux

# To import windows module from two package
from one.two import windows

# To import only os function from mac module
from one.three.mac import os

## To call sub function from linux module
linux.sub()


## To print name variable form windows module
print(windows.name)

## To call os function which imported from mac module
os()

'''Simple decorator'''

def dec_fun(f):
   def wrap_fun():
       return ' Hellow ' + f()
   return wrap_fun

@dec_fun
def get_name():
   return 'sriram'

r = get_name()
print(r)

'''Decorator with parameter'''

def dec_fun(f):
   def wrap_fun(name):
       return ' Hellow ' + f(name)
   return wrap_fun

@dec_fun
def get_name(name):
   return name

r = get_name('sriram')
print(r)


'''
1. Lambda is a another way to create a function.
2. Lambda is a one line anonymous function it doesn't contains name.
3. Using lambda we can do only one expression.
'''
## Lambda with out arguments
#add = lambda : 'sri'
#r = add()
#print(r)

## Lambda with arguments 
#add = lambda a,b: a + b
#r = add(2,33)
#print(r)

## Lambda with if and else
add = lambda a,b: b + 10 if a > 5 else a - b
print(add(6,6))


'''
1. map is used to do operation on each iterable value and it will return all operations result in map object foramt.

2. Map taks two parameters one is function another one is iterable object
'''

## Map with def fucntion
# def add(a):
    # return  a + 10

# mo = map(add,(1,2,3,4,5,6))
# print(list(mo))

## Map with lambda function
#mo = map(lambda a,b : a + b ,[1,2,3,4,5], [10,20,30])
#print(tuple(mo))

## Map with lambda if else
s=[1,2,6,4]
s1=[3,6,3,4]
mo = map(lambda a,b: a+b if a > b else a - b,s,s1)
print(list(mo))

'''
1. The filter() method filters the given sequence with the help of a function and retun filter object.
2. filter taks two parameters one is function another one is iterable object
'''

## Filtr with normal function
def add(a):
    if a >= 3 : return a

#fo = filter(add,[1,2,3,4,5])
#print(list(fo))

## Filter with lambda function
fo = filter(lambda a: a > 2,[1,2,6,4,5])
print(list(fo))

'''
1. reduce is used to do operation on each iterable value and its return all operations result sum.
2. reduce taks two parameters one is function another one is iterable object

'''

from functools import reduce

#(1+2)+3)+4)+5)

a = 24
b = 5

fact = reduce(lambda a,b: a * b,[1,2,3,4,5])
fib = reduce(lambda a,b: a + b,[1,2,3,4,5])
print(fib)

'''
List comprehensions are used for creating new list from another iterables.

Using list comprehensions we can do loop operations inside a square brackets.
'''

l = [1, 2, 3, 4]
## Basic list comprehension
#r = [ n + 5 for n in l]
#print(r)

## list comprehension with if condition
#r = [n + 2 for n in l if n >= 2]
#print(r)

## list comprehension with if and else condition
r = [n + 100 if n > 2 else n + 10 for n in l]
print(r)

'''
1. using iterators we can get sequence of values based on demand by using next() function.
2. We can create iterators by using iter() function.
'''

l = [1,2,3,4,5]

#for i in l:
#    print(i)

iter_obj = iter(l)

print(next(iter_obj))

print(next(iter_obj))


for i in iter_obj:
    print(' For loop ', i)



#print(next(iter_obj))

'''
1. Using generator we can execute a block of code based on demand by using next() function.
2. using yield keyword we can create a generator.
'''

def gen_fun(n):
    for i in range(n):
        print('Before yield')
        yield i
        print('After yield')

#gen_obj = gen_fun(10)
#print(next(gen_obj))
#print(next(gen_obj))
# print(next(gen_obj))

## Iterate based on for loop
#for i in gen_obj:
#    print(' For Loop ', i)


def gen_fun(n):
        print('Before return')
        yield n
        print('After return')
        yield n

gen_obj = gen_fun(10)
print(next(gen_obj))
print(next(gen_obj))

'''
1. You can access to the command line parameters using the sys.argv 

 Example ::- command_line_argu.py "sriram chowdary" 78
'''
import sys

## To get first command line argument
print(' argv[1] :: ' , sys.argv[1])

## To get second command line argument
#print(' argv[2] :: ' , sys.argv[2])

## To get file name with full path
#print(' argv[0] :: ' , sys.argv[0])

## To get all command line argument with file name
#print(' argv :: ' , sys.argv)

'''
1. Using standard input we can get values at run time.
2. using input() function we can get run time values in python.
'''

uname = input('\n Please enter your name ::')
pin   = input('\n Please enter PIN   ::')

print(' \n UNAME IS : ', uname)
print(' \n PIN   IS : ', pin)

'''
1. Using string format we can create a new string
'''

#l = input(' please enter about python : ')

s = '\n < {0} > is a {1} language '.format('python','bad')

print(s)

'''
1. The OS module in python provides functions for interacting with the operating system. 
'''
import os

#print(dir(os))

# To create a directory
#os.mkdir('TODAY')

# To remove directory
#os.rmdir("TODAY")

# To create a file
#open("my_file.py", 'w')

# To rename a file 
#os.rename('my_file.py', 'SSS.py')

# To check file is exist or not return True is exist or False
#status = os.path.isfile('SSS.py')
#print(' Status :', status)

# To get current working directory
#print('import os getcwd is:: ', os.getcwd())

# To change execution directory
#os.chdir(r'C:\Users\mallemputi.chowdary\Desktop\INST')
#print('import os getcwd is :: ', os.getcwd())

# To run system commands
#print(os.system('dir'))
os.system('python today.py')

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

import time

print(' \n Before sleep ', time.ctime())
time.sleep(5)
print(' \n After sleep  ', time.ctime())

'''
1. Praramiko module is used to do operations on remote machine.
2. used to run commands on remote host and copy file from local to remote and remote to local.
1. To install module ==> python -m pip install paramiko
'''
import paramiko

h_name = '10.122.32.135'
u_name ='smellamp'
p_word = '8Aug2019'
port_no = 22   # ssh port

# To create ssh object
ssh = paramiko.SSHClient()

## To Add unknown host automaticllay 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# To create a connection on remote machine
ssh.connect(h_name, username=u_name, password=p_word, port=port_no)

# To run commnd on remote host 
stdin, stdout, stderr = ssh.exec_command('ls /home/smellam')

## To get command output
print(' \n stdout is ::', stdout.readlines())

## To get error message if any failures 
print(' \n stderr is ::', stderr.read())
ssh.close()

'''Put_get.Py'''

import paramiko

host_name = '10.122.32.135'
u_name ='smellamp'
p_word = '8Aug2019'
port_no = 22

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_name, username=u_name, password=p_word, port=port_no)
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")


## Create FTP object to copy file from local to remote and remote to local
ftp = ssh.open_sftp()

## Copy file from remote machine to local machine
rsrc = '/home/smellamp/srikumar.py'
ldst = r'C:\Users\smellamp\Desktop\DU_TELEF\srikumar.py'

ftp.get(rsrc, ldst)

## Copy file from local machine to remote machine
lsrc = r'C:\Users\smellamp\Desktop\DU_TELEF\LOCAL.txt'
rdst = '/home/smellamp/sss.py'

ftp.put(lsrc, rdst)

# close ftp and ssh connections
ftp.close()
ssh.close()


'''
1. Using logging module we can log based on severity level.
2. By default, there are 5 standard levels indicating the severity of events. 
3. Log levels are ==> DEBUG, INFO,WARNING,ERROR,CRITICAL
4. The default level is WARNING
'''

import logging

logging.info(" TEST 1 ")
logging.debug(" TEST 2 ")
logging.warning(" TEST 3 ")
logging.error("   TEST 4 ")
logging.critical(" TEST 5 ")

'''
 datefmt='%m/%d/%Y %I:%M:%S %p'
'''
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(message)s ',
                    datefmt='%m:%d:%Y %H::%M',
                    filename='debug.log',
                    filemode='w')

logging.info(' :: TEST 1 ')
logging.debug(' :: TEST 2 ')
logging.warning(' :: TEST 3 ')
logging.error(' :: TEST 4 ')
logging.critical(" :: TEST 5 ")

'''debug'''

INFO 09:17:2020 07::51  :: TEST 1  
DEBUG 09:17:2020 07::51  :: TEST 2  
WARNING 09:17:2020 07::51  :: TEST 3  
ERROR 09:17:2020 07::51  :: TEST 4  
CRITICAL 09:17:2020 07::51  :: TEST 5  


'''
1. Threading is used to run multiple functions/jobs concurrently(at the same time)
2. Using threading module we can achive threading in python.
## target: the function to be executed by thread
## args: the arguments to be passed to the target function
## name: We can specify a name to the thread
## join: Using join function we keep a thread to wait till ending the thread
'''
import threading
import time

def first_fun():
    print(' \n first_thread started')
    time.sleep(3)
    print(' \n first_thread ended')

def second_fun(a,b):
    print(' \n second_thread started')
    time.sleep(7)
    print(' \n second_thread ended')

#first_fun()
#second_fun(3,4)


ft = threading.Thread(target=first_fun)
st = threading.Thread(target=second_fun, args=('sriram','chowdary'))

ft.start()
#ft.join()
st.start()

'''
1. threading.activeCount(): Returns the number of total Python thread that are active. 

'''

import threading
import time


def fun1():
    time.sleep(1)

def fun2():
    print(' \n Total threads count is :::::', threading.activeCount())


t1 = threading.Thread(target=fun1, name='add')
t2 = threading.Thread(target=fun2, name='sub')

#t1.start()
t2.start()

'''
1. threading.currentThread(): Returns the currentThread object
'''
import threading
import time


def fun1():
    print(' \n Fun1 thread name is :::::', threading.currentThread().getName())

def fun2():
    print(' \n Fun2 thread name is :::::', threading.currentThread().getName())


t1 = threading.Thread(target=fun1, name='add')
t2 = threading.Thread(target=fun2, name='sub')

t1.start()
t2.start()

'''ROBOT FRAMEWORK'''

What is Framework?
A framework is a collection of functions that can be used to achieve particular task.

Python Frameworks:       Django, Flask and Robot Framework
Java Frameworks:           Spring, Hibernate and Struts
Java Script Frameworks: React, and Angular 


Robot Framework Features 

1.Robot Framework is a Python and Java based keyword-driven test automation framework
2.Robot Framework is an open source and platform independent framework
3.Robot Framework is a generic test automation framework
4.By default, Robot Framework creates an XML output file and a log and a report in HTML format.
5.Official sit is for more information http://robotframework.org/
6.Provides ability to create reusable higher-level keywords from the existing keywords.
7.Provides tagging to categorize and select test cases to be executed.
Provides test-case and test-suite -level setup and teardown

*** Settings ***
Documentation    To know how to create test cases


*** Test Cases ***
testcase1
    log to console    \n TEST CASE ONE

testcase2
    log to console    \n TEST CASE TWO

TestCase3
    log to console    \n TEST CASE THREE


*** Settings ***
Documentation    To know how to do mathematical operations


*** Test Cases ***
Addition
    ${RV}    Evaluate    5 + 6
    log to console    \n addition of 5 + 6 = ${RV}

Sub
    ${r} =    Evaluate    45 - 5
    Log     test Case SUB ==> ${r}    ERROR

Robot frame work has 3 types of data types(Variables)

1. Scalar
2. List
3. Dictionary

# Scalar
    1. Using scalar variable we can store single value
    2. Using ${dollar} symbol we can create scalar variable
    # Example : ${name} =    SRIRAM

# List
    1. List is used to store multiple value
    2. Using @{attherate} symbol we can create List variable
    # Example : @{names} =    SRIRAM    KUMAR    BALU    BABU

# Dictionary
    1. Dictionary is used to store data in key value foramt
    2. Using &(Ampersand) symbol we can create Dictionary variable
    # Example : &{EMP_DET} =    name=SRIRAM    eid=78    did=9


*** Settings ***
Documentation   To know how to do scalar operations

*** Variables ***
${NAME}     Sri

*** Test Cases ***
Scalar Operations
    ${NAME}     Catenate    ${name}    Kumar
    Log    ${NAME}    WARN

*** Keywords ***
    


*** Settings ***
Documentation   To know how to do list operations

*** Variables ***
@{NAMES}    sriram    Nagesh    Balu

*** Test Cases ***
List Operations
    Log    ${NAMES}          ERROR
    Log    ${NAMES}[0:2]       ERROR


*** Settings ***
Documentation   To know how to do Dictionary operations

*** Variables ***
&{DICT}   name=kumar    eid=345    dname=IT

*** Test Cases ***
Dict Operations
    Log    ${DICT}    WARN
    Log    ${DICT}[name]    WARN

*** Settings ***
Documentation   *  Library for generating, modifying and verifying strings *

Library    String

*** Variables ***
${name}         SRIRAM
${FULL_NAME}    sriram sri
${SPLIT}        sri,ram,kumar

*** Test Cases ***
Testcase:1
    #${name}    Convert To Lowercase    ${name}
    #Log    After Converting Lowercase ==> #${name}    ERROR

    #${FNAME}   Remove String    srikumar     kumar
    #Log    After Removing SUB STRING ==> ${FNAME}    ERROR

    #${FULL_NAME}    Replace String    ${FULL_NAME}    #sri    sai   1
    #Log    After Replace ==> ${FULL_NAME}    WARN

    #${SPLIT}    Split String    ${SPLIT}    ,    1
    #Log    After spliting ==> ${SPLIT}    ERROR

    ${SUBSTRING}    Get Substring    ${name}    0    3
    Log    Substring is ==> ${SUBSTRING}    WARN


*** Settings ***
Documentation   To know how to do list operations

Library    Collections

*** Variables ***
${ONE}     5

*** Test Cases ***
List Operations
    ${L}    Create List
    Append To List    ${L}   one   2   3   4
    log    List values are :: ${L}    WARN

    #${R} =    Get From List    ${L}    2
    #log    Second index value :: ${R}    WARN

    #Remove From List  ${L}   0
    #log    After removing based on index :: ${L}    #ERROR

    Remove Values From List   ${L}   3   4
    log    After removing based on value ==> ${L}    WARN

*** Settings ***
Documentation   To know how to do Dict operations

Library    Collections

*** Variables ***
${TWO}    sriram

*** Test Cases ***
Dict Operations
    ${D}    Create Dictionary    name=${TWO}    dno=34
    Log     Dict is :: ${D}    WARN

    #${r}    Get From Dictionary    ${D}    name
    #Log     Name is : ${r}     WARN

    #${K}    Get Dictionary Keys    ${D}
    #Log     Keys are : ${K}     WARN

    Remove From Dictionary    ${D}    name
    Log     Dict IS :: ${D}    WARN

# Robot support all python comparison operations
==, !=, >, <,>=, <= 

1. In robot we can't create if block. If we want to run a block of code based on condition then we have to create a keyword with  block of code then we can run this keyword based on condition using "Run Keyword If" KEYWORD.
# Example :- Run Keyword If   2 == 2    Add    ${ONE}    5

2. In robot we can use IF and ELIF and ELSE also, like below

    Run Keyword If   2 == 4    Log    if block      WARN
    ...   ELSE IF    3 == 3    Log    first elif    WARN
    ...   ELSE IF    3 == 6    Log    Second elif   WARN
    ...   ELSE    Log   Else block is     ERROR

*** Settings ***
Documentation    To know how to do conditional operations


*** Test Cases ***
IF Statement
    Run Keyword If   2 == 2    Log    Simple if    ERROR


*** Settings ***
Documentation    To know how to do conditional operations

*** Test Cases ***
IF AND ELSE Statements
    Run Keyword If   7 <= 6    Add
    ...   ELSE IF    3 != 3    Log    first elif    WARN
    ...   ELSE IF    3 >= 6    Log    Second elif   WARN
    ...   ELSE    Log   Else block is     ERROR

*** Keywords ***
Add
    ${r}    Evaluate    45 + 5
    Log     SUM of 45 + 5 is ==> ${r}    ERROR

*** Settings ***
Documentation    To know how to use logical operations
Library    Collections

*** Variables ***
${ONE}    8

*** Test Cases ***
Logical Operations
    Run Keyword If   2 >= 4 or ${ONE} == 8   Log     LOGICAL OR \n    WARN

    Run Keyword If   2 > 1 and ${ONE} == 8   Log    LOGICAL AND \n    WARN


*** Settings ***
Documentation    To know how to use Membership operations

*** Variables ***
@{NAMES}    Sriram    balu    nagesh
${NAME}     'sriram'

*** Test Cases ***
Membership Operations
    Run Keyword If   'sri' in ${NAME}    Log   IN    ERROR

    #Run Keyword If   'Sri' not in ${NAMES}   Log   NOT #IN     ERROR


Robot framework supports only for loop


Loop statements in robot

1. Continue For Loop If  => To skip current iteration based on condition
2. Exit For Loop If      => To terminate loop based on condition


*** Settings ***
Documentation    Loop operations using list

*** Variables ***
@{names}     sriram    kumar    balu    nagesh

*** Test Cases ***
For Loop with list
    FOR    ${name}    IN    @{names}
      log    ${name}    WARN
      Log    OK
    END


*** Settings ***
Documentation    Loop operations using range function

*** Variables ***
${ONE}     10

*** Test Cases ***
Test For Loop
    FOR    ${INDEX}    IN RANGE    2    9    2
      log    ${INDEX}    WARN
    END


*** Settings ***
Documentation    Loop operations using list


*** Test Cases ***
For Loop with list
    FOR    ${V}    IN RANGE    1    8
        Continue For Loop If    ${V} >= 3
        Exit For Loop If        ${V} <= 5
        log    ${V}    WARN
    END

'''KEYWORD'''

1. Keyword is a block of robot code.

2. Keyword contains [Arguments], [Documentation] and [Return]satements.

3. We can create user define keywords inside *** Keywords *** section.


*** Settings ***
Documentation    To know how to create keywords


*** Test Cases ***
testcase:1
    Addition

testcase:2
    Subtraction    9    5


testcase:3
    ${RV} =    Multiplication    5    10
    Log      Multip OF 5 * 10 = ${RV}    ERROR


*** Keywords ***
Addition
    [Documentation]   Keyword without arguments
    ${SUM}    Evaluate    5 + 5
    Log    SUM OF 5 + 5 = ${SUM}    ERROR

Subtraction
    [Arguments]    ${A}    ${B}
    [Documentation]   Keyword with arguments
    ${SUM}    Evaluate    ${A} - ${B}
    Log    Subtraction OF ${A} - ${B} = ${SUM}    WARN

Multiplication    [Arguments]    ${A}    ${B}
    ${R}    Evaluate    ${A} * ${B}
    #[Return]    ${R}
    Return From Keyword If    2 == 6   ${R}


*** Settings ***
Documentation    To know how to create keyword with default arguments

*** Test Cases ***
testcase:1
    Addition    B=10    A=6

*** Keywords ***
Addition
    [Arguments]    ${A}    ${B}
    Log    A value is :: ${A}    WARN
    Log    B value is :: ${B}    WARN


*** Settings ***
Documentation    To know how to create keyword with default arguments

*** Test Cases ***
testcase:1
    Addition

*** Keywords ***
Addition
    [Arguments]    ${A}=20    ${B}=15
    Log    A value is :: ${A}    WARN
    Log    B value is :: ${B}    WARN


# What is resouce file ?
1. Resource file a robot file which dosn't contains Test Cases section.
2. Resource file contains common keywords which are using many test suits.
3. Using resource file we can reuse the keywords efficiently.

# How to import resource file ?
1. Using Resouce keyword we can import resorce file
  # Exaple :- Resource    common_keywords.robot
  
## To import from another path
  #Resource     C:\\Users\\smellamp\\Desktop\\PYTHON\\common_keywords.robot


*** settings ***
Documentation   This file is used to make math operations

*** Variables ***
${NAME}     SRIRAM


*** Keywords ***
Addition    [Arguments]    ${A}    ${B}
    ${R}    Evaluate    ${A} + ${B}
    Log    SUM OF ${A} + ${B} = ${R}    WARN


*** settings ***
Documentation   To know how to import resouce file

Resource    common_keywords.robot


*** Test Cases **
Testcase:1
    Addition    5    5
    Log    ${NAME}    ERROR


*** settings ***
Documentation   To know how to import resouce file

Resource    common_keywords.robot


*** Test Cases **
Testcase:1
    Addition    34    6


# What is Library file ?
1. Library is a python file which contains set of functions
2. Using "Library" keyword we can import Library file


# How to import Library file ?
Library    common_library.py

## To import from another path
#Library    C:\\Users\\smellamp\\Desktop\\PYTHON\\common_library.py


name = 'SRIRAM'

def emp_details():
    print('\n emp name is :', name)

def add(a,b):
    return int(a) + int(b)


*** settings ***
Documentation   To know how to import library files

Library    common_library.py

*** Test Cases **
Calling Python Function
    Emp Details
    ${R}    Add    5    10
    Log    ${R}     ERROR
    Log     ${name}    ERROR


# What is Variable file ?
2. Variable file contains all common variables which are using many test suits.
3. Using Variable file we can reuse the Variables efficiently.

# How to import Variable file ?
1. Using Variable keyword we can import Variable file
  # Exaple :- Variable    common_Variable.py
  
## To import from another path
  #Variable     C:\\Users\\smellamp\\Desktop\\PYTHON\\common_Variable.py


NAME    = 'kumar'
no      = 345
names   = ['sriram','kumar','balu','nagesh']
emp_det = {'name':'sriram', 'eid':34, 'dname':'IT'}

def add():
    pass


*** settings ***
Documentation   To know how to import variable files

Variables    variables_file.py

*** Test Cases **
Get Variables
    Log    ${NAME}       WARN
    Log    ${no}         WARN
    Log    ${names}      WARN
    Log    ${emp_det}    WARN


## [Setup]
setup is something that is executed before a test case to do required setup for test case execution.

#Example: open a file, start process and create a connection


## [Teardown]
Tear down will execute after executing the test case to do cleanup process.

# Example: close a file, stop process and close a connection


## Suite Setup    :--
It will execute before executing the all test cases
# Example: open a file, start process and create a connection

## Suite Teardown:-
It will execute after executing the all test cases

# Example: close a file, stop process and close a connection

*** Settings ***
Documentation   *  To know how to use setup and teardown options *

*** Test Cases ***
Testcase1
    [Setup]       Log    Setup FOR FIRST TEST CASE    WARN
    Log    Test Case : 1   ERROR
    [Teardown]    Log    Teardown FOR FIRST TEST CASE    WARN

Testcase2
    [Setup]    Log    Setup FOR SECOND TEST CASE    WARN
    Log    Test Case : 2   ERROR
    [Teardown]    Teardown Section

*** Keywords ***
Teardown Section
    Log    TEARDOWN SECTION     WARN
    Log    ok



*** Settings ***
Documentation   *  To know how to use setup and teardown options *

Suite Setup       Log    Suite Setup    ERROR
Suite Teardown    Log    Suite Teardown    ERROR

*** Test Cases ***
Testcase1
    Log    Test Case 1   ERROR
    [Teardown]    Log    Teardown FOR FIRST TEST CASE    WARN
    [Setup]    Log    Setup FOR FIRST TEST CASE    WARN

Testcase2
    [Setup]    Log    Setup FOR SECOND TEST CASE    WARN
    Log    Test Case 2   ERROR
    [Teardown]    Log    Teardown FOR SECOND TEST CASE    WARN

*** Keywords ***
Teardown Section
    Log    TEARDOWN SECTION     WARN

# [Tags] 
1. Using tags we can give alias name to the test cases to categorize(group). test cases like (sanity, smoke, regression).
2. With tags, we can include or exclude test cases to execute.

*** settings ***
Documentation   To know how to use tags

*** Test Cases **
Testcase:1
    [Tags]    win
    Log    WIN TestCase 1    ERROR

Testcase:2
    [Tags]    Linux
    Log    Linux TestCase 2    ERROR

Testcase:3
    [Tags]    win
    Log    WIN TestCase 3    ERROR

Testcase:4
    [Tags]    MAC
    Log    MAC TestCase 4    ERROR

Testcase:5
    [Tags]    Linux
    Log    Linux TestCase 5    ERROR



# To know robot version
robot --version

# To run particular test case and Test cases 
    robot -t "Add Two Values" first_test.txt
    robot -t Addition -t "Test Case 3" first_test.txt
    robot -t  Add* first_test.txt

# paasing values to variable through command line =>
    robot -v ONE:10 -v TWO:34 Loop.txt

# validate the test data
    robot --dryrun test2_list.robot

# TO run a test case based on tag
    robot -i test2 first_test.txt

# TO run all test cases except given tag
    robot -e test2 first_test.txt

# Change logs path ==> 
    robot -d C:\ON-LINE\COURSES\2_ROBOT\Logs TEST_SUITE.robot
    robot -d LOGS TEST_SUITE.robot
                'OR' 
    robot --outputdir LOGS TEST_SUITE.robot


*** settings ***
Documentation   To know how many options to run ro bobot file

*** Variables ***
${ONE}     99

*** Test Cases **
Testcase:1
    Sleep     0s
    Log    TestCase 1 ==> ${ONE}   ERROR

Testcase:2
    Sleep     0s
    Log    TestCase 2    ERROR

Add
    Sleep     1s
    Log    TCase 3    ERROR

*** Settings ***
Documentation   *  Provides a set of often needed generic keywords. Always automatically available without imports *

Library    Builtin

*** Variables ***
${name}    SRIRAM

*** Test Cases ***
Testcase:1
     #Log To Console    ${name}
     #Sleep    1s
     #Log    Name is = ${name}    WARN
     #Run Keyword If    3 == 3    Log    IF    ERROR
     Repeat Keyword    3    Log   SRIRAM    WARN


*** Settings ***
Documentation   *  Provides a set of keywords for handling Python lists and dictionaries. *

Library    Collections

*** Variables ***
${ONE}    5
${TWO}    sriram

*** Test Cases ***
List Operations
    ${L}    Create List
    Append To List    ${L}   one   2   3   ${TWO}
    log    List values are :: ${L}    WARN
    ${R} =    Get From List   ${L}    2
    log    Second index value :: ${R}    WARN
    Remove From List  ${L}   0
    log    After removing based on index :: @{L}    ERROR
    Remove Values From List   ${L}   sriram
    log    After removing based on value ==> ${L}    WARN

Dict Operations
    ${D}    Create Dictionary    name=sriram    dno=34
    Log     Dict is :: ${D}    WARN
    ${r}    Get From Dictionary    ${D}    name
    Log     Name is : ${r}     WARN
    ${K}    Get Dictionary Keys    ${D}
    Log     Keys are : ${K}     WARN
    Remove From Dictionary    ${D}    name
    Log     Dict values are :: ${D}    WARN


*** Settings ***
Documentation   *  Enables various operating system related tasks to be performed in the system where Robot Framework is running. *

Library    OperatingSystem

*** Variables ***
${ONE}    5
${TWO}    3

*** Test Cases ***
#First Test Case
    #Create Directory    LOG
    #Create File     LOG/log_file.txt
    #Remove File    LOG/log_file.txt
    #Remove Directory    LOG
    #File Should Exist    LOG/log_file.txt    Please create a log_file.txt

Run System Command
    ${r}    Run    dir
    Log    ${r}    ERROR



*** Settings ***
Documentation   *  Library for generating, modifying and verifying strings *

Library    String

*** Variables ***
${name}         SRIRAM
${FNAME}        srikumar
${FULL_NAME}    sriram sri
${SPLIT}        sri,ram,kumar

*** Test Cases ***
Testcase:1
    #${name}    Convert To Lowercase    ${name}
    #Log    After Converting Lowercase ==> #${name}    ERROR

    #${FNAME}   Remove String    ${FNAME}     kumar
    #Log    After Removing SUB STRING ==> #${FNAME}    ERROR

    #${FULL_NAME}    Replace String    #${FULL_NAME}    sri    sai   1
    #Log    After Replace ==> ${FULL_NAME}    WARN

    #${SPLIT}    Split String    ${SPLIT}    ,
    #Log    After spliting ==> ${SPLIT}    ERROR

    ${SUBSTRING}    Get Substring    ${name}    0    3
    Log    Substring is ==> ${SUBSTRING}    WARN

*** Setting ***
Library    SeleniumLibrary

*** Test Cases ***
Login facebook
    Open Browser    http://www.facebook.com    Chrome
    Maximize Browser Window
    Sleep    5
    Input Text        email    sriram.python111@gmail.com
    Sleep    5
    Input Text        pass     password
    Sleep    5
    Click Button      Log In
    Sleep    5
    Close Browser


'''SELENIUM'''

# What is Selenium
    Selenium is a free (open source) automated testing tool for web applications across different browsers and platforms. 
    
    Selenium has four components.
        1. Selenium Integrated Development Environment (IDE)
        2. Selenium Remote Control (RC)
        3. WebDriver
        4. Selenium Grid

# How to install selenium
    python -m pip install selenium

# How to check Selenium Version
import selenium
print(selenium.__verison__)

# What are web drivers ?
    Selenium provides few drivers that help you to perform actions on browser. 

    Below are the drvers: 
        1. ChromeDriver   --> for Chrome
        2. GeckoDriver    --> for Firefox
        3. IEDriverServer --> for Internet InternetExplorer

# How to select required Chrome driver
    We have to download ChromeDriver based on Chrome Version

# How to find element in Webpage
    Using Developer tools

# Ways to go into Developer tools ?
    1. Right click on webpage --> inspect
    2. By clicking F12 key
    3. Control + Shift + C 


from selenium import webdriver
import selenium
import time

# To Know selenium VERSION
print(' \n SELENIUM VERSION IS :: ', selenium.__version__)


# Open a Browser 
driver = webdriver.Chrome()
time.sleep(3)

## If Chrome driver in different path
# driver = webdriver.Chrome(r'C:\\Users\\TEST\chromedriver.exe')

## To Maximize window
driver.maximize_window()
time.sleep(3)

## Open a URL
driver.get('https://accounts.lambdatest.com/login')
time.sleep(3)

## To enter username in text box based on ID Locator
uname = driver.find_element_by_name('email')
uname.send_keys('sriram.python111@gmail.com')
time.sleep(5)

## To enter password in text box based on name Locator
password = driver.find_element_by_id('userpassword')
password.send_keys('sriram.python111')
time.sleep(5)

## To click on login button
login_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[3]/button')
login_button.click()

## Close a browser
driver.close()

## Please complete below steps one by one

1. Install Selenium

2. Find selenium Version

3. Creare seperate folder for you selenium scripts

4. download required chrome driver and place in your selenium scripts folder
    # Link for download chrome driver : https://chromedriver.storage.googleapis.com/index.html

5. create a login_page.py file inside selenium diractory

6. write code for below actions inside login_page.py file 
    
    1. import webdriver from selenium
    2. create a driver for Chrome brower
    3. Maximize browser window
    4. Enter login page URL('https://accounts.lambdatest.com/login')
    5. Find element for uname text box
    6. Enter uname
    7. Find element for password text box
    8. Enter password
    9. Find element for login button text box
   10. Click on login button 
   11. Colse browser


from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")
time.sleep(4)
## Get text based on xpath
text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

print('\n Text is :', text)


time.sleep(4)
driver.close()


from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://www.python.org')
d.maximize_window()
time.sleep(5)

# Take screenshot
d.save_screenshot(r'C:\Users\smellamp\Desktop\INCEDO\PYTHON999.png')
d.close()

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")

## click on specified element
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downloads"]/a').click()
time.sleep(5)
driver.back()
time.sleep(7)
driver.forward()
time.sleep(7)
driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")


time.sleep(10)
driver.refresh()
time.sleep(7)
driver.refresh()
time.sleep(5)
driver.close()


from selenium import webdriver
import time

# Open a Chrome Browser
d = webdriver.Chrome();
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(10)

# To Scroll down page
d.execute_script("window.scrollTo(0, 200)")
time.sleep(6)
d.execute_script("window.scrollTo(200, 400)")
time.sleep(6)

# To Scroll up page
d.execute_script("window.scrollTo(500, 0)")
time.sleep(5)
d.close()

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")

## Move cursor on specified element and click
time.sleep(3)
actions = ActionChains(driver)
obj = driver.find_element_by_xpath('//*[@id="authentication"]/button')
actions.move_to_element(obj)
time.sleep(3)
actions.double_click()
time.sleep(3)                                                                                                                                                    
actions.perform()

time.sleep(10)
driver.close()

from selenium import webdriver
import time

# Launch Firefox browser
d = webdriver.Chrome()
d.get('https://python.org')

# To Get Window Title
w_title = d.title

print('\n Window title is : ', w_title)
time.sleep(3)

assert w_title == 'Welcome to Python.org' , ' Title is not matched '


time.sleep(10)
d.close()

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")
time.sleep(5)


driver.execute_script("document.body.style.zoom='300%'")
time.sleep(7)
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(5)
driver.close()

from selenium import webdriver
import time

d = webdriver.Chrome()
d.maximize_window()
d.get("https://accounts.google.com/")
time.sleep(5)

## Open a new tab with URL
d.execute_script("window.open('http://bings.com')")
time.sleep(5)


## Open a new tab without URL
d.execute_script("window.open()")
time.sleep(5)


## Open a new URL on same tab
d.execute_script('window.open("https://www.pylint.org/","_current")')
time.sleep(8)

# TO close only current tab
#d.close()

# TO close all tabs 
d.quit()


from selenium import webdriver
import time

# Open chrome browswer
d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(5)

## Open a new tab with given URL
d.execute_script("window.open('http://robotframework.org/')")
time.sleep(5)

## Open a second tab with given URL
d.execute_script("window.open('https://mail.google.com')")
time.sleep(5)

#### To get all windows tabs
windows = d.window_handles

print('\n windows', windows)

print('\n Default tab title :', d.title)
time.sleep(5)

## Switch into first tab from right side 
d.switch_to.window(windows[1])
time.sleep(5)
print('\n windows[1] title is ', d.title)

## Switch into second tab from right side 
d.switch_to.window(windows[2])
time.sleep(5)
print('\n windows[2] title is ', d.title)

## Switch into first tab(Default tab) from left side
d.switch_to.window(windows[0])
time.sleep(5)
print('\n windows[0] title is  ', d.title)

d.quit()

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(5)

select_element = driver.find_element_by_id('MONTHS')

months = Select(select_element)
time.sleep(5)
## To select a value based on visable text
#months.select_by_visible_text('May')
#time.sleep(5)

## To select a value based on value
#months.select_by_value('Apr')
#time.sleep(5)

## To select a value based on index
months.select_by_index(1)

time.sleep(10)
driver.close()


from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.maximize_window()
d.get(r'C:\ON-LINE\3_SELENIUM/alert_2.html')
sleep(5)

d.find_element_by_xpath('/html/body/button').click()

alert = d.switch_to.alert

#  To get alert message
print(' \n\n ' , alert.text)
sleep(5)

## To accept alert
alert.accept()

# alert.accept()  – used to accept the Alert
# alert.dismiss() – used to cancel the Alert
# alert.send_keys(' sriram ') – used to enter a value in the Alert text box.

sleep(10)
d.close()

from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(5)


# Select Check box
obj = driver.find_element_by_id('vehicle1')
obj.click()
time.sleep(5)

driver.close()

from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(3)


# Select radio button
driver.find_element_by_id('age4').click()

time.sleep(10)
driver.close()

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')
time.sleep(5)

e = driver.find_element_by_link_text('Gmail')
print('\n\n LINK TEXT : ', e.text)

#elem = driver.find_element_by_partial_link_text("Gma")
#print('\n\n Partial LINK TEXT : ', elem.text)

#el2 = driver.find_element_by_tag_name('a')
#print('\n\n  TAG : ', el2.text)

#e = driver.find_element_by_class_name('gb_g')
#print('\n\n CLASS : ',e.text)

#e = driver.find_element_by_css_selector('.gb_g')
#print('\n\n  CSS : ',e.text)

time.sleep(3)
driver.close()

Implicit waits are used to provide a default waiting time between each consecutive test step/command across the entire test script.
Thus, the subsequent test step would only execute when the specified amount of time has elapsed after executing the previous test 
step/command.
Explicit waits are used to halt the execution until the time a particular condition is met or the maximum time has elapsed.
Unlike Implicit waits, Explicit waits are applied for a particular instance only.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://selenium-python.readthedocs.io")
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[5]/aaa').click()

driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://selenium-python.readthedocs.io")


# To create wait object
wait = WebDriverWait(driver, 10)

r = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[5]/ad')))

r.click()

driver.close()

''' REST API'''
REST: -    Representational State Transfer
API: -       Application Programing Interface
HTML: - Hyper Text Markup Language
HTTP: Hyper Text Transfer Protocol

REST requires the interaction between the customer and server
REST have a URL structure and a request/response pattern the revolve around the use of resources
REST is a type of software architecture and a method for users to request data or information from servers
REST requires the interaction between the customer and server

there are 39 Methods in REST API 
Mainly 9 --- Put, Post, Put, DElete, Head, PAtch, Options, Connect, Trace

'''Server Code should to be always in run'''

from flask import Flask, jsonify, request
import time

app = Flask(__name__)
cust_det = {'cust1':'KUMAR', 'cust2':'Balu'}

@app.route('/get', methods=['GET'])
def get_cust_details():
    '''
    To get all customer details
    '''
    time.sleep(2)
    return jsonify(cust_det)

@app.route('/create', methods=['POST'])
def create_customer():
    '''
    To create new record
    '''
    d = request.json
    cust_det.update(d)
    return jsonify(cust_det)

@app.route('/update', methods=['PUT'])
def update_emp():
    '''
    To update emp details
    '''
    d = request.json
    cust_det.update(d)
    keys = list(d.keys())
    k = keys[0]
    return ' {0} RECORD UPDATED SUCCESSFULLY'.format(k)

@app.route('/delete', methods=['DELETE'])
def delete_emp():
    '''
    To delete emp record
    '''
    d = request.json
    keys = list(d.keys())
    k = keys[0]
    del cust_det[k]
    return ' {0} record Deleted SUCCESSFULLY'.format(k)


l = []
@app.route('/list', methods=['POST'])
def add_list():
    '''
    Add values to the list
    http://127.0.0.1:5000/list
    {"list":[1,2,3,4]}
    '''
    d = request.json
    keys = list(d.keys())
    v = d[keys[0]]
    l.extend(v)
    print('\n\n\n\n ', type(v))
    return '{0}'.format(l)

# To run app
app.run(debug=True)


'''Example for REST API Testing'''

import requests

## To get all customers details
res_obj = requests.get('http://127.0.0.1:5000/get')

## If Credentials required
#res = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('uname', 'password'))

print('\n response code is  :', res_obj.status_code)
print('\n CUST details are  :', res_obj.json())

## To create new customer record
r = requests.post('http://127.0.0.1:5000/create', json={"cust3":"SRI"})
print('\n response code is :', r.status_code)
print('\n response DATA is :', r.json())

## To Update emp 
r = requests.put('http://127.0.0.1:5000/update', json={"cust2":"Ramesh"})
print('\n response code is :', r.status_code)
print('\n update is :', r.text)


## To Delete emp
r = requests.delete('http://127.0.0.1:5000/delete', json={"cust2":"Ramesh"})
print('\n response code is :', r.status_code)
print('\n Deleted is :', r.text)


GET     ==> Used to get information from web server
POST    ==> Used to create new record in web server
PUT     ==> used to update existing record in web server
DELETE  ==> Used to delete record in web servers

'''PROJECT'''

## Project 1  ::---
1. " PROJECT NAME " is an application to manage all network devices(switchs,routers).
2. Using " PROJECT NAME "  we can manage all network devices configuration(Function).
3. Using " PROJECT NAME "  we can get all network devices information into single point.
4. using " PROJECT NAME " we can change network device functionality also.
5. Using policies(set of Conditions) we can validate device functionality as client requirements.
6. " PROJECT NAME " used to check the device health status.

## Roles and responsibilities:-
1. In this project My Role is automate manual test cases using python
2. I have used Robot Framework for test Suite creation and execution.
3. Developed user define keywords under robot framework as requirement.
4. I have used python concepts like regular Expressions, file handile, OOP's, Modules and Packages.
5. Used Selenium webdriver for automate web based test cases.
6. Used python predefine modules re, selenium, sys, logging and paramiko
7. Attended daily standup meeting to tell what we have done yesterday and what we are going to do today.


## Project 2  ::---
1. " PROJECT NAME " is used to provide Instant Capacity to the servers.
2. using " PROJECT NAME " we can increase capacity instantly rather than waiting weeks for additional resources to arrive and be installed.
3. We can enable additinal cores and memory very quckly based on business requiremnet.
4. It will provide low-cost backup servers.
5. Perform workload balancing among partitions and servers.


## Roles and responsibilities:-
1. Performed Functional, regression and performance testing.
2. Involved into prepare Design documnets and user Guide Documents also.
3. Done manual testing before going to auomate testcase.
4. Developed new modules as requirement.
5. Ran test suite to find new bugs.
6. Attended daily standup meeting to tell what we have done yesterday and what we are going to do today.

