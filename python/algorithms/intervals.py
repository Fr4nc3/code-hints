ls = ["2 6", "9 12", "8 9", "18 21", "4 7", "10 11"]
# while True:
#     #ch = input('Enter an interval or press the Return key to finish: ')
#     ch = input()
#     if len(ch) != 0:
#         ls.append(ch)
#         continue
#     else:
#         break

all_n = []
for l in ls:
    s = l.split(" ")
    all_n = list(set(all_n) | set(range(int(s[0]), int(s[1]))))


f_r = list(set(range(all_n[0], all_n[-1])) - set(all_n))
print(f_r)
print(all_n)


def insertInterval(arr, interval):
    newSet = []
    endSet = []
    i = 0

    # add intervals that come before the new interval
    while i < len(arr) and arr[i][1] < interval[0]:
        newSet.append(arr[i])
        i += 1

    # add our new interval to this final list
    newSet.append(interval)

    # check each interval that comes after the new interval to determine if we can merge
    # if no merges are required then populate a list of the remaining intervals
    while i < len(arr):
        last = newSet[-1]
        if arr[i][0] < last[1]:
            newInterval = [min([last[0], arr[i][0]]), max([last[1], arr[i][1]])]
            newSet[-1] = newInterval
        else:
            endSet.append(arr[i])
        i += 1

    return newSet + endSet

#ls = ["2 6", "9 12", "8 9", "18 21", "4 7", "10 11"]
print(insertInterval([[1,5],[10,15],[20,25]], [12,27]))


from itertools import permutations

S, L = range(2), range(4) # or ExpList1, ExpList2
for p in permutations(L, len(S)):
    print(list(zip(S, p)))