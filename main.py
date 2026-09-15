from library import Library

library_start = Library()

def wait_for_continue():
    input(f"\n{8*" "}Press Enter to return to menu.")

while True:
    print("""
f"{8*" "}------------------------------
f"{8*" "}****** library management *****
f"{8*" "}------------------------------
    
f"{8*" "}1. Add Book
f"{8*" "}2. Add Member
f"{8*" "}3. Show Books
f"{8*" "}4. Show Members
f"{8*" "}5. Search Book
f"{8*" "}99. Exit
""")
    while True:
        user_input = input(f"{8*" "}Select a number : ")
	    
        if user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print(f"{8*" "}Please enter a number.")

    if user_input == 1: #Add Book
        print(f"\n{8*" "}Please enter book informations.")

        while True:
            title = input(f"{8*" "}title : ")
            author = input(f"{8*" "}author : ")
            year = input(f"{8*" "}year : ")
        
            approval = input(f"{8*" "}{title} by {author} in ({year}). \
do you want to save this? (y/n)").lower()
            if approval in ["y", "yes"]:
                library_start.add_book(title, author, year)
                print(f"{8*" "}Book added successfully.")
                wait_for_continue()

                break

            elif approval in ["n", "no"]:
                print(f"{8*" "}Enter boobk information again. ")

            else:
                print(f"{8*" "}Please enter y/yes or n/no.")

    elif user_input == 2: #Add Member
        print(f"\n{8*" "}Please enter member informations.")
        name = input(f"{8*" "}your name : ")
        while True:
            phone_number = input(f"{8*" "}phone number(+989123456789) : ")
            if phone_number.startswith("+989") \
                and len(phone_number) == 13 \
                and phone_number[4:].isdigit():
                break
            else:
                print(f"{8*" "}please enter your number in (+989123456789) format. ")

        while True:
            password1 = input(f"{8*" "}password : ")
            password2 = input(f"{8*" "}re-enter password : ")
            if password1 == password2:
                password = password1
                break
            else:
                print(f"{8*" "}password does not match. try again.")
                
        library_start.add_member(name, password, phone_number)
        print(f"\n\tmember {name}, {phone_number} created successfully.")

    elif user_input == 3: #Show Books
        print(f"\n{8*" "}The list of library's Books : \n")
        books = library_start.get_data("books")

        if not books:
            print(f"{8*" "}no book found.")
        else:
            for option_num, book in enumerate(books, start=1):
                print(f"{8*" "}{"-" * 15}"
                      f"{6*" "}{option_num}.")

                print(
                    f"{8*" "}Title : {book["title"]}\n"
                    f"{8*" "}Aothur : {book["author"]}\n"
                    f"{8*" "}Year : {book["year"]}\n"
                    f"{8*" "}Is Borrowed : {"Yes" if book["is_borrowed"] else "No"}"
                )
                print(f"{8*" "}{"-" * 15}")

    elif user_input == 4: #Show Members
        print(f"\n{8*" "}The list of Members : \n")
        members = library_start.get_data("members")

        if not members:
            print(f"{8*" "}no member found.")
        else:
            for option_num, member in enumerate(members, start=1):
                print(f"{8*" "}{"-" * 15}"
                      f"{6*" "}{option_num}.")

                print(
                    f"{8*" "}Member ID : {member["member_id"]}\n"
                    f"{8*" "}Name : {member["name"]}\n"
                    f"{8*" "}Phone Number : {member["phone_number"]}\n"
                    f"{8*" "}Membership Date : {member["membership_date"]}\n"
                )
                print(f"{8*" "}{"-" * 15}")


    elif user_input == 5: #Search Book
        pass

    elif user_input == 99: #Exit
        break

