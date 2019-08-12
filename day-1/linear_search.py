def linear_search(target, my_list):
    message = 'not found'
    for index, i in enumerate(my_list):
        if i == target:
            message = index
            break
    print(message)

random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

linear_search(18, random_numbers)  # 2 (it returns the position of the number)
linear_search(9, random_numbers)   # not found