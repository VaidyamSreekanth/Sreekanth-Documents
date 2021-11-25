'''
1. self is used to reffer the instance of the class to the method.
2. Based on self only the method will get to know for which instace it has to responce.
3. We can give any name in place of self.
'''

class One():
    def add(self):
       print(' \n ID of self is  : ',id(self))

    def sub(name, a, b):
        #print(' \n ID of r is     : ',id(name))
        print(' A value is :', a)
        print(' A value is :', b)


ins1 = One()

ins2 = One()

#print(' \n ID of ins1 is  : ',id(ins1))
#ins1.add()

ins1.sub(10,5)

ins2.sub(100,200)





