'''
1. We can inherit a derived class from another derived class, this process is known as multilevel inheritance
2. Example :- We have three classes A, B and C, If you inheritance class A into class B and class B into class C This is called Multi inheritance.
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
