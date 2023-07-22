
# ? Single Inheritance is the process of deriving the property of single parent class to child class

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal making sound")
    
    def __str__(self) -> str:
        return f"This is a {self.name}"

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print(f"{self.name}: bhaw bhaw bhaw .... 🐶")
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print(f"{self.name} : meaw meaw .... 🐱")
    
    def jump(self):
        print(f"{self.name} : is jumping .... 😾")
    
    def run(self):
        print(f"{self.name} : is running .... 😿")
    
dog = Dog("Doggy")
print(dog)

cat = Cat("geera")
print(cat)

cat.jump()
cat.make_sound()
cat.run()