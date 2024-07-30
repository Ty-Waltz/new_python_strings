def find_first_length(username):
    if len(username) < 2:
        print("Please enter a name longer than 2 characters")
    else:
        return (f"'{username}' is a valid first name")
def find_last_length(username):
    if len(username) < 2:
        print("Please enter a name longer than 2 characters")
    else:
        return (f"'{username}' is a valid last name")
       



while True:
    user_first = input("Please enter your first name: ")
    first_name = find_first_length(user_first)
    print(first_name)

    user_last = input("Please enter your last name: ")
    last_name = find_last_length(user_last)
    print(last_name)

    new_user = input(f"Is '{user_first} {user_last}' correct?(yes/no): ").lower
    if new_user != "no":
        break
