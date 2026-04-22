import re

def find_dates(text):
    """Находит даты формата день.месяц.год"""
    pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}\b'
    return re.findall(pattern, text)


text = input("Введите текст: ")
dates = find_dates(text)
if dates:
    print(f"Найденные даты: {dates}")
    print(f"Количество дат: {len(dates)}")
else:
    print("Даты не найдены")
