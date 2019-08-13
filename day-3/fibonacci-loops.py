#function which returns fibanacci sequence value of a given index using loops

def fib(index):
    sequence = [0, 1]
    counter = 1
    if index == 0:
        return sequence[0]
    while counter != index:
        sequence.append(sequence[counter] + sequence[counter - 1])
        counter += 1
    return sequence[-1]


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21

