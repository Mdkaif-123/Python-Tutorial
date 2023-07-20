
# ? Class Alternative is a method to use constructor in different format input


class Employee:

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def hifenFormat(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])
    
    @classmethod
    def underscoreFormat(cls, string):
        return cls(string.split('_')[0], string.split('_')[1])

e1 = Employee("Kaif", 1200)

print(e1.name)
print(e1.salary)
stringInput = "suraj-1200"

e2 = Employee.hifenFormat(stringInput)

print(e2.name)
print(e2.salary)

stringInput = "Wasim_1200111"

e2 = Employee.underscoreFormat(stringInput)

print(e2.name)
print(e2.salary)