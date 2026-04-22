import re

def min_rational_in_string(s):
    """Находит минимальное рациональное число в строке"""
    fractions = re.findall(r'(\d+)/(\d+)', s)
    if not fractions:
        return None
    values = [int(a)/int(b) for a, b in fractions]
    min_val = min(values)
    idx = values.index(min_val)
    return f"{fractions[idx][0]}/{fractions[idx][1]}"


text = input("Введите строку: ")
result = min_rational_in_string(text)
if result:
    a, b = result.split('/')
    value = int(a)/int(b)
    print(f"Минимальное рациональное число: {result} ≈ {value:.4f}")
else:
    print("Рациональные числа не найдены")
