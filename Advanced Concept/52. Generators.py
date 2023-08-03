
#? Generators are the function that doesn't return the value but a generator and value can be obtain in a fly 

def myGenerator ():
    for i in range(4000):
        yield i
        

gen = myGenerator()

print(gen) # gen is not a list it is a generator 
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
