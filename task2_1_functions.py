def count_russian_chars(s):
    """Находит общее количество русских символов в строке"""
    count = 0
    for ch in s:
        if 'а' <= ch <= 'я' or 'А' <= ch <= 'Я' or ch == 'ё' or ch == 'Ё':
            count += 1
    return count


text = input("Введите строку: ")
result = count_russian_chars(text)
print(f"Количество русских символов: {result}")
