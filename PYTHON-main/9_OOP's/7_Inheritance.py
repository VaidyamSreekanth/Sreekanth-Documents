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
