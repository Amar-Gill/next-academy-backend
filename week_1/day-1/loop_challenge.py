info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

keys = info.pop(0)

class_info = {}

for i in range(len(info)):
    class_info[str(i)] = {keys[0]:info[i][0], keys[1]:info[i][1], keys[2]: info[i][2]}

#below logic is for printing

# for key in class_info:
#     print(class_info[key])

print(class_info)

#expected output:
'''
class_info = {
  "0": {"name": "Amy", "age": 20, "pet": "bird"},
  "1": {"name": "John", "age": 21, "pet": "cat"},
  "2": {"name": "Ash", "age": 24, "pet": "dog"},
}
'''