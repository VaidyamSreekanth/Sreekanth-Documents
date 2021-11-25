'''
1. All name variables and methods are public by default in Python

2. Protected variable we can define By prefixing the name of your variable or method with a single underscore, you’re telling others “don’t touch this, unless you’re a subclass”

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






