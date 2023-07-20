# ? Creating a  Library management system
import datetime

x = datetime.datetime.now()


class Library:

    # data members
    books = []
    noOfBooks = 0
    issueBooks = []


    def addBook(self):
        try:
            book_name = input("\nEnter book name: ")
            book_id = input("Enter book ID: ")
            copy = int(input("Enter the number of copies: "))

            if book_name.strip() == "" or book_id.strip() == "":
                raise ValueError(
                    "Invalid input. Book name and book ID cannot be empty.")
        except ValueError:
            print("Invalid input.")
            return

        new_book = {
            "bookName": book_name.lower(),
            "bookId": book_id,
            "noOfCopy": copy
        }

        self.books.append(new_book)
        self.noOfBooks += copy

    print("Book added successfully!\n")

    def getBook(self):
        bookName = input("\n\nEnter the name of the book :").lower()
        
        if(len(self.books) <= 0):
            print("Sorry, No books Available 😕")
            
        for book in self.books:
            if book['bookName'] == bookName and book['noOfCopy'] > 0:
                try:
                    days = int(input("Enter no of days : "))
                    issueDate = f"{x.strftime('%d')}/{x.strftime('%b')}/{x.year}"
                    studentName = input("Enter the name  of the student :")
                    studentRollNo = input("Enter the roll no of student :")

                except ValueError:
                    print("Invalid input 😕")

                issueBook = {
                    'studentName': studentName,
                    'rollNo': studentRollNo,
                    'bookName': bookName,
                    'issueDate': issueDate,
                    'bookId': book['bookId'],
                    'noOfDays': days
                }
                self.issueBooks.append(issueBook)
                book['noOfCopy'] = book['noOfCopy']-1

                print("\nCongratulation 🎉,  Book issued ")
                break
            
        print("Sorry, Book is not available in library 😕")

    def showAvailableBooks(self):
        print("\n\nAvailable Books 📚📚\n")
        
        if(len(self.books) <= 0):
            print("Sorry, No books Available 😕")
            
        for book in self.books:
            if (book["noOfCopy"] != 0):
                print("Book Name : ", book["bookName"].capitalize())
        print("\n\n")

    def totalNumberOfBooks(self):
        print('\n\n')
        for book in self.books:
            print("Book Name : ", book["bookName"].capitalize())
            print("Book ID : ", book["bookId"])
            print("Number of copies : ", book["noOfCopy"])
    print('\n\n')
    
    
while (True):
    print("\n\n\n❄️❄️❄️❄️❄️❄️❄️❄️❄️\tWelcome to Code Library\t❄️❄️❄️❄️❄️❄️❄️❄️❄️\n\n\n")
    print("1. Add Books")
    print("2. Show Available Books")
    print("3. Get Books")
    print("4. Total books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")

    librarian = Library()

    match(choice):
        case 1:
            librarian.addBook()
        case 2:
            librarian.showAvailableBooks()
        case 3:
            librarian.getBook()
        case 4:
            librarian.totalNumberOfBooks()
        case 5:
            break
        case _:
            print("Enter a  valid choice 😕")

print("Thankyou")