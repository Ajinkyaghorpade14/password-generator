import random
import string

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get the desired password length from the user
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
