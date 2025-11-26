#Exercise 8
# Validate user Input
# 1. username is no more than 12 characters
# 2. username must not contain any spaces
# 3. username must not contain any digits

username = input("Please enter your username: ")

if len(username) > 12:
    print("Sorry, username cannot be more than 12 characters.")

elif not username.find(" ") == -1:
    print("Sorry, username cannot have any spaces.")

elif not username.isalpha():
    print("Sorry, Username cannot have any numbers.")

else:
    print(f"Welcome {username}")
