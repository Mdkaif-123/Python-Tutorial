
# ? Creating a program for water drinking reminder



from plyer import notification #for getting notification on your PC
import time

forty_five_minutes = 60 *45
while True:
    
    
    def throwNotification():
        notification.notify(
                #title of the notification,
                title = "Drink Water",
                #the body of the notification
                message = "Its till 45 min you didn't have any sip 🥤",  
                timeout  = 60
            )
        time.sleep(forty_five_minutes)

    throwNotification()