import os

# * Creating a directory
# os.mkdir("demo")

# * Changing a directory
# print(os.getcwd())
# os.chdir("/")
# print(os.getcwd())

# *  Creating multiple directory
# for i in range(0,10):
#     os.mkdir(f"demo/folder {i+1}")

# * Renaming the directory
# for i in range(0, 10):
#     os.rename(f"demo/folder {i+1}", f"demo/Tutorial {i+1}")


# * Finding list of directory
# listFolder = os.listdir('demo')
# for folder in listFolder:
#     print(folder)


# * Finding list of directory inside the directory
# listFolder = os.listdir('demo')
# for folder in listFolder:
#     print(os.listdir(f"demo/{folder}"))
