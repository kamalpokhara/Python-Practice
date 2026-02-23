# print(5+True+False)
'''
Docstring for bool
a = True
b= False
c = True
print(a and b)
print(a or b)
print(not b)


print( 5 < 6 )
print( 5 > 6 )
print( -12 > 0)

age = input(" Input age ")

if 32 == int(age):
    print(' you are 32 years old ')
else:
    print(' you are NOT 32 years old ')

'''

a = 100000000000
b = 100000000000
print(a == b)  # True (cached)

a = 100000000000
b = 257
print(a is b)  # False (different objects)
 
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same contents)
print(a is b)  # False (different lists)
