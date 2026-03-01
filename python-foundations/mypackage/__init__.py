from mypackage.one import one
from .two import two


#from mypackage.two import two


# print("Hello from init.py")

from .hidden import password

__all__ = ['one', 'two']