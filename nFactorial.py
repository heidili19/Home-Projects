# Factorial Recursively for n! (0 or greater numbers)
# n * (n-1) * (n-2) * (n-3) ...

def nFactorial(n):
    if n < 3:
        return n
    else:
        return (n * nFactorial(n - 1))

x = nFactorial(4)
print (x)
    

    
