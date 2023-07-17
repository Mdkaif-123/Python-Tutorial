    #? Exercise 3 - Create a string encoder and decoder
    
import random

def enCoder(string):
        string = string.strip()
        stringArray = string.split(" ")

        for i in range(len(stringArray)):
            
            if len(stringArray[i]) < 3:
                stringArray[i] =  stringArray[i][::-1]
            else:
                randomCharacter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                
                firstCharacter = stringArray[i][0]
                stringArray[i] = stringArray[i][1:]+firstCharacter
                
                for index in range(3):
                    stringArray[i] = random.choice(randomCharacter)+stringArray[i]+random.choice(randomCharacter)
                    
        joined_string = ' '.join(stringArray)
        
        return joined_string

def deCoder(string):
    string = string.strip()
    stringArray = string.split(" ")
    
    for i in range(len(stringArray)):
        
        if len(stringArray[i] ) <= 3:
            stringArray[i] = stringArray[i][::-1]
        else:
            stringArray[i] = stringArray[i][3:-3]
            lastCharacter = stringArray[i][-1]
            stringArray[i] = lastCharacter+stringArray[i][:-1]

    joined_string = ' '.join(stringArray)
    return joined_string



inputString = input("Enter your secret message : ")
encryptedString = enCoder(inputString)
print(f"Encrypted text : {encryptedString}\n")

decryptedString = deCoder(encryptedString)
print(f"Decrypted text : {decryptedString}")
