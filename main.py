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
            
        return list_of_books
    
    if choice.lower() == "g":
        genre_search = input("Pick a genre: ")
        for book in library_books:
            if genre_search.lower() == book['genre'].lower():
                title = book['title']
                genre_list.append(title)
        if len(genre_list) == 0:
            print("There is no book under that genre")

        return genre_list


        

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
            if book["available"] == False:
                print(f"The book is already checked out")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    display_available_inventory()
    print(search())
    checkout()
    display_available_inventory()
    checkout()