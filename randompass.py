import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password (default is 12): ") or 12)
        if length <= 0:
            print("Length must be a positive integer.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
