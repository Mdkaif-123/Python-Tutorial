#? List is nothing but the array that can have different types data

a = [23, 89, 4, "Kaif", True]
print(a)

#* Iterate a list
for i in a:
    print(i)

#* To check whether the item is  present in list
if 2 in a :
    print("Yes")
else:
    print("No")

#* Methods of printing loop

print(a[:])
print(a[1:-1])
print(a[:3])
print(a[-9:-5])

#* List comprehension is the technique of creating a list at the run time
#* Example -1 
array = [i+1 for i in range(10)]
print(array)

#* Example -2 : Store all the even number from 1 to 100
array = [i for i in range(100) if i%2==0 ]
print(array)