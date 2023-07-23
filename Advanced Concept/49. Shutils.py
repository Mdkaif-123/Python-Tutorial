
#* Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file. 
#* It comes under Python’s standard utility modules. 
#* This module helps in automating the process of copying and removal of files and directories.

#! Note : Shutil is a build-in module in python 

import shutil

source = "shutils/main.py"
destination ="shutils/main2.py"

shutil.copy(source, destination)
# shutil.copytree("pdf","copied_pdf")
# shutil.rmtree("copied_pdf")
print(shutil.disk_usage('D:'))