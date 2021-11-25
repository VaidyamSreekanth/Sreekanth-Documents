'''
__init__.py file is used to import modules into package from another path.
'''
## TO import windows module from two package to one package
from .two import windows


## To import only os function into one package from three package mac module
from .three.mac import os


## To import vmware module into one package
from .three.four import vmware


## To import linux module into one package
from . import linux
