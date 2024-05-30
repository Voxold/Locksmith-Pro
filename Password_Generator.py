import random
import string

def generate_password(length=True, uppercase=True, lowercase=True, digits=True, symbols=False):
    """
    Generate a random password.

    Parameters:
    - length (int): Length of the password (default: 12)
    - uppercase (bool): Include uppercase letters (default: True)
    - lowercase (bool): Include lowercase letters (default: True)
    - digits (bool): Include digits (default: True)
    - symbols (bool): Include symbols (default: False)

    Returns:
    - password (str): Randomly generated password
    """
    length = int(input('Please choose length of your password : '))
    # Define character sets based on parameters
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage:
    # Generate a password with default settings
    default_password = generate_password()
    print("Default password:", default_password)

    # Generate a password with specific criteria
    custom_password = generate_password(length=16, symbols=True)
    print("Custom password:", custom_password)