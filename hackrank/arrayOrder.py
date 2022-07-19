def isOrder(a):
    b =[]
    n = len(a)
    for i in range(n):
        if len(a)>0:
            b.append(a.pop(0))
        if len(a)>0:
            b.append(a.pop(-1))
    flag = True
    print(b)
    for i in range(n-1):
        if b[i] > b[i + 1]:
            flag = False
            break
    print(flag)
        


c = [1, 3, 5, 6, 4, 2]
isOrder(c)
isOrder([1, 4, 5, 6, 3])