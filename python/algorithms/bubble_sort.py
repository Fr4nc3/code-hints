def bubble_sort(arr):
    print(len(arr))
    for k in range(0, len(arr) - 1):
        print("k: " + str(k))
        for i in range(0, len(arr) - k - 1):
            print("i: " + str(i))
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        print(arr)


print(bubble_sort([7, 4, 5, 2]))
