def cyclic_shift_right_1(arr):
    """Циклический сдвиг элементов массива вправо на 1 позицию"""
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]


input_list = input("Введите элементы списка через пробел: ").split()
if input_list:
    try:
        numbers = [int(x) for x in input_list]
        result = cyclic_shift_right_1(numbers)
        print(f"Исходный список: {numbers}")
        print(f"После сдвига вправо на 1: {result}")
    except ValueError:
        result = cyclic_shift_right_1(input_list)
        print(f"Исходный список: {input_list}")
        print(f"После сдвига вправо на 1: {result}")
else:
    print("Список пуст")
