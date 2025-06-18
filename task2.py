#This program generates a strong random password using letters, numbers, and symbols. 
import random  
import string  

# define the character sets to be used in the password
lowercase_letters = string.ascii_lowercase      # a to z
uppercase_letters = string.ascii_uppercase      # A to Z
digits = string.digits                          # 0 to 9
special_characters = string.punctuation         # Symbols like !@#$%^&*()

# combine all characters
password_characters = lowercase_letters + uppercase_letters + digits + special_characters

print("************************************")
print("Password Generator")
print("************************************")

while True:
    password_length_input = input("\nEnter the desired password length (e.g., 8, 12, 16): ")

    if password_length_input.isdigit():
        password_length = int(password_length_input)
    else:
        print("Please enter a valid number. Try again.")
        continue 

    # Initialize an empty string to store the password
    generated_password = ""

    # Generate password using a loop
    for i in range(password_length):
        random_char = random.choice(password_characters)
        generated_password += random_char

    # Display the final generated password
    print("\n✅ Your generated password is:", generated_password)

    choice = input("\nDo you want to generate another password? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for using the password generator. Stay safe!")
        break
