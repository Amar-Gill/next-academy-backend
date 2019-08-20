#function which returns fibonacci sequence number of a given index using recursion

def fib(index):

    if index == 0:
        return 0
    if index == 1:
        return 1
    
    return fib(index-1) + fib(index-2)


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
