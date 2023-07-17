'''
---------Types of typeCasting--------- 
        Type  casting is the process of converting one datatype into another
1. Implicit typeCasting - Implicit typecasting is  the  process where dataType is converted by the interpreter itself.
2. Explicit typeCasting - Explicit typecasting is the process of converting the data types of variable using some type casting functions such as -  int() , float(), tup(), etc

'''

#* Implicit typecasting 
a= 12.1
print(type(a))
b= 8
print(type(b))

#* c will be converted into float
c= a+b
print(c)
print(type(c))

#* Explicit typecasting 

str1 = "12"
str2 = "98"

print(int(str1) + int(str2))