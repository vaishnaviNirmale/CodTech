import random
import string


def generate_password(length, uppercase=True, numbers=True, symbols=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Customizing the symbols string based on our preferences
    excluded_symbols = "!@#$%^&*()_+=-`~,./<>?;:'\"\\|[]{}`"
    symbols_string = ''.join(symbol for symbol in string.punctuation if symbol not in excluded_symbols)
    characters += symbols_string

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    #Displays a welcome message.
    print("Welcome to the Password Generator!")

    try:
        #Take user input for the desired password length.
        length = int(input("Enter the desired password length (at least 7): "))

        #Validate that the password length is at least 7 characters.
        if length < 7:
            print("Password length must be at least 7 characters.")
            return

        #Asks the user whether to include uppercase letters, numbers, and symbols.
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, numbers, symbols)

        if password:
            print(f"\nYour generated password is: {password}")
        else:
            print("Invalid input. Please enter a valid password length.")

    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")


if __name__ == "__main__":
    main()
