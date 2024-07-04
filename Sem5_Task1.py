#Факториал числа

def fact(n):
    if n < 0:
        return "Ошибка ввода"
    if n == 0:
        return 1
    return n * fact(n-1)
       
print(fact(5))        





#фибоначи

def fb(x):
    if x <= 2:
       return 1
    return fb(x-1) + fb(x-2)
    
n = int(input('Введите число:  '))
print(fb(n))