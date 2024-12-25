def fibonacci(n):
   
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 6
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

print("----------------------------------------")


def fibonacci_series(n):
    
    a, b = 0, 1
    count = 0

    print("Fibonacci series up to", n, "numbers:")
    while count < n:
        print(a, end=" ")
       
        a, b = b, a + b
        count += 1


fibonacci_series(20)

