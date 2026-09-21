from typing import List

def read_integers() -> List[int]:
    line = input()
    s = line.split(",")
    res_list = []
    
    for i in s:
        res_list.append(int(i))

    return res_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
