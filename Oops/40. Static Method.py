
#? Static methods are the methods that are associated with the class and can accessed with class as well as the instance
#* Static methods can be created using "@staticmethod" keyword

class Bike:
    def __init__(self, name) -> None:
        self.name = name
        
    @staticmethod
    def run():
        print("Running.........  🚴🏽‍♂️")

ktm = Bike("KTM")
ktm.run() #* we can use instance to call static  method  
Bike.run() #* we can also use Class name to call static method  