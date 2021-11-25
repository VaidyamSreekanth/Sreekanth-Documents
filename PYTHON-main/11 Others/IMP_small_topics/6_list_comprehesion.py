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

