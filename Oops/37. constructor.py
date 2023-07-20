    #? Constructor is a default function that runs everytime the object is created
    

class Person():
    #* init is used to create the constructor. And it return none by default 
    def __init__(self, name , occ):
        self.name = name
        self.occupation = occ
        
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Kaif", "Developer")
a.info()