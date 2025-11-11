from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def display_available_inventory():
    for book in library_books:
        if book['available'] == True:
            print("---------------------")
            for key, value in book.items():
                print(f"{key}:{value}")
    print("-------------------")



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search():
    list_of_books = []
    genre_list = []
    choice = input("Do you want to search by author or genre? A or G: ")
    if choice.lower() == "a":
        author_search = input("Name of author: ")
        for book in library_books:
            if author_search.lower() == book['author'].lower():
                title = book['title']
                list_of_books.append(title)
        if len(list_of_books) == 0:
            print("There is no book under that name")
            
        print(list_of_books)
        return(list_of_books)
    
    if choice.lower() == "g":
        genre_search = input("Pick a genre: ")
        for book in library_books:
            if genre_search.lower() == book['genre'].lower():
                title = book['title']
                genre_list.append(title)
        if len(genre_list) == 0:
            print("There is no book under that genre")

        print(genre_list)
        return(genre_list)


        

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout():
    id_search = input("What is the ID of the book you are looking for? ")

    for book in library_books:
        if id_search == book['id']:
            if book["available"] == True:
                book["available"] = False
                book["due_date"] = datetime.now() + timedelta(weeks=2)
                book["checkouts"] += 1
            elif book["available"] == False:
                print(f"The book is already checked out")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book():
    id_search = input("What is the ID of the book you are looking for? ")

    for book in library_books:
        if id_search == book['id']:    
            book['available'] = True
            book['due_date'] = None

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def overdue_books():
    list_of_books = []
    for book in library_books:
        if book["due_date"] != None:
            if str(book["due_date"]) <= str(datetime.now()) and book['available'] == False:
                list_of_books.append(book["title"])
    print(list_of_books)


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

def display_menu():
  print("\n **Texas Library**")  
  print("1. View All Books ") 
  print("2. View All Available Books ")     
  print("3. Search by Author or Genre")  
  print("4. Checkout Book")
  print("5. Return Book")
  print("6. All Overdue Books")     
  print("7. Exit\n")  
        

  #used to capture and process user selections
def user_selection():
    in_use = True
    user_choice = int(input("Enter a number between 1-7: "))  
    book = library(library_books)
    if user_choice == 1:  
        book.view_all()
    elif user_choice == 2:  
        book.display_available_inventory()
    elif user_choice == 3:
        book.search()
    elif user_choice == 4:
        book.checkout()
    elif user_choice == 5:
        book.return_book()
    elif user_choice == 6:
        book.overdue_books()    
    elif user_choice == 7:  
        print("Thank you for using the program!")             
        in_use = False  
        print("program ends.") 
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")
    return in_use


class library:
    def __init__(self, library):
        self.library = library
    
    def search(self):
        list_of_books = []
        genre_list = []
        choice = input("Do you want to search by author or genre? A or G: ")
        if choice.lower() == "a":
            author_search = input("Name of author: ")
            for book in self.library:
                if author_search.lower() == book['author'].lower():
                    title = book['title']
                    list_of_books.append(title)
            if len(list_of_books) == 0:
                print("There is no book under that name")
                
            print(list_of_books)
            return(list_of_books)
        
        if choice.lower() == "g":
            genre_search = input("Pick a genre: ")
            for book in self.library:
                if genre_search.lower() == book['genre'].lower():
                    title = book['title']
                    genre_list.append(title)
            if len(genre_list) == 0:
                print("There is no book under that genre")

            print(genre_list)
            return(genre_list)

    def view_all(self):
        for book in self.library:
            print("---------------------")
            for key, value in book.items():
                print(f"{key}:{value}")
    print("-------------------")

    def display_available_inventory(self):
        for book in self.library:
            if book['available'] == True:
                print("---------------------")
                for key, value in book.items():
                    print(f"{key}:{value}")
        print("-------------------")


    def checkout(self):
        id_search = input("What is the ID of the book you are looking for? ")

        for book in self.library:
            if id_search == book['id']:
                if book["available"] == True:
                    book["available"] = False
                    book["due_date"] = datetime.now() + timedelta(weeks=2)
                    book["checkouts"] += 1
                elif book["available"] == False:
                    print(f"The book is already checked out")
    
    def return_book(self):
        id_search = input("What is the ID of the book you are looking for? ")

        for book in self.library:
            if id_search == book['id']:    
                book['available'] = True
                book['due_date'] = None
    
    def overdue_books(self):
        list_of_books = []
        for book in self.library:
            if book["due_date"] != None:
                if str(book["due_date"]) <= str(datetime.now()) and book['available'] == False:
                    list_of_books.append(book["title"])
        print(list_of_books)




# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    in_use = True
    while in_use == True:
        display_menu()
        in_use = user_selection()
    '''
    display_available_inventory()
    print(search())
    checkout()
    display_available_inventory()
    checkout()
    return_book()
    display_available_inventory()
    overdue_books()
    '''