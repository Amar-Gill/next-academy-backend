def global_linear_search(target, my_list):
    result = []
    for index, i in enumerate(my_list):
        if target == i:
            result.append(index)
    print(result)

bananas_arr = list("bananas")   #  ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]