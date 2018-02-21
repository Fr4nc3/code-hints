"""
Description:
    "Determine whether a circular array of relative indices is composed of
     a single complete cycle."
"""


def is_complete_cycle(array):
    """
    Determine whether a circular array of relative indices is composed of a
    single complete cycle.
    """
    # Start at the first element in the array, and keep jumping through the
    # array until we meet the original element or we have jumped more times
    # than there are elements in the array.
    count = 0
    index = 0
    while ((count == 0) or (index != 0)) and (count <= len(array)):
        count += 1
        print("entry index: {}".format(index))
        print("value: {}".format(array[index]))
        print("sum: {}".format(index + array[index]))
        index = (index + array[index]) % len(array)
        print("final: {}".format(index))

    return count == len(array)


"""
 * Example:
 *   [2, 2, -1] --> true
 *   [2, 2, 0] --> false
 *   [0] --> true
 *   [1, -1] --> true
"""

#print(is_complete_cycle([2, 2, -1]))
print(is_complete_cycle([2, 2, 0]))
#print(is_complete_cycle([1, -1]))
# print(is_complete_cycle([0]))
