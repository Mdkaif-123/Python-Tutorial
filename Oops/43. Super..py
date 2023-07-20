
#? Super keyword is used to call the methods of the immediate parent class

class Employee:
    def __init__(self, name , id) -> None:
        self.name = name
        self.id = id
        
    def parent_method(self):
        print("I am the parent method")


class Programmer(Employee):
    def __init__(self, name, id, lang) -> None:
        super().__init__(name, id)
        self.lang = lang
        
    def child_method(self):
        print("I am a child method")
        super().parent_method()
        
kaif = Programmer("kaif", 12, "python")
kaif.child_method()
kaif.parent_method()
