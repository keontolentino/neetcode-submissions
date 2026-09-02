def add_two_numbers() -> int:
    inp = input().split(",")
    total = 0
    for i in range(len(inp)):
        inp[i] = int(inp[i])
        total += inp[i]
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
