    #? For else is the special type of else statement that execute after the loop ends

for i in  range(5):
    print(i)
    if(i==4): #* If the loop is not completed else will not execute
        break
else:
    print("Hey loop ends ")
    
print("End of loop")