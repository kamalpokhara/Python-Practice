class Animal:
    count = 1

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Animal.count += 1

    def showAnimal(self):
        print(f"The animal name is {self.name} and is {self.color} color")

        print(f"Count is {self.count} ")

    def __eq__(self, other):
        return self.name == other.name


a1 = Animal("cat", "yellow")
a1.showAnimal()

a2 = Animal("dog", "white")
a2.showAnimal()

a3 = Animal("sheep", "balack")
a3.showAnimal()

print(a1 == a2)
