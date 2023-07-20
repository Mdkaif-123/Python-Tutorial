
#? CLass method is the way define manipulate the class variable 

class Company:
    companyName = "K.K Coders"
    def showCompanyDetails(self):
        print(f"Company name is {self.companyName}")
    
    @classmethod 
    def changeCompany(cls, newCompanyName):
        cls.companyName = newCompanyName

c = Company()
c.changeCompany("Tesla")
c.showCompanyDetails()

print(Company.companyName) # if I remove the decorator then company will be default to class variable