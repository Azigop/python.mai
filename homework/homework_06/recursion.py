def print_list(l: list, n: int = 0):
    if n == (len(l)):
        return
    print(l[n])
    print_list(l, n + 1)


list_1 = input().split()

print(print_list(list_1))
