# Define a method called apple_price which takes in one argument
def apple_price(num_of_apples):
    return num_of_apples * 1.00


###############
# Call the method
# What's wrong with the following code?

# print(apple_prices(10))

# 1. Write down the error message here
'''
Traceback (most recent call last):
  File "error_3.py", line 9, in <module>
    print(apple_prices(10))
NameError: name 'apple_prices' is not defined
'''

# 2. Fix the code so that it works.
print(apple_price(10))