from collections import Counter

def sort_by_frequency(arr):
    """Сортирует список по частоте встречаемости элемента"""
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], arr.index(x)))


input_list = input("Введите элементы списка через пробел: ").split()
if input_list:
    try:
        numbers = [int(x) for x in input_list]
        result = sort_by_frequency(numbers)
        freq = Counter(numbers)
        print(f"Исходный список: {numbers}")
        print(f"Частота элементов: {dict(freq)}")
        print(f"Отсортировано по частоте: {result}")
    except ValueError:
        result = sort_by_frequency(input_list)
        freq = Counter(input_list)
        print(f"Исходный список: {input_list}")
        print(f"Частота элементов: {dict(freq)}")
        print(f"Отсортировано по частоте: {result}")
else:
    print("Список пуст")
