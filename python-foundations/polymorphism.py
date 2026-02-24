
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "Woof! "

# class Cat(Animal):
#     def speak(self):
#         return "Meow! "

# animals =  [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())


# def add(x, y, z=0):
#     return x + y + z

# print(add(2, 3))
# print(add(2, 3, 4))

# def add(a,*b):
#     a= 0
#     for i in b:
#         a +=i
#     return a

# print(add(2,2,2))


# def add(*b):
#     a = 0
#     for i in b:
#         a += i
#     return a


# print(add())
# def add(*b):
#     a = ""
#     for n in b:
#         if isinstance(n,int):
#             a =0
#         a += n

#     return a


# print(add())
# print(add(1,2,3,4))
# print(add('h', 'ello'))


def add(**kwargs):
    print(type(kwargs))
    print(kwargs)

    n = True
    if isinstance(n, int):
        print("n is integer")


add(a=1, b=2, c=3, d=4, e=5)
add(x="h", y="ello")
