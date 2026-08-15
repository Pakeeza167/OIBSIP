# Project: Random Password generator
# Internship: Python Programming
# Developer:  Pakeeza fatima

import random
import string

print("======================================")
print("      Random Password Generator       ")
print("======================================")

while True:
    try:
        #Ask for password length
        password_len=int(input("\nEnter the length of the password (minimum 8 characters): "))

        if password_len < 8:
            print("Password must contain at least 8 characters.")
            continue
        print("\nchoose character types (yes/no):")

        upper = input("Include Uppercase letters? ").lower()
        lower = input("Include Lowercase letters? ").lower()
        numbers = input("Include numbers? ").lower()
        symbols = input("Include symbols? ").lower()

        char_pool = ""
        selected = 0

        if upper == "yes":
            char_pool += string.ascii_uppercase
            selected += 1

        if lower == "yes":
            char_pool += string.ascii_lowercase
            selected += 1

        if numbers == "yes":
            char_pool += string.digits
            selected += 1

        if symbols == "yes":
            char_pool += string.punctuation
            selected += 1

        if selected < 2:
            print("\nPlease select at least two character types.")
            continue

        # Generate password
        generated_password= ""

        for i in range(password_len):
            generated_password += random.choice(char_pool)

        print("\n=========================================")
        print("Password generated successfully!")
        print("Generated Password:", generated_password)
        print("password length   :", password_len)
        print("===========================================")
        
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
        continue
        choice = input("\nDo you want to generate another password? (yes/no): ").lower()

    choice = input("\nDo you want to generate another password? (yes/no): ").lower()

    if choice != "yes":
            print("Thank you for using the Random Password Generator!")
            print("have a nice day!")
            break   
    

        
        