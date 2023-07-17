#? Match case in python is as as switch case

a = int(input("Enter a number :"))

match a: 
    case 0:
        print("Number is  zero")
    case 10:
        print("Number is  10")
    case 20:
        print("Number is  20")
    case 30:
        print("Number is  30")
    case _ if( a < 100):
        print("Number is less that 100")
    case _:
        print("Number is greater that 100")