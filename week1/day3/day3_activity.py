def is_prime(n):
    if(n%n == 0 and n%1 == n):
        return True
    else:
        return False
    
print(is_prime(7))

# Sum of digits
def sum_of_digits(n):
    result = 0
    while(n>0):
        m = n%10
        result +=m
        n = n//10
    return result

print(sum_of_digits(123))
    

# sum of digits recursive 

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n%10) + sum_of_digits(n // 10)
print(sum_of_digits(12))