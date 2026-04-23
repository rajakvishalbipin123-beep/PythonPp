def extract_words():
    filename = input("Enter filename: ")
    length = int(input("Enter word length: "))

    try:
        with open(filename, "r") as file:
            words = file.read().split()

        result = [w.strip(".,!?") for w in words if len(w.strip(".,!?")) == length]

        print("Words:", result if result else "None found")

    except FileNotFoundError:
        print("File not found!")

extract_words()
