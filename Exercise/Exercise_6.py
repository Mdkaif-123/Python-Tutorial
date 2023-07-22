
#? Creating a function to change all the name of file in some specific extension

import os
# creating a  directory 

# os.mkdir("exercise-solution")

files = os.listdir('exercise-solution')

for i in range(1,len(files)):
    os.rename(f"exercise-solution/{files[i]}", f"exercise-solution/{i}.png")