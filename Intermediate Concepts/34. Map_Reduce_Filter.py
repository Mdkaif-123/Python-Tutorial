
#? Map , Reduce and filter is a higher order function that take function as argument 

#* MAP
def double(a):
    return a*2

l = [12, 34,56,78,89,99]

newlist = list(map(double, l))
print(newlist)

# * FILTER 

specialList = list(filter(lambda a: a>50, l))
print(specialList)


# * REDUCE
from functools import reduce

reduceList = reduce(lambda a,b : a+b, l)
print(reduceList)