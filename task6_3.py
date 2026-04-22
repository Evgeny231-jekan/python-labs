def count_even(arr):
    """Находит количество четных элементов"""
    return sum(1 for x in arr if x % 2 == 0)


input_list = input("Введите целые числа через пробел: ").split()
try:
    numbers = [int(x) for x in input_list]
    result = count_even(numbers)
    print(f"Список: {numbers}")
    print(f"Количество четных элементов: {result}")
except ValueError:
    print("Ошибка: введите целые числа!")
