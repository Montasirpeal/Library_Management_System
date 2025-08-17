# step 1 : Create krbo Library_ class

class Library:

    book_list = []

    @classmethod
    def entry_book(cls, book):

        cls.book_list.append(book)


# lib1 = Library()
# lib2 = Library()
# lib3 = Library()
# lib4 = Library()
# lib5 = Library()
# lib6 = Library()
# lib7 = Library()
# lib8 = Library()
# lib9 = Library()

# lib1.entry_book("The Great Mhp")

# lib2.entry_book("The Great Mhp1")

# lib3.entry_book("The Great Mhp2")

# lib4.entry_book("The Great Mhp3")

# lib5.entry_book("The Great Mhp4")

# lib6.entry_book("The Great Mhp5")

# lib7.entry_book("The Great Mhp6")

# lib8.entry_book("The Great Mhp7")

# lib9.entry_book("The Great Mhp8")

# print(lib1.book_list)
# print(lib2.book_list)
# print(lib3.book_list)
# print(lib4.book_list)               
# print(lib5.book_list)
# print(lib6.book_list)
# print(lib7.book_list)
# print(lib8.book_list)
# print(lib9.book_list)

# print(Library.book_list)  # sob gula ke shate dekhabe 


# Step 2: Book class
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self._book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

        Library.entry_book(self)  # auto add to library

    # borrow_book method
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is currently not available.")

    # return_book method
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"Thank you for returning '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    # view_book_info method
    def view_book_info(self):
        print(f"{self._book_id} - {self.title} by {self.author} | {'Available' if self.availability else 'Not Available'}")




# Step 3: Manually create Book objects 

book1 = Book(1, "The Great MHP"  , "Author 1")
book2 = Book(2, "The Great MHP1" , "Author 2")
book3 = Book(3, "The Great MHP2" , "Author 3")

# #check all books in the library

# for book in Library.book_list:
#     print(f"Book ID: {book._book_id}, Title: {book.title}, Author: {book.author}, Available: {book.availability}")



# Step 4: menu system

# Step 1: Library class
class Library:
    book_list = []

    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)


# Step 2: Book class
class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True
        Library.add_book(self)

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}'")
        else:
            print(f"'{self.title}' was not borrowed.")

    def info(self):
        status = "Available" if self.available else "Not Available"
        print(f"{self.id} - {self.title} by {self.author} | {status}")


# Step 3: Create books
Book(1, "The Great MHP", "Author 1")
Book(2, "The Great MHP1", "Author 2")
Book(3, "The Great MHP2", "Author 3")


# Step 4: Menu
def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add a New Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            # sob book dekhabe
            for book in Library.book_list:
                book.view_book_info()

        elif choice in ['2', '3']:
            # borrow or return
            book_id = input("Enter Book ID: ")
            if not book_id.isdigit():
                print("Enter a valid number!")
                continue
            book_id = int(book_id)
            
            # Book khujbe 
            book = None
            for b in Library.book_list:
                if b._book_id == book_id:
                    book = b
                    break

            if not book:
                print("Book not found!")
            else:
                if choice == '2':
                    book.borrow_book()
                else:
                    book.return_book()

        elif choice == '4':
            # new add book korbe
            new_id = input("Enter new Book ID: ")
            if not new_id.isdigit():
                print("Enter a valid number!")
                continue
            new_id = int(new_id)
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            Book(new_id, title, author)
            print(f"Book '{title}' added successfully!")

        elif choice == '5':
            print("Exiting library. Bye!")
            break

        else:
            print("Invalid choice! Enter 1-5.")


# Run menu
menu()
