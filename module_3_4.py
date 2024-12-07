def single_root_words(root_word, *other_words):
    same_words = [] #Создайте внутри функции пустой список
    words = list(other_words)# перенести слова в список др. слов
    for i in range (len (words)):# перебрать в диапазоне кол-во слов
        # логика
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    return (same_words)# вернуть 

# вывод
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
