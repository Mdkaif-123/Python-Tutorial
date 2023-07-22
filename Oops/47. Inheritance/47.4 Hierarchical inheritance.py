
#? In Hierarchical inheritance, more than one sub-class inherits the property of a single base class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog("Buddy")
dog.speak()  # Output: Dog barks

cat = Cat("Whiskers")
cat.speak()  # Output: Cat meows
