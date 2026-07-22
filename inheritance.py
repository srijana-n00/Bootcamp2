class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def info(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"
    
    def info(self):
        return f"{self.name} is {self.color} and is {self.age} years old"


dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "orange")

print(dog.info())
print(dog.make_sound())
print()
print(cat.info())
print(cat.make_sound())
