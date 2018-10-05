import sys


def proper_parentheses(line):

    count_p = 0  # counting parentheses
    count_s = 0  # counting happy faces
    count_r = 0  # counting sad faces

    for i in range(len(line)):
        p = line[i - 1] if i > 0 else " "
        if line[i] == "(":
            count_p += 1
        if line[i] == ")":
            count_p -= 1
        if p == ":" and line[i] == ")":
            count_s += 1
        if p == ":" and line[i] == "(":
            count_r += 1
        if count_p < 0 and count_s < abs(count_p):
            return "NO"

    return "NO" if count_p > 0 and count_r < count_p else "YES"


for line in sys.stdin:
    print(proper_parentheses(line), end="")
