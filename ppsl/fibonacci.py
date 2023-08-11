def fibo(n):
    a, b = 0, 1
    print(a,"\n", b)
    while a<n:
        c = a+ b
        a = b
        b = c
        print(c)
