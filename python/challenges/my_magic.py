import sys


def magic_number(n, max):
    n_str = str(n) # convert number in string (list)
    n_list = list(map(int, n_str))  # list of integer
    n_l_temp= list(map(int, n_str)) # list of integer temp copy
    init = 0  #init value
    valid = []
    total = len(n_list)
    for t in range(total):
        e = n_l_temp[init]
        check = e + init
        while max * e >= len(n_l_temp) or init >= len(n_l_temp):
            n_l_temp =  n_l_temp.extend(n_l_temp)
        if n_l_temp[check] != 0 and n_l_temp[check] != e:
            if n_l_temp[check] not in valid:
                valid.append(n_l_temp[check])
                init += e
            else:
                break
        else:
            break
    return True if len(n_list) == len(valid) else False

line = "100 1000"
split = line.split(" ")
# '''if the line input is incorrect''''
if len(split) < 2:
    print("-1")
elif not split[0].isdigit() or not split[0].isdigit():
    print("-1")

magic_numbers = []
a = int(split[0])
b = int(split[1])
max = len(split[1])
for i in range(a, b + 1):
    if magic_number(i, max):
        magic_numbers.append(i)

if len(magic_numbers) > 0:
    print(*magic_numbers, sep="\n")
else:
    print("-1")
