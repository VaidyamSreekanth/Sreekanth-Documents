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
