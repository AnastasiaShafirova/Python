k = 300
a = []
b = []
for i in range(k):
    summa = 0
    for J in range(1, i // 2 + 1):
        if i%j==0:
            summa += J
    if summa > 1:
        a.append(summa)
        b.append(i)
for z in range(len(a)):
    for y in range(z):
        if a[z] == b[y] and b[z] == a[y]:
            print(b[z], b[y])
                            