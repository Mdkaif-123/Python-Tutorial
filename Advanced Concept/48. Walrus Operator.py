
# ? Walrus operator is the special type of operator that allows assignment inside the expression

# * The walrus operator, also known as the assignment expression operator,
# * is a feature introduced in Python 3.8. It allows you to assign values to
# * variables within an expression. The operator is represented by :=

# *ex - print( a:= False)

print(a := True)

# * This is the a normal python program
# foods = []

# while(True):
#     food = input("Enter your favorite food: ")
#     foods.append(food)

#     if(food == 'quit'):
#         break


# * This can be done in 2 lines using walrus operator
foods = []


while (food := input("Enter your favorite food :")) != 'quit':
    foods.append(food)


print(foods)
