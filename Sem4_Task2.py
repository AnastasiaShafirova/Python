# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# text = input("Введите текст:" )
text = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure. So if she sells sea  shells on the sea shore, I'm sure that the shells are sea shore shells "
text = text.upper()
text = text.replace('.', ' ')
text = text.split()
print(text)
print(len(set(text))) # метод set оставляет уникальные моменты, а метод len считает их