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



