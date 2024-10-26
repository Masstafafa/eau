numbers = list(range(0, 1000))
string_number = [f'{number:03}' for number in numbers]

for i in string_number:
    if i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
        print(i, end=", ")

