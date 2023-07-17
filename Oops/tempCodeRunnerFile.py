    #? Inheritance is the  process of deriving the property of parent class into child class


class Employee():
    def __init__(self, name , id) -> None:
        self.id = id  
        self.name = name
        
    def showDetails(self):
        print(f"Id: {self.id}\nName : {self.name}\n")
        
class Programmer(Employee):
    def showDetails(self):
        print(f"He is {self.name} and know  pytjon")


e1 = Employee("Shubham", 90)
e1.showDetails()

p = Programmer("Kaif", "21" )
p.showDetails()