
# ? Dunder or magic methods in Python are predefined methods that allow you to customize the behavior of objects
# ? Dunder methods that can directly been called by the object of that class

# * We can also make our dunder methods as well using __methodname __

# * There are few dunder in build methods such as __init__, __str__ , __call__ , __defr__


class Employee:

    def __init__(self, name) -> None:
        self.name = name

    def __len__(self): #* This is my created dunder methods
        i = 0
        for ch in self.name:
            i = i+1
        return i
    
    # def __str__(self): #* str methods are used to 
    #     return (f'Employee({self.name})')

    def __repr__(self): #* __repr__ dunder method is used to define a string representation of an object
        return ("This is  the method function")

    #! Note : If the __str__ is not defined it automatically call the repr 

e = Employee("kaif")
print(len(e))
print(e)