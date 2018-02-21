a = "columbia university"
uno = ""

for k, i in enumerate(a):
    count = 0
    # print(uno)
    for j in range(k, len(a)):
        if i == a[j]:
            count += 1
    if count % 2 != 0:
        uno +=i


#print(uno)


a = [1, 2, 3, 4, 1]
b = 1
c = -1
for k, v in enumerate(a):
    if v == b:
        #print(v)
        c = k+1

#print(c)


# print(1%2)
# print(-3%2)
# print(-2%2)
# print(-5%2)
print(-2%3)
print(2%3)
print(0%2)
print(-1%3)
print(-1%2)