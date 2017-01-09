# Fib of n 
# fn = f(n - 1) + f(n - 2)

def fib (n):
    if n < 2:
        return n
    else:
        return ((fib(n-1)) + fib(n-2))

#for n in range(0, 10):
#    print ("The bottom number is the fib of this " +str(n))
#    print (fib(n))
    
print ("Enter the fib number you would like to calculate")
userin = int(input())
result = fib (userin)
print ("The fib of " +str(userin) +" is " +str(result))




    

    
