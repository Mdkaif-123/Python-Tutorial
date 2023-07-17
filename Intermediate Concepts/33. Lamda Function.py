
# ? Lambda function are the one line function that doesn't has any name

# Note : Lambda function can be passed as an argument of another function

# * Normal function
def square(num):
    return num * num


# * Lambda function
def cube(x): return x*x*x

# print(cube(2))
# print(square(12))


# * Function that take function as argument

def avg(sum, a, b):
    return sum(a, b)/2

result = avg(lambda a, b: a+b, 5, 10)

print(result)
