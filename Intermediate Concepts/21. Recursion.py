# ? Recursion is the process of calling function in it's own body

def fibonacci(n, f0=0, f1=1):

    if (n == 0 or n == 1):
        return f0+f1
    else:
        return f0+f1, fibonacci(n-1, f0=f1, f1=f0+f1)


print(0, 1, fibonacci(5))

# ? 0 1 1 2 3 5 8 13
