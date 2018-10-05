import sys


def phone_to_word(number):
    keyboard = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret = []
    # recursive solution
    # O(n^n) with n = phone digits
    getCombination(number, ret, keyboard, "", 0)

    return ','.join(ret)


def getCombination(number, ret, keyboard, st, index):
    if index >= len(number):
        ret.append(st)
        return

    chars = keyboard.get(number[index], '')  #
    for i in chars:
        st += i
        getCombination(number, ret, keyboard, st, index + 1)
        st = st[0:len(st) - 1]  # clean temp string


for line in sys.stdin:
    print(phone_to_word(line.strip()), end="")
