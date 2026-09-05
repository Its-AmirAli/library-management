from library import *

library_start = Library()

test = 2

while test > 0:
    print("""
\t------------------------------
\t****** library managment *****
\t------------------------------
    
\t1. Add Book
\t2. Add Member
\t3. Show Books
\t4. Show Members
\t99. Exit
""")
    while True:
        user_input = input("\tSelect a number : ")
	    
        if user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print("\tPlease enter a number.")

    if user_input == 1:
        print("\tPlease enter book informations.")
        library_start.add_book()
    elif user_input == 2:
        print("\tPlease enter member informations.")
        library_start.add_member()
    test -= 1

    
