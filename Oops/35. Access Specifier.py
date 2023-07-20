
#? There is nothing called private , public and protected in python

#? Python doesn't provide any access specifier rather we can use Name mangling  

#? Name mangling is the process where we make a data member not be accesed directly with the object 
#? But can be accessed indirectly using class name , (see the code how?)


# __(Double underscore ) is usually used for private data sets  
class Employee:
    def __init__(self, name) -> None:
        self.__name = name


obj = Employee("Kaif")

#print(obj.__name) #* We cannot accessed data member directly 
print(obj._Employee__name) #*  But We can accessed data member indirectly

#! Note : Usually we use __ for access specifier but _ (single under score ) can be used for private convention as well