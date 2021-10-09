def own_enumerate(arr):
    num = 0
    for i in arr:
        b = (num, i)
        yield b
        num += 1


print(list(own_enumerate(['MAI', 'Lambda', 'Python'])))
print(list(own_enumerate('Hello MAI!')))
