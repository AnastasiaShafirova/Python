# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def f(a,b):
    if b == 1:
        return a
    return a * f(a, b-1)
    
a = int(input('Введите число:  '))
b = int(input('Введите число:  '))
print(f)

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    if a <= 0:
       return b
    return 1 + sum(a-1,b)
    
a = int(input('Введите число:  '))
b = int(input('Введите число:  '))
print(sum)

# или

def sum(a,b):
    if b == 0:
        return a
    if b > 0:
        return sum(a + 1, b - 1)
    return sum(a - 1, b + 1) 
print(sum)