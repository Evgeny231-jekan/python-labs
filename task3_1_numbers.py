import re

def max_float_in_string(s):
    """Находит максимальное вещественное число в строке"""
    numbers = re.findall(r'-?\d+\.\d+', s)
    if not numbers:
        return None
    return max(map(float, numbers))


text = input("Введите строку: ")
result = max_float_in_string(text)
if result is not None:
    print(f"Максимальное вещественное число: {result}")
else:
    print("Вещественные числа не найдены")
