
import time

current = time.time()
today = time.ctime(current)
print("Time :" , today)

hour = int (today.split(" ")[3].split(":")[0])
print(hour)
if(hour > 0 or  hour < 5):
    print("It' to late to sleep , Good night !")
elif(hour >= 5 or  hour < 12): 
    print("Good Morning , Dear")
elif(hour >=12 or hour < 5): 
    print("Good Afternoon , Dear")
elif(hour >=5 or hour < 9): 
    print("Good Evening , Dear")
else:
    print("Good night  , Dear")