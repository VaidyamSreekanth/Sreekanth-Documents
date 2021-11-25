'''
1. If you have same method names in class A and class B, then if you Inheritence class A into class B then Class A method will override with class B method.
'''
class A():
    def add(self):
        print('\n A ADD ')

class B():
    def add(self):
        print('\n B ADD ')

class C(A, B):
    def add(self):
        print(' \n C ADD ')

inst = C()
inst.add()
