
from PyPDF2 import PdfWriter

file1 = open('./pdf/pdf1.pdf', 'rb')
file2 = open('./pdf//pdf1.pdf', 'rb')

merger = PdfWriter()


i=1
for pdf in [file1, file2]:
    
    startPosition = int(input(f"Enter the start position of file {i} : "))
    endPosition = int(input(f"Enter the end position of file {i} : "))
    
    merger.append(pdf, pages=(startPosition, endPosition))
    i =i+1 
    
merger.write("./pdf/merged-pdf.pdf")
merger.close()

print("Done 🎉")