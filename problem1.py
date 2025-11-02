

def palindrome_checker():
    clear = 0
    word = input("Enter word here to check if Palindrome: ")
    while len(word) == 0:
        print("try again")
        word = input("Enter word here to check if Palindrome: ")

    

    list_of_words = list(word)

    while clear == 0:
        for letter in list_of_words:
            if letter.isdigit():
                print("try again")
                word = input("Enter word here to check if Palindrome: ")
                list_of_words = list(word)
            else:
                clear = 1
        
    
    reversed_list = list_of_words[::-1]

    if reversed_list == list_of_words:
        print("The string is a palindrome")
    else:
        print("The string isn't a palindrome")

palindrome_checker()