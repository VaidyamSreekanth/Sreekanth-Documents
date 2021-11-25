# To import linux module from one package
from one import linux

# To import windows module from two package
from one.two import windows

# To import only os function from mac module
from one.three.mac import os

## To call sub function from linux module
linux.sub()


## To print name variable form windows module
print(windows.name)

## To call os function which imported from mac module
os()