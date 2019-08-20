# Run the code. Read the error message.
# Fix it

#original code below:

# def mean(numbers):
#     print(type(numbers))
#     total = sum(numbers)
#     return total / len(numbers)

# mean(5, 3, 6, 10)

def mean(*numbers):
    print(type(numbers))
    total = sum(numbers)
    return total / len(numbers)

mean(5, 3, 6, 10)
z = mean(5, 3, 6, 10)
print(z)