def count_min_elements(arr):
    """Находит количество минимальных элементов"""
    if not arr:
        return 0
    min_val = min(arr)
    return arr.count(min_val)


input_list = input("Введите целые числа через пробел: ").split()
try:
    numbers = [int(x) for x in input_list]
    result = count_min_elements(numbers)
    min_val = min(numbers) if numbers else None
    print(f"Список: {numbers}")
    print(f"Минимальный элемент: {min_val}")
    print(f"Количество минимальных элементов: {result}")
except ValueError:
    print("Ошибка: введите целые числа!")
