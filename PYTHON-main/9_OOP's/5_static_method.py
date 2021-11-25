'''
1. Using @staticmethod decorator we can create static method.
2. For Static method self argument doesn't required.
3. Using staticmethod we can provide same behavior to the all the instances of class.
4. staticmethod we can call through instance or without intance.
'''

class One():
    @staticmethod
    def add():
        print(' Static Method')

#ins = One()
#ins.add()
One.add()







