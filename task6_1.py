def cyclic_shift_right_2(arr):
    """Циклический сдвиг элементов массива вправо на 2 позиции"""
    if len(arr) <= 2:
        return arr[:]
    return arr[-2:] + arr[:-2]


input_list = input("Введите элементы списка через пробел: ").split()
if input_list:

    try:
        numbers = [int(x) for x in input_list]
        result = cyclic_shift_right_2(numbers)
        print(f"Исходный список: {numbers}")
        print(f"После сдвига вправо на 2: {result}")
    except ValueError:
      
        result = cyclic_shift_right_2(input_list)
        print(f"Исходный список: {input_list}")
        print(f"После сдвига вправо на 2: {result}")
else:
    print("Список пуст")
