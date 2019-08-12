my_list = [13, 19, 24, 29, 32, 37, 43]

def binary_search(target, lst):
    low_index = 0
    high_index = len(lst) - 1
    mid = (high_index + low_index)//2
    
    while (low_index != high_index):
        if target == lst[mid]:
            return mid
        if target > lst[mid]:
            low_index = mid + 1
            mid = (high_index + low_index)//2
        else:
            high_index = mid - 1
            mid = (high_index + low_index)//2
    
        
    return 'Not in list'

print(binary_search(37, my_list))