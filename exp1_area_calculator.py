import math

def calculate_area():
    print("=== Area Calculator ===")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area of Circle =", round(math.pi * r * r, 2))

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of Rectangle =", l * w)

    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of Triangle =", 0.5 * b * h)

    else:
        print("Invalid choice!")

calculate_area()
