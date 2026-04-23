import re

def check_password():
    password = input("Enter password: ")
    if (len(password)>=8 and re.search(r"[A-Z]",password)
        and re.search(r"[a-z]",password)
        and re.search(r"[0-9]",password)
        and re.search(r"[!@#$%^&*]",password)):
        print("Strong password")
    else:
        print("Weak password")

check_password()
