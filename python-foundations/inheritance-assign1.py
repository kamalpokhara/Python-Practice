from abc import ABC, abstractmethod

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal {self.name} created")

#     def move(self):
#         print(f"{self.name} moves in some way.")


# class Walker(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def move(self):
#         print(f"{self.name} walks on land.")


# class Swimmer(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def move(self):
#         print(f"{self.name} swims in water.")


# class Frog(Swimmer, Walker):

#     def __init__(self, name):
#         Walker.__init__(self, name)
#         Swimmer.__init__(self, name)


# frog = Frog("Freddy")
# print(Frog.__mro__)
# frog.move()


class Animal(ABC):
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created")

    @abstractmethod
    def move(self):
        pass


class Walker(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f"{self.name} walks on land.")


class Swimmer(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f"{self.name} swims in water.")


class Frog(Swimmer, Walker):

    def __init__(self, name):
        Walker.__init__(self, name)
        Swimmer.__init__(self, name)


frog = Frog("Freddy")
print(Frog.__mro__)
frog.move()
