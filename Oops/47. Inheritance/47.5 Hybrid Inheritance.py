
#? Hybrid Inheritance - The type of inheritance that impliment more than one type of inheritance 

#*Hybrid inheritance in Python refers to a scenario where a class is derived from multiple classes using both single and multiple inheritance. It is a combination of both types of inheritance.

class A:
    def method_a(self):
        print("This is method A")

class B:
    def method_b(self):
        print("This is method B")

class C(A, B):
    def method_c(self):
        print("This is method C")
class D(C):
    def method_d(self):
        print("This is method C")

obj = D()
obj.method_a()  # Output: This is method A
obj.method_b()  # Output: This is method B
obj.method_c()  # Output: This is method C
obj.method_d()  # Output: This is method C