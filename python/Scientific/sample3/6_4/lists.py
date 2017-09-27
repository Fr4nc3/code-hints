# *************************************
# @Fr4nc3
# 03/06/2015
# file: lists.py
# *************************************
import copy


def swap(list):
    '''6.4.a'''
    # swap the last for the first element
    first_tem = list[0]
    last = len(list) - 1
    list[0] = list[last]
    list[last] = first_tem
    return list


def shift_to_right(list):
    '''6.4.b'''
    # shift elements to the right
    # last element is the first now
    last_item = list.pop()
    list.insert(0, last_item)

    return list


def replace_with_zero(list):
    '''6.4.c'''
    # replace even elements with zero
    for i in range(len(list)):
        if i % 2 == 0:
            list[i] = 0
    return list


def replace_with_large(list):
    '''6.4.d'''
    # replace elements to with the greatest between its neighbors
    # only first and last keep heir location
    i = 0
    while i < len(list):
        if i == 0 or i == len(list) - 1:
            i += 1
            continue
        else:
            list[i] = max(list[i], list[i - 1], list[i + 1])
        i += 1

    return list


def remove_middle(list):
    '''6.4.e'''
    # remove the middle element when the list is odd
    # remove two middle elements when the list is even
    length = len(list)
    if length % 2 == 0:
        half = int(length / 2)
        list.pop(half - 1)  # pop the element in the middle
        list.pop(half - 1)  # pop second element 
    else:
        half = length // 2 + length % 2
        list.pop(half)
    return list


def move_front(list):
    '''6.4.f'''
    # move to the front even elements
    odd_list = []
    even_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even_list.append(list[i])
        else:
            odd_list.append(list[i])

    return even_list + odd_list


def second_largest(list):
    '''6.4.g'''
    # return the second largest element
    list.remove(max(list))  # remove the first largest

    return max(list)


def is_sorted(list):
    '''6.4.h'''
    # check if the list is sorted
    list_copy = copy.copy(list)  # create a copy of the list
    list.sort()
    return list_copy == list

def contains_adjacent_duplicate(list):
    '''6.4.i'''
    # check if two adjacents number are equal
    i = 0
    ad_duplicate = False
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            ad_duplicate = True
            break
        i = i + 1

    return ad_duplicate


def contains_duplicate(list):
    '''6.4.j'''
    # check if any element is duplicated
    duplicates = False
    for i in range(len(list)):
        if list.count(list[i]) > 1:
            duplicates = True
            break

    return duplicates