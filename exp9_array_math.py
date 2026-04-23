def array_math():
    n = int(input("Size: "))
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(n)]

    print("Addition:", [a[i]+b[i] for i in range(n)])
    print("Dot product:", sum(a[i]*b[i] for i in range(n)))

array_math()
