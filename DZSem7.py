
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

def count_vowels(word):
    vowels = "аеёиоуыэюя"
    return sum(1 for char in word if char in vowels)
def chek_rhythm(stroka):
    pharases = stroka.split()

    if len(pharases) < 2:
        return "Количество фраз должно быть больше одной!"
    
    syllables_count = [sum(count_vowels(word) for word in phrase.split('-')) for phrase in pharases]
    if all(count == syllables_count[0] for count in syllables_count):
        return "Парам пам-пам"
    else:
        return "Пам парам"
    
print(chek_rhythm(stroka))


# print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
             row.append(str(operation(i, j)))
        print(" ".join(row))