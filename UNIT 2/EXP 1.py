from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Bark!
print(cat.make_sound())  # Meow!