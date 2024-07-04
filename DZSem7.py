
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