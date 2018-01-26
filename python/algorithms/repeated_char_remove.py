a = "columbia university"
uno = ""

for k,i in enumerate(a):
    count = 0
    # print(uno)
    for j in range(k, len(a)):
        if i == a[j]:
            count += 1
    if count % 2 != 0:
        uno +=i


print(uno)
