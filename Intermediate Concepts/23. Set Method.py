    #? Following are set methods
    
set1 = { "London", "Berlin", "Tokyo", "Las vegas","US" }
set2 = { "London", "Delhi", "US", "Kanpur"}
#? Union
# set3 = set2.union(set1) #* Concatenate  the set1 and set2 removing the duplicate value

# set1.update(set2) #* Update the set values with set2 value without duplicates 

# print(set1)
# print(set3)

#? Intersection
set4 = set1.intersection(set2)
set1.intersection_update(set2)

# print(set4)
set1.add("Kaif")
set1.remove("London")#* Throws an error if element is not present
set1.discard("London")#* Doesn't throws any error if element is not present
set1.pop() #* remove any element from the set
set4.clear() #* Removes all elements from the set.
copySet = set1.copy() #*Returns a shallow copy of the set.
print(set1.difference(set2))


print(set1)
print(set2)
# print(copySet)
