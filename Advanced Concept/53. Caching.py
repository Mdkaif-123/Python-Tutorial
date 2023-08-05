
#? Caching is the method through which we can store the computed data to be used in future and save the computation

from functools import lru_cache
import time 

@lru_cache(maxsize=None)

def myFun(i):
    time.sleep(2)
    return i*5
    
print(myFun(12))
print("Printed the result with 12")
print(myFun(2))
print("Printed the result with 2")
print(myFun(9))
print("Printed the result with 9")

#? If we print the call the method with same parameter it does not take time to execute as result is stored in the cache
print(myFun(12))
print("Printed the result with 12")
print(myFun(2))
print("Printed the result with 2")
print(myFun(9))
print("Printed the result with 9")

#* It will take time as it is not stored in the cache
print(myFun(78))
print("It took time")


"""
#* Usage 
1. Can be used where function is costly on the prospective of computation
2. When performance is considered more than memory

eg - Used in large data extraction from the data base, so that the computation can be preserved every time it request for the data

"""