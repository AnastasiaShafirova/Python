# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

n = int(input('Введите натуральное число:  '))
last = 0
cur = 1
next = 0
count = 2
while n > cur:          
    next = last + cur      #last, cur = cur, last + cur
    last = cur             #count += 1
    cur = next
    count += 1

if next != n:
    print(-1)
else:
    print(count)