# from decorator import logger


# @logger
# def greet(username):
#     print("Hello")

# if __name__ == '__main__':
#     greet("Hari")

# print("__name__ is", __name__)


# from mypackage import *

# one()
# two()

def one():
    print("One from main file")

from mypackage import one as on 
one()
on()
