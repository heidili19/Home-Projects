# Write a function to compute the Fibonacci numbers (for positive numbers)
# Fibonacci is defined as f(n) = f(n-1) + f(n-2)


def fibonacci(n):
    if n < 2:
        fn = n
        return fn
    fn = (fibonacci(n-1)) + (fibonacci(n-2))
    return fn

print ("Enter the number you want to find the fibonacci")
print ("Result is " +str(fibonacci (int(input()))))
