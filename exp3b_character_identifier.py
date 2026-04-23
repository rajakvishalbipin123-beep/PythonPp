def character_identifier():
    ch = input("Enter character: ")

    if ch.isdigit():
        print("DIGIT")
    elif ch.islower():
        print("LOWERCASE")
    elif ch.isupper():
        print("UPPERCASE")
    else:
        print("SPECIAL CHARACTER")

character_identifier()
