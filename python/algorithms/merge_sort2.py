

def _split(arr):
    return (arr[: len(arr) // 2], arr[len(arr) // 2:])


def _merge(left, right):
    leftIndex = 0
    rightIndex = 0
    print("_merge")
    print(left)
    print(right)
    result = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result


def merge_sort(arr):
    if arr is None:
        return None

    if len(arr) < 2:
        return arr

    left, right = _split(arr)
    print("merge_sort")
    print(left)
    print(right)
    return _merge(merge_sort(left), merge_sort(right))


nums = [1, 6, 5, 7, 8, 2, 4, 3, 9]

print(merge_sort(nums))