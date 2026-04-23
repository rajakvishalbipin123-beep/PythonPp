def converter():
    print("=== Converter ===")
    print("1. Rupees to Dollar")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Feet")

    choice = input("Enter choice: ")

    if choice == "1":
        rupees = float(input("Enter Rupees: "))
        print("Dollar =", round(rupees / 84, 2))

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", (c * 9/5) + 32)

    elif choice == "3":
        inches = float(input("Enter inches: "))
        print("Feet =", round(inches / 12, 2))

converter()
