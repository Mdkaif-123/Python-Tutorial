    #? Sets are as similar as list but doesn't have duplicate values in it.
    #? Set cannot be access using the index because they doesn't have any order

s = {12,9283,2873, "Kaif", True, False}

print(s)

#? A blank set can be created using set()
set2 = {} #* This is not a set but a dictionary
set1 = set()
print(type(set1))
print(type(set2))

#? We can access the set item using loop

for i in s:
    print(i) #* Doesn't have any order