# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

sp = [1, 1, 2, 0, -1, 3, 4, 4]
a = []
for c in sp:
    if c not in a:
        a.append(c)
print(len(a))


print(len(set(sp)))
st = set() # пустое множество