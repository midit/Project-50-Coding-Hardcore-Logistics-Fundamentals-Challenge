import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return bool(re.match(pattern, email))

if __name__ == "__main__":
    emails = ["example@gmail.com", "example1234", "example1234@test."]
    for e in emails:
        print(f"{e}: {is_valid_email(e)}")

