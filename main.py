import hashlib
import secrets
import string
from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def generate_password(password_size):
    """Generates a random password and returns its SHA-256 hash."""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(password_size))
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    return password, password_hash

def read_password_and_hash():
    """Reads a password from the user and returns its SHA-256 hash."""

    password = input("Enter your password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    return password_hash

def main():

    clear()
    password_size = int(input("How many characters would you like your password to be? 12 is the minimum suggested: "))
    password, password_hash = generate_password(password_size)
    print("Generated password:", password)
    print("SHA-256 hash:", password_hash)

    entered_hash = read_password_and_hash()
    print("Entered password hash:", entered_hash)

    if entered_hash == password_hash:
        print("Password matches!")
    else:
        print("Password does not match.")



main()