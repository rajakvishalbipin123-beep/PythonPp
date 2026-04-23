import re

def validate():
    phone = input("Phone: ")
    email = input("Email: ")

    if re.match(r"^\d{10}$", phone):
        print("Valid phone")
    else:
        print("Invalid phone")

    if re.match(r"^[\w]+@[\w]+\.[a-z]{2,}$", email):
        print("Valid email")
    else:
        print("Invalid email")

validate()
