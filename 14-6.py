def print_average(arr):
    if not arr:
        return 0
    a = 0
    for i in arr:
        a += i
    a = a // len(arr)
    return a
print(print_average([]))