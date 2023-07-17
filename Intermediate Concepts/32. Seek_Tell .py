
#? seek() function is used to change the position of the File 
#? Handle to a given specific position

#? Tell is used to know the current position of the seek value 

f = open("txt.txt",'r')

f.seek(4)

print(f.tell())

text = f.readline()

print(text)