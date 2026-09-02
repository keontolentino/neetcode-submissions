from typing import List

def read_integers() -> List[int]:
    lst = input().split(",")
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
