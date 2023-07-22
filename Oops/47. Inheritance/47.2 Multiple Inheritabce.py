
#? Inheritance is said to multiple when a single class  iss  inherited from multiple class


class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
            print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance) -> None:
        self.dance = dance

    def show(self):
        print(f"Dance is {self.dance}")

    
class Dancer_employee(Employee, Dancer):
    def __init__(self, name, dance) -> None:
        self.name = name
        self.dance = dance


rohan = Dancer_employee("rohan", "break-dance")

rohan.show()

#* MRO stands for "Method Render Order" - It return all the order related to that class in their rendering order 
print(Dancer_employee.mro())