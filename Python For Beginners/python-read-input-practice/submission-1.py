def add_two_numbers() -> int:
    
    i = input()

    res = i.split(",")

    num1 = int(res[0])
    num2 = int(res[1])

    sum = num1+num2
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
