from library import *

library_start = Library()

test = 2

while test > 0:
    print("""
    ------------------------------
    ***** welcome to library *****
    ------------------------------
    
    1. Add Book
    2. Add Member
    3. Show Books
    4. Show Members
    99. Exit
    """)
    while True:
        user_input = input("Select a number : ")
	    
        if user_input.isdigit():
	        user_input = int(user_input)
	    else:
            print("Please enter a number.")

    if user_input == 


    test -= 1

    
