    #? Finally method is used is execute a block of code in all condition 

def finallyExample() :
    try:
        index = int(input("Enter an index : "))
        arr = [12,56,89,34]
        print(arr[index])
        return 1
    except IndexError:
        print("Index error")
        return 0
    except ValueError :
        print("Invalid input")
        return 0
        
    finally:
        #* finally is usually used for clean ups and to close file after the operation or to disconnect any connection
        print("You function has been executed ")


x = finallyExample()

print(x)