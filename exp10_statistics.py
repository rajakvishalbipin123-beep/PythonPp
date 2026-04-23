import math

def statistics():
    arr = list(map(float, input("Enter numbers: ").split()))
    n = len(arr)

    mean = sum(arr)/n
    var = sum((x-mean)**2 for x in arr)/n
    std = math.sqrt(var)

    print("Mean:", mean)
    print("Variance:", var)
    print("Std Dev:", std)

statistics()
