class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says bark!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says Moo!"

dog = Dog("daina")
cat = Cat("sassie")
cow = Cow("pinky")

# print(dog.make_sound())
# print(cat.make_sound())
# print(cow.make_sound())

print(super(Dog, dog).make_sound())
print(super(Cat, cat).make_sound())
print(super(Cow, cow).make_sound())
