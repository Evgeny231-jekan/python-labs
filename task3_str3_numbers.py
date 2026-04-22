def max_consecutive_digits(s):
    """Находит наибольшее количество идущих подряд цифр"""
    max_len = 0
    curr_len = 0
    for ch in s:
        if ch.isdigit():
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len


text = input("Введите строку: ")
result = max_consecutive_digits(text)
print(f"Наибольшее количество идущих подряд цифр: {result}")
