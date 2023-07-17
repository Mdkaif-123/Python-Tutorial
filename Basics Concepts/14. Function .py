#? Functions are the block of code that can be written once and used multiple times
def sum(a,b):
    print("Sum of two number is : ", a+b)

a=12
b=13

sum(a,b)

# ? There are four type of function arguments in python
#* 1. Default 
#* 2. Keyword
#* 3. Required
#* 4. Variable length argument

#? Example of default argument
def sum(a=89,b=9):
    print("Sum of two number is : ", a+b)

#? Example of keyword argument
def printName(fname, lname):
    print(fname, lname)
    
printName(lname="KAif ", fname="Ansari")

#? Example of required argument
def sum(a,b):
    print("Sum of two number is : ", a+b)
sum(12,58)


#? Example of required argument
def average(*number):
    sum=0
    for i in number:
        sum = sum + 1
    return sum/len(number)

average(12,44,85,90)
