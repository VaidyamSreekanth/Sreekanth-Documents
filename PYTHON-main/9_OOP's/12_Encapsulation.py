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
