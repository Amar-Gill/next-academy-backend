my_list = ['a', 'aa', 'banana', 'orange', 'aaa']

# def long_words(lst):
#     words = []
#     for word in lst:
#         if len(word) > 5:
#            words.append(word)
#     return words


# words = long_words(my_list)

words = [word for word in my_list if len(word)>5]

print(words)