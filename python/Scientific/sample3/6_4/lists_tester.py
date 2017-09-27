# *************************************
# @Fr4nc3
# 03/06/2015
# file: lists_tester.py
# *************************************
import lists


def main():
    ''' test list methods implemented in lists.py '''
    a = [1, 0, 0, 3, 4, 6, 7]
    b = [1, 0, 0, 3, 4, 6, 7]
    c = [1, 4, 5, 3, 4, 6, 7]
    d = [1, 4, 5, 8, 4, 6, 7]
    e = [1, 4, 5, 3, 4, 6, 7]
    f = [1, 4, 5, 8, 10, 6, 7]
    g = [1, 4, 5, 8, 10, 6, 7]
    h = [1, 4, 5, 8, 11, 6, 7]
    i = [1, 4, 5, 3, 4, 6, 7]
    j = [1, 0, 0, 3, 4, 6, 7]
    print(lists.swap(a))
    print(lists.shift_to_right(b))
    print(lists.replace_with_zero(c))
    print(lists.replace_with_large(d))
    print(lists.remove_middle(e))
    print(lists.move_front(f))
    print(lists.second_largest(g))
    print(lists.is_sorted(h))
    print(lists.contains_adjacent_duplicate(i))
    print(lists.contains_duplicate(j))

main()