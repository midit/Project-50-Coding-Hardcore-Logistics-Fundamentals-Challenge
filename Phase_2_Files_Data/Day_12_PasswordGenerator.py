import secrets
import string

def password_generator(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    if length < 6:
        return("Are you sure password this long is safe enough? Password length minimum 6 symbols!")

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range (length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    
    return password

if __name__ == "__main__":
    print(password_generator(10))
    print(password_generator(5))
    print(password_generator(16))