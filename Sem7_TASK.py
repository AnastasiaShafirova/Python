# def f(x):
#     return x
# print(f(5))

# f1 = lambda x: x
# print(f1(5))

# print((lambda x: x)(5))




num = "2 4 7 4 1".split()
print(num)
num1 = list(map(int,num))
print(num1)

num1 = list(map(lambda x: int(x),num))
print(num1)

num1 = list(map(lambda x: x*2,num1))
print(num1)

num1 = list(filter(lambda x: 100,num1))
print(num1)



# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok


