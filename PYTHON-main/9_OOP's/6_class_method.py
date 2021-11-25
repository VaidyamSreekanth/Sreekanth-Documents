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







