#function that returns factorial of a number

def factorial(num):
    result = num
    while num != 1:
        result = result*(num - 1)
        num -=1
    return result

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))