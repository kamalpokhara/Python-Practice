class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
   
    def introduce(self):
        print(f"Hello, My name is {self.name} and I'm {self.age} years old.")


class Student(Person):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
    
    def introduce(self):
        super().introduce()
        print(f"I am a {self.gender} student")

    

p1=Person("Roz", 22)
p1.introduce()

s1=Student("ZORO", 22, "Male")
s1.introduce()

print(s1.introduce())