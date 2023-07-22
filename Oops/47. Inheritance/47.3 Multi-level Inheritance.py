
#? Multi-level inheritance is the type of inheritance where a derived class id inherited by a class  

class Office:
    def __init__(self, office) -> None:
        self.office = office
    
    def show_details(self):
        print(f"Office is {self.office}")

class Branch(Office):
    def __init__(self,branch, office = "microsoft") -> None:
        super().__init__(office)
        self.branch = branch 
    
    def show_details(self):
        print(f"Branch is {self.branch}")
        Office.show_details(self)
    
class Employee(Branch):
    def __init__(self,name, branch) -> None:
        super().__init__(branch)
        self.name = name
    
    def show_details(self):
        print(f"Name is {self.name}")
        Branch.show_details(self)
    
E = Employee("Kaif", "CO")
E.show_details()