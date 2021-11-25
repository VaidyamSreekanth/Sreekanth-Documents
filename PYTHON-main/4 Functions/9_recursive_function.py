'''
1. A recursive function is a function that calls itself during its execution.
'''

def add(a):
   print('A value is ', a)
   a += 5
   if a > 20: return
   add(a)

add(5)

