    #? Class is a blue print, that has its own values and methods 

class Student:
    name = "Kaif"
    age = 18
    qualification = "Diploma"
    def info(self):
        print(f"{self.name} is {self.age} years old and study {self.qualification}")

#* Objects 
s1 = Student()
s2 = Student()

s2.name = "Wasim"

#*  Methods
s1.info()
s2.info()