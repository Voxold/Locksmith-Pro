import random
import string


def generate_password(length=0, uppercase=False, lowercase=False, digits=False, symbols=False):
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
    # Generate a password with specific criteria
    custom_password = generate_password(length=16, uppercase=True, lowercase=True, digits=True, symbols=True)
    print("Custom password:", custom_password)