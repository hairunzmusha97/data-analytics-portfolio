# Multiple Return Values
def calculate(a,b):
    return a+b,a-b

print(calculate(2,3))

# Scope (Local vs Global)
x=10

def change_x():
    x=5
    print("Inside:",x)

change_x()
print("Outside:",x)

# Mutiplication

def multiply(a,b):
    return a*b

print(multiply(2,3))

# Greet User

def greet_user(name, city):
    statement  = f"Hello {name}, welcome to {city}!"
    return statement

print(greet_user("John","Dublin"))

# square of list using set

multiplied_Numbers = set()
def square_list(numbers):
    for i in numbers:
        multiplied_Numbers.add(i *i)
    return multiplied_Numbers

print(square_list({1,2,3}))

# square of list using list

multiplied_Numbers = []
def square_list(numbers):
    for i in numbers:
        multiplied_Numbers.append(i *i)
    return multiplied_Numbers

print(square_list({1,2,3}))