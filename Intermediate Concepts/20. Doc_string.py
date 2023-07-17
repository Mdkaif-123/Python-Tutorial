#? Doc String is a special types of comments that can be used to document a function

def sum(a,b):
    ''' Adds two number and return the sum, both the argument are required'''
    return a+b

c = sum(167,445)

print(c)
print(sum.__doc__)