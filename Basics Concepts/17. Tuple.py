#? tuple is also an array that can have different types of  data. The only  difference between list and tuple 
# is list are mutable and tuple are immutable.

tup = ( 12, 878, "Kaif", "Ansari", True, False)

print(tup[0:2])

for i in tup :
    print(i)
    
#* Methods of printing loop
print(tup[:])
print(tup[1:-1])
print(tup[:3])
print(tup[-9:-5]) # this does not exits 
