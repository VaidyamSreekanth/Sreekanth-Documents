def dec_fun(f):
   def wrap_fun():
       return ' Hellow ' + f()
   return wrap_fun

@dec_fun
def get_name():
   return 'sriram'

r = get_name()
print(r)



