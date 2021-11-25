## Using constructor we can create instance varables.
## Using __init__ we can create constructor
class One():
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        #print('__INIT__')

    def add(self):
       print(' Add method ', self.uname , self.password)
       
    def sub(self, hostname, port):
        print(' Sub method ', self.uname, self.password)

    def mul(self):
        print(' Mul method ',  self.password )

inst = One('Admin', 'Admin123')

inst.add()
inst.sub('2.3.4.5', 23)
inst.mul()




