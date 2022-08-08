a = [1]
b = [2]
print(a, b)
a[0] = b[0]

print(a[0], b[0])

def swap_list(first, second):
    first[0] = second[0]
    return first, second

print(swap_list(a, b))
print(f'{a}')
print('a')
