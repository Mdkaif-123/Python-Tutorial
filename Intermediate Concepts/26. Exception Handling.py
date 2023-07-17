    #? just like in other programming languages we can also handle error in python
    

#* Example of value error 

# try:
#     age = int(input("Enter your age : "))
#     if age >= 18:
#         print("You can drive")
#     else:
#         print("You cannot drive")
# except ValueError :
#     print("Enter a valid input")
    
# print("Thankyou !")


#* Example of index error 

try:
    index = int(input("Enter the index : "))

    arr = [90,45,67]
    print(arr[index])
    
except IndexError:
    print("Index Error")
except ValueError :
    print("Enter a valid input")