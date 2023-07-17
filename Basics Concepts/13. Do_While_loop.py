#? Do while loop is  not  supported in python
i = int(input("Enter the value of i :"))

while(True):
    print(i)
    if(i<0):
        break
    else:
        i = int(input("Enter the value of i :"))

print("Done with the loop")
