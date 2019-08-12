names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey', 'Amard0pe']

longest_name = ''

# for name in names:
#     if len(name) > len(longest_name):
#         longest_name = name

count = 0

while count < len(names):
    if len(names[count]) > len(longest_name):
        longest_name = names[count]
    count +=1

print(longest_name)