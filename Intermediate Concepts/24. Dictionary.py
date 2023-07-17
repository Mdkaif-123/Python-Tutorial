    #? Dictionary are nothing but the key value pairs like object
    
dic ={
    "name" : "Md Kaif Ansari",
    "roll": 12,
    "dev" : "web development",
    "state": "JH."
}

print(dic) #* To print the dictionary
print(dic["name"]) #* Throws an error if no name is present 
print(dic.get("name")) #* Doesn't throws any error if name is not present 
print(dic.keys()) #* To print only the keys 
print(dic.values()) #* To print only the values 
print(len(dic))  #* Length of dictionary
print(type(dic))



for keys, values in dic.items() :
    print(f"The key is {keys} and the value is {values}") #* To print only the key as well as values  
