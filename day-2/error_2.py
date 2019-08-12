# Define a method called student_details that takes in two arguments

def user_details(name, occupation):
    return f"Hi! My name is {name} and I am a {occupation}."

######
# Call the method
user_name = "Glo"
user_occupation = "Lecturer"
print(user_details(user_name, user_occupation))

# 1. Write the error message here:
'''
Traceback (most recent call last):
  File "error_2.py", line 10, in <module>
    print(user_details(user_name, user_occupation))
NameError: name 'user_occupation' is not defined
'''
# 2. Fix the code so that it works.
'''changed user_occupatian to user_occupation = Lecturer '''