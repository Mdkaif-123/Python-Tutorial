
#? If else in python is used to check conditions 

# a = int(input("Enter your age :"))

# if(a > 18):
#     print("You are eligible to drive")
# else:
#     print("You are not eligible to drive")
    
#? elif  in python is used to check conditions 

# price = int(input("Enter the price of the milk :"))

# if(price < 100):
#     print("You can consider to buy it!")
# elif(price < 150):
#     print("You should not consider to but  it !")
# elif(price < 200):
#     print("dont dare to buy it !")
# else :
#     print("No option dont buy !")

#? nested if-else  in python is used to check conditions 

num = int(input("Enter the value of num : "))

if (num < 0):
    print("Number is negative")
elif(num == 999):
    print("Number is special")
elif(num > 0) :
    if( num < 10):
        print("Number is less than 10 ")
    elif (num < 20):
        print("Number is less than 20 ")
    else:
        print("Number is greater than 20")
else:
    print("It is not  a number")