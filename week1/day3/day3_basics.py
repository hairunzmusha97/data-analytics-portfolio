# Basic Function
def greet(name):
    return f"Hello {name}!"

print(greet("Musharrif"))

# Function with Default Parameter
def add(a,b=5):
    return a+b

print(add(5))
print(add(5,10))

# Factorial Function

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result
print(factorial(5))

# Recursive Approach

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

# Fibonacci 

