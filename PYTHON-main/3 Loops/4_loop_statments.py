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

