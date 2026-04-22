def sort_by_length(strings):
    """Сортирует строки по длине"""
    return sorted(strings, key=len)


print("Введите строки (для завершения введите пустую строку):")
strings = []
while True:
    line = input()
    if line == "":
        break
    strings.append(line)

if strings:
    sorted_strings = sort_by_length(strings)
    print("\nИсходный список:")
    for s in strings:
        print(f"  '{s}' (длина: {len(s)})")
    print("\nОтсортировано по длине:")
    for s in sorted_strings:
        print(f"  '{s}' (длина: {len(s)})")
else:
    print("Список пуст")
