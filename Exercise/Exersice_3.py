#? Creating a KBC game

#*Questions 
ques = ["Which is the first programming language", "Who is the prime minister of India", "National animal of India", "Capital of India","Which of the following was used in programming the first computers?","Full form of CPU" ]
ans = ["C", "Narendra modi", "Tiger", "Delhi", "Assembly Language", "Central processing unit"]

# options array 
language = ["C++", "Java", "Python","C"]
person = ["Alakh panday", "Narendra modi", "Susmita banerji", "Shreeram chandra"]
animal = ["Lion", "Dinosaurs","Tiger", "Peacock"]
state =["Lucknow", "Mumbai", "Delhi", "Srinagar"]
oldLanguage = ["Binary Language", "Assembly Language", "Equational language", "Computer Graphics language"]
cpu = ["Central processing unit","central process unit", "central productivity unit", "central prerequisite unit"]

#option

option = ["language", "person", "animal","state","oldLanguage", "cpu"]

name = input("Enter your name to start the game :")
price = 0
welcome = " Welcome to Kaun Banega Crorepati "
while(True):
    print(welcome.center(110, "-"), "\n\n")
        
    print("❄️❄️❄️❄️❄️❄️❄️❄️     First question on your computer screen     ❄️❄️❄️❄️❄️❄️❄️❄️❄️\n\n")
    
    index=0
    for i in ques:
        print("Question", index+1, ":", i)

        currentOption = eval(option[index]) 
        currentIndex =0
        for question in currentOption:
            print (currentIndex+1, ":", currentOption[currentIndex])
            currentIndex = currentIndex + 1
            
        answer = int(input("Enter your choice :"))
        print(currentOption[answer-1])
        
        if(currentOption[answer-1] == ans[index]):
            price = price + 10000
            index=index+1
            print("Your answer is correct : You won 10,000 💵\n")
        else:
            print("Wrong Answer\n ")
            break
    break

result = "  Result  "
print(result.center(20 , "✨"), "\n\n")

if( price == 0):
    print("Better luck next time, Dont be sad 😊" )
elif (price <20000):
    print("Good game , It can be even more better, Practice more 👍🏽")
    print("Your price is :" , price)
elif ( price < 50000):
    print("Excellent 🎉, you won", price)
else:
    print("You are incredible 🫡🫡🫡, You answer all the question")
    print("Congratulation 🎉🎉🎉🎉, You won ", price , "💵💵💵")

print("\n\n")